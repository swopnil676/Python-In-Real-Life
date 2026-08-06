# money calculator
    # method 1
def calculate_revenue(sales):
    return sum(sales)

def highest_sale(sales):
    return max(sales)

monthly_sales = [1200, 950, 2100, 1800]

print(calculate_revenue(monthly_sales))
print(highest_sale(monthly_sales))



    # method 2
def calculate_revenue(sales):
    return sum(sales)

def highest_sale(sales):
    return max(sales)

reports = {
    "revenue": calculate_revenue,
    "highest": highest_sale
}

monthly_sales = [1200, 950, 2100, 1800]

print(reports["revenue"](monthly_sales))
print(reports["highest"](monthly_sales))
