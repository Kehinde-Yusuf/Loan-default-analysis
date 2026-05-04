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
