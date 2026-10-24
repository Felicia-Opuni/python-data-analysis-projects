# Expense Tracker & Spending Analyzer

## About the Project

The Expense Tracker & Spending Analyzer is a beginner-friendly Python project that records expenses, analyzes spending patterns, and compares actual expenditure against predefined budgets.

The project uses Python dictionaries, lists, loops, conditional statements, and functions to organize and analyze expense data.

## Features

- **Total Spending:** Calculates the total amount spent across all recorded expenses.
- **Monthly Spending Analysis:** Groups expenses by month and calculates monthly totals.
- **Category Analysis:** Calculates total spending for each expense category.
- **Budget Tracking:** Compares actual spending against category budgets.
- **Overspending Detection:** Identifies categories where spending exceeds the budget and calculates the excess amount.
- **Remaining Budget:** Calculates how much money remains when spending is within budget.
- **Missing Category Handling:** Reports budget categories that have no recorded spending.
- **Empty Data Handling:** Tests how the analysis functions behave when given an empty expense list.

## Technologies Used

- Python 3
- Python dictionaries and lists
- Functions, loops, and conditional statements

## Project Structure

```text
expense-tracker/
├── main.py
└── README.md
```

## Sample Data

The project uses sample expense records containing the following information:

- Description
- Amount
- Category
- Date

Example expense:

```python
{
    "description": "Lunch",
    "amount": 35,
    "category": "Food",
    "date": "2026-03-15"
}
```

The project uses Ghana cedis (GHC) as the currency for expense and budget calculations.

## Budget Tracking Example

The project uses predefined budgets for different categories, including Food, Transport, Utilities, and Education.

| Category | Actual Spending | Budget | Result |

| Food | GHC 245 | GHC 200 | Over budget by GHC 45 |
| Transport | GHC 90 | GHC 100 | GHC 10 remaining |
| Utilities | GHC 330 | GHC 300 | Over budget by GHC 30 |
| Education | GHC 75 | GHC 100 | GHC 25 remaining |

Categories with no recorded expenses are reported separately.

## How to Run the Project

1. Install Python 3 if it is not already installed.
2. Clone the repository or download the project files.
3. Open a terminal in the `expense-tracker` directory.
4. Run the following command:

```bash
python main.py
```

The program will display total spending, monthly spending totals, category totals, and budget reports, depending on which function calls are enabled in `main.py`.

## What I Learned

Through this project, I practiced:

- Organizing related data using lists of dictionaries.
- Writing reusable functions.
- Calculating totals using loops.
- Grouping data by month and category.
- Using dictionaries to track and compare spending.
- Handling missing dictionary keys.
- Testing functions with empty lists.
- Applying conditional logic to identify overspending.

## Future Improvements

Possible improvements include:

- Allowing users to enter expenses through the terminal.
- Saving expense records to a CSV or JSON file.
- Adding input validation and error handling.
- Generating charts to visualize spending patterns.
- Producing a more detailed monthly financial report.

## Author

Created as part of my Python project-based learning journey, with a focus on data analysis and data science.

