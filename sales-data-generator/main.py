import random
import datetime


products = [
    "Laptop","Smartphone",
    "Headphones","Tablet",
    "Keyboard","Mouse"
]


regions = [
    "Accra","Kumasi",
    "Tamale","Takoradi",
    "Cape Coast"
]


salespeople = [
    "Ama","Kojo",
    "Abena","Kofi",
    "Akosua"
]


product_categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Headphones": "Accessories",
    "Tablet": "Electronics",
    "Keyboard": "Accessories",
    "Mouse": "Accessories"
}


product_prices = {
    "Laptop": 3500,
    "Smartphone": 2500,
    "Headphones": 250,
    "Tablet": 1800,
    "Keyboard": 150,
    "Mouse": 80
}



def generate_random_date():
    start_date = datetime.date(2026, 1, 1)
    end_date = datetime.date(2026, 12, 31)

    date_diff = end_date - start_date

    total_days = date_diff.days
    random_days = random.randint(0,total_days)

    random_date = start_date + datetime.timedelta(days=random_days)

    return random_date


def generate_sales(number_of_sale):
    sales_list = []
    for i in range(number_of_sale):
        product = random.choice(products)
        quantity = random.randint(1, 10)
        price = product_prices[product]
        revenue = price * quantity
        category = product_categories[product]
        region = random.choice(regions)
        salesperson = random.choice(salespeople)
        date = generate_random_date()

        
        sale = {
            "Product" : product,
            "Category" : category,
            "Quantity" : quantity,
            "Unit price" : round(price,2),
            "Revenue" : revenue,
            "Region" : region,
            "Salesperson" : salesperson,
            "Date" : date.strftime("%Y-%m-%d")
        }

        sales_list.append(sale)

    return sales_list




def calculate_total_revenue(sales):
    total_revenue = 0
    for sale in sales:
        revenue_calc = sale["Revenue"]
        total_revenue += revenue_calc
        
    return total_revenue

def calculate_total_transaction(sales):
    if len(sales) == 0:
        print("No sales has been recorded")
    return len(sales)


def calculate_average_sale(sales):

    if not sales:
        return "No sales is recorded. Record sale and try again"
        
    
    average_sale = calculate_total_revenue(sales) / calculate_total_transaction(sales)

    return round(average_sale,2)




def calculate_product_revenue(sales):
    product_revenue = {}

    for sale in sales:
        product = sale.get("Product",0)
        revenue = sale.get("Revenue",0) 

        product_revenue[product] = product_revenue.get(product, 0) + revenue

    return product_revenue


def calculate_category_revenue(sales_list):
    category_revenue = {}

    for sale in sales_list:

        category = sale.get("Category",0)
        revenue = sale.get("Revenue",0)

        category_revenue[category] = category_revenue.get(category,0) + revenue
    return category_revenue



def calculate_region_revenue(sales_list):
    region_revenue = {}
    for sale in sales_list:
        region = sale.get("Region",0)
        revenue = sale.get("Revenue",0)

        region_revenue[region] = region_revenue.get(region,0) + revenue

    return region_revenue


def calculate_salesperson_revenue(sales_list):
    salesperson_revenue = {}

    for sale in sales_list:
        salesperson = sale.get("Salesperson",0)
        revenue = sale.get("Revenue",0)

        salesperson_revenue[salesperson] = salesperson_revenue.get(salesperson,0) + revenue

    return salesperson_revenue


def find_highest_sale(sales):
    if not sales:
        return "No sales is recorded. Record sale and try again"
    
    highest_sale_revenue = sales[0]["Revenue"]
    highest_sale = sales[0]
    
    
    for sale in sales:
        if sale["Revenue"] > highest_sale_revenue:
            highest_sale_revenue = sale["Revenue"]
            highest_sale = sale
    return highest_sale



def find_lowest_sale(sales):
    if not sales:
        return "No sales is recorded. Record sale and try again"
    
    lowest_sale_revenue = sales[0]["Revenue"]
    lowest_sale = sales[0]
    
    
    for sale in sales:
        if sale["Revenue"] < lowest_sale_revenue:
            lowest_sale_revenue = sale["Revenue"]
            lowest_sale = sale
    return lowest_sale



def rank_products_by_revenue(sales):
    product_revenue = calculate_product_revenue(sales)

    return sorted(product_revenue.items(), key = lambda item: item[1], reverse = True)


def rank_categories_by_revenue(sales):
    category_revenue = calculate_category_revenue(sales)

    return sorted(category_revenue.items(), key = lambda item: item[1], reverse = True )


def rank_regions_by_revenue(sales):
    regions_revenue = calculate_region_revenue(sales)

    return sorted(regions_revenue.items(), key = lambda item: item[1], reverse = True)


def rank_salespeople_by_revenue(sales):
    salespeople_revenue = calculate_salesperson_revenue(sales)

    return sorted(salespeople_revenue.items(), key= lambda item: item[1], reverse = True )



sales = generate_sales(1000)
print("Total transaction ",len(sales),"\n")

print("Total Revenue ", calculate_total_revenue(sales),"\n")
print("Average sale value ", calculate_average_sale(sales),"\n")
print("Highest sale\n",find_highest_sale(sales),"\n","\n")
print("Lowest sale\n", find_lowest_sale(sales),"\n","\n")

performing_product_list = rank_products_by_revenue(sales)
print("Top three performing products\n",performing_product_list[:3],"\n","\n")

performing_category_list = rank_categories_by_revenue(sales)
print("Top three performing categories\n",performing_category_list[:3],"\n","\n")

performing_salespeople_list = rank_salespeople_by_revenue(sales)
print("Top three performing salespeople\n",performing_salespeople_list[:3],"\n","\n")

performing_regions_list = rank_regions_by_revenue(sales)
print("Top three performing regions\n",performing_regions_list[:3])