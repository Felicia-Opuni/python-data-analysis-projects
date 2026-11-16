# Sales Data Generator & Analyzer

## Project Overview

The Sales Data Generator & Analyzer is a Python project that generates random sales records and performs basic sales analysis.

The program creates fictional sales data using randomly selected products, quantities, regions, salespeople, and dates. It then analyzes the generated records to provide useful sales insights.

This project was built as part of my Python learning journey, focusing on data analysis, functions, dictionaries, loops, and sorting.

## Features

### 1. Random Sales Generation
- Generates a specified number of sales records.
- Randomly selects products, quantities, regions, and salespeople.
- Assigns product categories and prices based on the selected product.
- Generates random dates within 2026.
- Calculates revenue for each transaction.

### 2. Sales Performance Analysis
- Calculates total revenue.
- Counts total sales transactions.
- Calculates average sale value.
- Identifies the highest and lowest sales.

### 3. Revenue Analysis
Calculates total revenue by:
- Product
- Category
- Region
- Salesperson

### 4. Sales Ranking
Ranks products, categories, regions, and salespeople according to their revenue, from highest to lowest.

The program can also display the top three performers in each category.

### 5. Error and Edge Case Handling
- Handles empty sales lists.
- Prevents errors when calculating averages or finding the highest and lowest sales without records.
- Tested with different dataset sizes, including 0, 1, 10, 500, and 1,000 sales records.

## Technologies Used

- Python 3
- Random module
- Datetime module

## Python Concepts Practised

- Variables and data types
- Lists and dictionaries
- For loops
- Conditional statements
- Functions and function reuse
- Dictionary methods (`get()` and `items()`)
- List slicing
- Sorting with `sorted()`
- Lambda functions
- Random data generation
- Date and time handling
- Error handling and testing

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Felicia-Opuni/python-data-analysis-projects.git
   ```

2. Navigate to the project folder:

   ```bash
   cd python-data-analysis-projects/sales-data-generator
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## Project Structure

```text
sales-data-generator/
│
└── main.py
```

## Learning Outcomes

Through this project, I improved my understanding of how to:

- Generate and manage structured datasets using Python.
- Write reusable functions for data analysis.
- Calculate and group revenue using dictionaries.
- Sort data and identify top-performing items.
- Test programs using different dataset sizes and empty datasets.

## Future Improvements

- Save generated sales records to CSV files.
- Read and analyze sales data from external CSV files.
- Generate visual reports using Matplotlib.
- Add monthly sales analysis.
- Create an interactive sales dashboard.

---

**Author:** Felicia Opuni

**Project:** Week 3 – Python Data Analysis Projects