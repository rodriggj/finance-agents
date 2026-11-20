# Purpose: 
> An AI-powered fundamental stock analysis pipeline built with the OpenAI Agents SDK. Five specialist agents (financial data, valuation, news/sentiment, risk, report writer) collaborate under an Orchestrator to produce a professional investment brief for any publicly traded stock.

# Fundamental Analysis
> Fundamental analysis consists of determing a company's intrinsic value, meaning what the business is actually worth, independent of what the stock price. This contrasts to technical analysis which focuses on predicting the future price movements by analyzing historical price charst and trading volume. 

## Two complimentary pillars of Fundamentals Analysis 
1. `Quantitiative Analysis`: A focus on the numbers. Three (3) financial statements form this foundation: 1. `income statement`, 2. `balance sheet`, & 3. `cash flow`. The output of the analysis is a review of ratios that provide insight into profitability, financial strength, efficiency, and valuation. 

2. `Qualitative Analysis`: A focus on the narrative. These tend to evaluate competitive advantage, management allocation of capital, industry trends. The output of this analysis is signals are extracted from earnings, mgmt interviews, industry reports, news, etc. 

## Intended Outcome 
Every public company produces three (3) core financial statements on a regular basis. This solution will establish agents, a workflow, and specific criteria, and a synthesis of these 3 core documents: 

1. `income statement`: evaluating specifically 
    1. Revenue, 
    2. Gross Profit, 
    3. Operating Income, 
    4. Net Income

2. `balance sheet`:  evaluating specifically 
    1. Cash and Equivalents 
    2. Total Debt & 
    3. Shareholder's Equity. 

3. `cash flow statement`: evaluating specifically 
    1. Operating Cash Flow, 
    2. Capital Expenditures & 
    3. Free Cash Flow 

Key Ratios that these documents and metrics will be contribute to are: 

1. `Valuation Ratios`: specifcally 
    1. Price to Earnings (P/E) ratio 
    2. Price to Book (P/B) ratio 
    3. Price to Sales (P/S) ratio, 
    4. Enterprise Value to Earnings Before Interest, Taxes, Depreciation (EV/EBITDA) & 
    5. Enterprise Value to Revenue (EV/R) ratio. 

2. `Profitability Ratios`: specifically 
    1. Gross Margin, 
    2. Operating Margin, 
    3. Net Margin, 
    4. Return on Equity (ROE), & 
    5. Return on Assets (ROA). 

3. `Liquiditity and Leverage Ratios`: specically 
    1. Current Ratio, 
    2. Quick Ratio, & 
    3. Debt-to-equity-ratio (Debt/equity). 

4. `Growth Metrics` ratios: specifically 
    1. Revenue growth (YoY), 
    2. Revenue Growth (3-year), 
    3. Earnings Growth (YoY), & 
    4. Earnings Growth (Qtrly)

5. `Dividend ratios`: specifcally 
    1. Dividend yield, 
    2. Payout ratio, & 
    3. Annual Dividend rate


