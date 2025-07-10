import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('EXPENSES.csv', parse_dates = ['DATE'])

totalExpense = df['Amount'].sum()
print("Total Expense = {totalExpense} ")

dailyTotal = df.groupby('Date')['Amount'].sum()
print("Daily Expenses= {dailyTotal}")

avgTotal = dailyTotal.mean()

category_expense = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print("\nCategory-wise Expenses:")
print(category_expense)

highest_category = category_expense.idxmax()
print(f"\nHighest Expense Category: {highest_category}")

lowest_category = category_expense.idxmin()
print(f"\nLowest Expense Category: {lowest_category}")

category_expense.plot(kind='bar', title='Expenses by Category', figsize=(8,5), color='skyblue')
plt.xlabel('Category')
plt.ylabel('Amount Spent (₹)')
plt.tight_layout()
plt.savefig("category_expense_chart.png")