# Loan Default Analysis (Python)

## Project Overview
This project analyzes a financial loan dataset to understand the factors influencing loan repayment and default behavior. 

The analysis focuses on identifying key drivers such as credit score, income, and employment history, and how they impact the likelihood of a borrower fully repaying a loan or defaulting.

The goal of this project is to extract meaningful insights that can help financial institutions make better lending decisions and reduce credit risk.

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- VS Code

## Dataset
The dataset used for this analysis is a financial loan dataset obtained from Kaggle. It contains information about borrowers, including credit score, income, loan status, and other financial attributes.

Key columns include:
- Loan Status
- Credit Score
- Annual Income
- Years in Current Job
- Home Ownership
- Purpose

## Data Cleaning Methodology

1. Objective

The dataset was cleaned using Python to ensure consistency, accuracy, and readiness for analysis.

2. Cleaning Steps
   
2.1 Removal of Text from Numerical Fields

The “Years in current job” column contained mixed formats such as “10+ years”, “3 years”, and “< 1”.
All text elements like “years”, “year”, and “+” were removed to retain only numeric values.

2.2 Handling Special Values

The value “< 1” was replaced with 0 to maintain consistency and ensure all values are numeric.

2.3 Handling Missing Values

Missing values (NaN) in the column were replaced with 0 using fillna().
This ensured completeness of the dataset and allowed all records to be included in the analysis.

2.4 Data Type Conversion

The column was converted from string to integer type to enable numerical analysis and calculations.

3. Outcome

After cleaning, the dataset became structured, consistent, and suitable for analysis and modelling.

## Key Findings
-The dataset is complete after preprocessing, with no missing values across all variables, indicating that all necessary data cleaning steps have been successfully applied.

-Most borrowers have strong employment history, with 10+ years in current job being the most common group, suggesting a generally stable workforce.

-Loan performance shows that 77% of loans are fully paid, while 23% are charged off, indicating a relatively strong repayment rate with some level of credit risk.

-Credit scores are mostly concentrated within a moderate range (approximately 585 to 751), showing that borrowers generally fall within mid to good credit profiles.

-Borrowers with fully paid loans have slightly higher average annual income compared to those with charged-off loans, suggesting income has some influence on repayment behaviour but is not the only factor.

-Some inconsistencies were observed in credit score aggregation results, indicating that further validation may be required to ensure full data accuracy.

## Conclusion

Overall, the analysis shows that the loan portfolio is relatively stable, with a high proportion of successfully repaid loans and a borrower base that is generally experienced and financially active. However, the presence of charged-off loans highlights existing credit risk that should be monitored. While income and employment history provide useful indicators, they do not fully explain repayment outcomes, suggesting that other factors also influence loan performance.

