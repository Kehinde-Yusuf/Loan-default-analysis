import pandas as pd

df = pd.read_csv("credit_train.csv")

df['Credit Score'] = df['Credit Score'].fillna(df['Credit Score'].median())
df['Annual Income'] = df['Annual Income'].fillna(df['Annual Income'].median())
df['Years in current job'] = df['Years in current job'].fillna(df['Years in current job'].mode()[0])
df.drop('Months since last delinquent', axis=1, inplace=True)

df = df.dropna()
print(df.isnull().sum())

print(df['Years in current job'].head(20))
print(df['Years in current job'].unique())

print(df['Years in current job'].value_counts())

df['Years in current job'] = df['Years in current job'].str.replace(' years', '')
df['Years in current job'] = df['Years in current job'].str.replace(' year', '')
df['Years in current job'] = df['Years in current job'].str.replace('+', '')

# handle missing values
df['Years in current job'] = df['Years in current job'].fillna('0')

# handle "< 1"
df['Years in current job'] = df['Years in current job'].replace('< 1', '0')

# convert to integer
print(df['Years in current job'].astype(int))

print(df.isnull().sum())

#Analyze the dataset
print(df['Loan Status'].value_counts())
print(df['Loan Status'].value_counts(normalize=True) * 100)
print(df.groupby('Loan Status')['Credit Score'].mean())
print(df.groupby('Loan Status')['Annual Income'].mean())

print(df['Credit Score'].describe())
print(df['Credit Score'].sort_values().head(10))
print(df['Credit Score'].sort_values().tail(10))

df.loc[df['Credit Score'] > 850, 'Credit Score'] = df['Credit Score'] / 10
df['Credit Score'] = df['Credit Score'].clip(300, 850)

print(df['Credit Score'].describe())

import matplotlib.pyplot as plt


# 1. Loan Status
df['Loan Status'].value_counts().plot(kind='bar')
plt.title('Loan Status Distribution')
plt.xlabel('Loan Status')
plt.ylabel('Count')
plt.show()
plt.close()

# 2. Credit Score vs Loan Status
df.boxplot(column='Credit Score', by='Loan Status')
plt.title('Credit Score by Loan Status')
plt.suptitle('')
plt.savefig('credit_score_by_loan_status.png')
plt.show()
plt.close()

# 3. Income vs Loan Status
df.boxplot(column='Annual Income', by='Loan Status')
plt.title('Income by Loan Status')
plt.suptitle('')
plt.savefig('income_by_loan_status.png')
plt.show()
plt.close()

