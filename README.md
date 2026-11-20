# Purpose: 
> An AI-powered fundamental stock analysis pipeline built with the OpenAI Agents SDK. Five specialist agents (financial data, valuation, news/sentiment, risk, report writer) collaborate under an Orchestrator to produce a professional investment brief for any publicly traded stock.

# Fundamental Analysis
> Fundamental analysis consists of determing a company's intrinsic value, meaning what the business is actually worth, independent of what the stock price. This contrasts to technical analysis which focuses on predicting the future price movements by analyzing historical price charst and trading volume. 

## Two complimentary pillars of Fundamentals Analysis 
1. `Quantitiative Analysis`: A focus on the numbers. Three (3) financial statements form this foundation: 1. `income statement`, 2. `balance sheet`, & 3. `cash flow`. The output of the analysis is a review of ratios that provide insight into profitability, financial strength, efficiency, and valuation. 

2. `Qualitative Analysis`: A focus on the narrative. These tend to evaluate competitive advantage, management allocation of capital, industry trends. The output of this analysis is signals are extracted from earnings, mgmt interviews, industry reports, news, etc. 

## Intended Outcome 
Every public company produces three (3) core financial statements on a regular basis. This solution will establish agents, a workflow, and specific criteria, and a synthesis of these 3 core documents: 

1. `income statement`: evaluating specifically: 
    - Revenue, 
    - Gross Profit, 
    - Operating Income, 
    - Net Income

2. `balance sheet`:  evaluating specifically:
    - Cash and Equivalents 
    - Total Debt & 
    - Shareholder's Equity

3. `cash flow statement`: evaluating specifically 
    - Operating Cash Flow, 
    - Capital Expenditures & 
    - Free Cash Flow 

Key Ratios that these documents and metrics will be contribute to are: 

1. `Valuation Ratios`: specifcally: 
    - Price to Earnings (P/E) ratio 
    - Price to Book (P/B) ratio 
    - Price to Sales (P/S) ratio, 
    - Enterprise Value to Earnings Before Interest, Taxes, Depreciation (EV/EBITDA) & 
    - Enterprise Value to Revenue (EV/R) ratio

2. `Profitability Ratios`: specifically: 
    - Gross Margin, 
    - Operating Margin, 
    - Net Margin, 
    - Return on Equity (ROE), & 
    - Return on Assets (ROA) 

3. `Liquiditity and Leverage Ratios`: specically: 
    - Current Ratio, 
    - Quick Ratio, & 
    - Debt-to-equity-ratio (Debt/equity)

4. `Growth Metrics` ratios: specifically 
    - Revenue growth (YoY), 
    - Revenue Growth (3-year), 
    - Earnings Growth (YoY), & 
    - Earnings Growth (Qtrly)

5. `Dividend ratios`: specifcally 
    - Dividend yield, 
    - Payout ratio, & 
    - Annual Dividend rate


