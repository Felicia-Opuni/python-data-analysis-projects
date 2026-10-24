expenses = [
    {
        "description": "Lunch",
        "amount": 35,
        "category": "Food",
        "date": "2026-03-15"
    },
    {
        "description": "Transport",
        "amount": 20,
        "category": "Transport",
        "date": "2026-03-16"
    },
    {
        "description": "Electricity bill",
        "amount": 120,
        "category": "Utilities",
        "date": "2026-04-02"
    },
    {
    "description": "Groceries",
    "amount": 85,
    "category": "Food",
    "date": "2026-03-20"
    },
    {
        "description": "Internet bundle",
        "amount": 60,
        "category": "Utilities",
        "date": "2026-04-05"
    },
    {
        "description": "Taxi",
        "amount": 45,
        "category": "Transport",
        "date": "2026-04-10"
    },
    {
        "description": "School supplies",
        "amount": 75,
        "category": "Education",
        "date": "2026-05-03"
    },
    {
        "description": "Lunch",
        "amount": 30,
        "category": "Food",
        "date": "2026-05-12"
    },
    {
        "description": "Electricity bill",
        "amount": 150,
        "category": "Utilities",
        "date": "2026-05-18"
    },
    {
        "description": "Bus fare",
        "amount": 25,
        "category": "Transport",
        "date": "2026-06-02"
    },
    {
        "description": "Groceries",
        "amount": 95,
        "category": "Food",
        "date": "2026-06-08"
    }
 
]

budgets = {
    "Food": 200,
    "Transport": 100,
    "Utilities": 300,
    "Education": 100,
    "Entertainment": 80
}



def calculate_total(expenses):
    total = 0

    for expense in expenses:
        
        total = total + expense["amount"]

    
    return total



def calculate_monthly_totals(expenses):

    monthly_totals = {}
    
    for expense in expenses:
        month = expense["date"][0:7]
        amount = expense["amount"]
        
        if month in monthly_totals:
            monthly_totals[month] += amount

        else:
            monthly_totals[month] = expense["amount"]
            
    return monthly_totals




def calculate_category_totals(expenses):

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        
        if category in category_totals:
            category_totals[category] += amount

        else:
            category_totals[category] = expense["amount"]

    return category_totals






def check_budget(expenses,budgets):

    category_dict = calculate_category_totals(expenses)
    for x,y in budgets.items():
        if not category_dict.get(x,0):
            print(x,"has no recorded spending")
        else:
            if category_dict[x] > y:
                spend_over = category_dict[x] - y
                print(x," -- Actual spending: GHC",category_dict[x],", Budget: GHC",y, "-- Over budget by GHC",spend_over)
            else:
                spend_under = y - category_dict[x]
                print(x,"-- Actual spending: GHC",category_dict[x],", Budget: GHC",y, "--Budget money left GHC",spend_under)



print("Total spending:",calculate_total(expenses))
print("\n Monthly Total Expenditure\n\n",calculate_monthly_totals(expenses))
print("\n Category Total Expenditure\n\n",calculate_category_totals(expenses))
print("\n Budgets\n")
check_budget(expenses,budgets)

empty_expenses = []
print(calculate_total(empty_expenses))
print(calculate_monthly_totals(empty_expenses))
print(calculate_category_totals(empty_expenses))
check_budget(empty_expenses,budgets)