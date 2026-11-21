# Pronpting Technique: PCIF 

# Persona, Context, Instructions, & Format (PCIF)
PCIF is a four-part way to write an agent instruction so the model knows who it is, what situation it is in, what to do, and how to answer. In this project it is the string stored in FINANCIAL_DATA_INSTRUCTIONS and passed to the OpenAI model as the agent's operating policy.


| Letter | Part	| What it fixes	| In this agent | 
| ------ | ---- | ------------- | ------------- | 
| P | Persona | Who the model should act as | "You are a senior financial analyst specializing in reading and interpreting corporate financial statements." |
| C | Context | The situation and the job | "Given a stock ticker, retrieve the company's financial statements and compute key fundamental ratios." |
| I | Instructions | The exact steps, in order | Call get_income_statement, then get_balance_sheet, then get_cash_flow_statement, then compute_key_ratios. |
| F | Format | The shape of the answer | Five named sections, a verdict limited to STRONG, SOLID, MIXED, or WEAK, and the strict rules about citing numbers. | 

Each part answers a different question, so you can change one without rewriting the others. Changing the persona does not change the tool order. Changing the section headings does not change which statements the agent fetches.

In `financial_analyst_agent.py` those four parts sit in one string. The Agents SDK sends that string as the system instructions, and the ticker the user types later is the per-run input. The instructions stay the same for every company. Only the ticker changes.

The instructions part is what makes this an agent prompt rather than a one-shot question. It names the four tools and the order to call them, and it says what each call is for: revenue and earnings, the balance sheet, cash flow, then ratios. The model is expected to call those tools before it writes the summary.

The format part is what later agents can rely on. The Orchestrator and Valuation Agent can look for REVENUE & PROFITABILITY, BALANCE SHEET HEALTH, CASH FLOW QUALITY, KEY RATIOS SNAPSHOT, and FINANCIAL HEALTH VERDICT because the prompt requires those headings every time. The strict rules tighten that format further: every claim needs a number from a tool, each section stays inside its own data, and a missing figure has to be called out.