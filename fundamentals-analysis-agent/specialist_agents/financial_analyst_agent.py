"""
financial_data_agent.py
-----------------------
Specialist agent for retrieving and interpreting financial statements.

This agent is the data foundation of the pipeline. It uses four tools to
fetch the income statement, balance sheet, cash flow statement, and a
computed set of key ratios. It returns structured, interpreted findings
that the Orchestrator and Valuation Agent will consume downstream.
"""

from agents import Agent
from fundamentals_analysis_agent.tools.financial_tools import (
    get_income_statement,
    get_balance_sheet,
    get_cash_flow_statement,
    compute_key_ratios,
)
from dotenv import load_dotenv
import os

load_dotenv()

class FinancialAnalystAgent(Agent):
    def __init__(self, name="Financial Analyst"):
        super().__init__(name=name)
        self.tools = [get_income_statement, get_balance_sheet, get_cash_flow_statement, compute_key_ratios]
        self.model = os.getenv("MODEL")
        self.temperature = 0.0
        self.max_tokens = 1000