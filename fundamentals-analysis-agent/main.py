"""CLI entry point for the fundamentals analysis pipeline.

With a ticker, this runs FinancialDataAgent and then NewsAndSentimentAgent.
Without one, it only checks the OpenAI API key.

Examples:
    python main.py
    python main.py --ticker AAPL
"""

from __future__ import annotations

import argparse
import sys

from dotenv import load_dotenv
from openai import APIConnectionError, APIStatusError, AuthenticationError, OpenAI


PLACEHOLDER_VALUES = {
    "",
    "sk-your-openai-api-key-here",
}


def check_api_key() -> int:
    """Verify OPENAI_API_KEY is set and accepted by the OpenAI API.

    Call this before any agent run. Returns 0 when the key is valid, 1 otherwise.
    """
    load_dotenv()

    client = OpenAI()
    key = client.api_key or ""

    if key.strip() in PLACEHOLDER_VALUES:
        print("OPENAI_API_KEY is missing. Copy .env.example to .env and set a real key.")
        return 1

    try:
        page = client.models.list()
        model_ids = [model.id for model in page.data]
    except AuthenticationError:
        print("OPENAI_API_KEY was rejected (401). Check the key on platform.openai.com.")
        return 1
    except APIConnectionError as exc:
        print(f"Could not reach the OpenAI API: {exc}")
        return 1
    except APIStatusError as exc:
        print(f"OpenAI API returned status {exc.status_code}: {exc.message}")
        return 1

    preview = f"{key[:7]}...{key[-4:]}" if len(key) > 12 else "(set)"
    print(f"OPENAI_API_KEY is valid ({preview}).")
    print(f"Account can list {len(model_ids)} models.")
    return 0


def run_financial_analysis(ticker: str) -> str:
    """Run FinancialDataAgent for a ticker and return its structured analysis.

    The agent fetches the income statement, balance sheet, cash flow statement,
    and key ratios, then writes the summary defined in its instructions.
    """
    symbol = ticker.strip().upper()
    if not symbol:
        raise ValueError("A ticker symbol is required, for example AAPL.")

    from agents import Runner
    from agents.exceptions import AgentsException

    from specialist_agents.financial_analyst_agent import financial_data_agent

    load_dotenv()
    result = Runner.run_sync(
        financial_data_agent,
        (
            f"Analyze the financial statements for {symbol}. "
            "Follow your required tool sequence and return the structured summary."
        ),
    )
    if not result.final_output:
        raise AgentsException(f"FinancialDataAgent returned no analysis for {symbol}.")
    return str(result.final_output)


def run_news_sentiment(ticker: str) -> str:
    """Run NewsAndSentimentAgent for a ticker and return its structured report.

    The agent fetches recent headlines, scores sentiment, and writes the
    report defined in its instructions.
    """
    symbol = ticker.strip().upper()
    if not symbol:
        raise ValueError("A ticker symbol is required, for example AAPL.")

    from agents import Runner
    from agents.exceptions import AgentsException

    from specialist_agents.news_sentiment_agent import news_sentiment_agent

    load_dotenv()
    result = Runner.run_sync(
        news_sentiment_agent,
        (
            f"Analyze recent news and investor sentiment for {symbol}. "
            "Follow your required tool sequence and return the structured sentiment report."
        ),
    )
    if not result.final_output:
        raise AgentsException(f"NewsAndSentimentAgent returned no report for {symbol}.")
    return str(result.final_output)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check the OpenAI API key, or run the financial and news sentiment "
            "agents for a ticker."
        ),
    )
    parser.add_argument(
        "--ticker",
        help="Stock ticker to analyze, for example AAPL. Omit to only check the API key.",
    )
    args = parser.parse_args(argv)

    if args.ticker is not None and sys.version_info < (3, 10):
        current = sys.version.split()[0]
        print(
            "The analysis agents require Python 3.10 or newer "
            f"(this interpreter is {current})."
        )
        print("Recreate the virtual environment with a newer Python:")
        print("  /opt/homebrew/bin/python3 -m venv .venv")
        print("  source .venv/bin/activate")
        print("  pip install -r requirements.txt")
        return 1

    status = check_api_key()
    if args.ticker is None or status != 0:
        return status

    from agents.exceptions import AgentsException

    symbol = args.ticker.strip().upper()
    agent_errors = (
        ValueError,
        AgentsException,
        AuthenticationError,
        APIConnectionError,
        APIStatusError,
    )
    failed = False

    print(f"Running FinancialDataAgent for {symbol}...")
    try:
        print(run_financial_analysis(symbol))
    except agent_errors as exc:
        print(f"Financial analysis failed: {exc}")
        failed = True

    print(f"Running NewsAndSentimentAgent for {symbol}...")
    try:
        print(run_news_sentiment(symbol))
    except agent_errors as exc:
        print(f"News and sentiment analysis failed: {exc}")
        failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
