student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# 1. Calculate average grade for each student
student_averages = {}
for name, grades in student_grades.items():
    student_averages[name] = sum(grades) / len(grades)

# 2. Assign letter grade based on average
student_letter_grades = {}
for name, avg in student_averages.items():
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    student_letter_grades[name] = grade

# 3. Calculate class average
class_average = sum(student_averages.values()) / len(student_averages)
print(f"Class Average: {class_average:.2f}\n")

# 4. Print individual summary report
print("Student Summary:")
for name in student_grades:
    avg = student_averages[name]
    letter = student_letter_grades[name]
    print(f"{name}: Average = {avg:.2f}, Letter Grade = {letter}")
# Exercise 2: Advanced Data Manipulation and Analysis

# Python
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Task 1: Total Sales Calculation per product category
total_sales = {}
for transaction in sales_data:
    product = transaction["product"]
    revenue = transaction["price"] * transaction["quantity"]
    total_sales[product] = total_sales.get(product, 0) + revenue

print("Total Sales per Product:", total_sales)

# Task 2: Customer Spending Profile
customer_spending = {}
for transaction in sales_data:
    cid = transaction["customer_id"]
    revenue = transaction["price"] * transaction["quantity"]
    customer_spending[cid] = customer_spending.get(cid, 0) + revenue

print("Customer Spending Profile:", customer_spending)

# Task 3: Sales Data Enhancement (Add total_price)
for transaction in sales_data:
    transaction["total_price"] = transaction["price"] * transaction["quantity"]

# Task 4: High-Value Transactions (> $500 sorted descending)
high_value_transactions = [t for t in sales_data if t["total_price"] > 500]
high_value_transactions.sort(key=lambda x: x["total_price"], reverse=True)
print("\nHigh Value Transactions:", high_value_transactions)

# Task 5: Customer Loyalty Identification (> 1 purchase)
purchase_counts = {}
for transaction in sales_data:
    cid = transaction["customer_id"]
    purchase_counts[cid] = purchase_counts.get(cid, 0) + 1

loyal_customers = [cid for cid, count in purchase_counts.items() if count > 1]
print("Loyal Customers:", loyal_customers)

# --- Bonus: Insights and Analysis ---

# 1. Average transaction value per product category
avg_transaction_value = {}
for product in total_sales:
    matching_txs = [t["total_price"] for t in sales_data if t["product"] == product]
    avg_transaction_value[product] = sum(matching_txs) / len(matching_txs)

print("\nAverage Transaction Value:", avg_transaction_value)

# 2. Most popular product based on total quantity sold
quantity_per_product = {}
for t in sales_data:
    product = t["product"]
    quantity_per_product[product] = quantity_per_product.get(product, 0) + t["quantity"]

most_popular = max(quantity_per_product, key=quantity_per_product.get)
print("Most Popular Product (by quantity):", most_popular)

# 3. Marketing Insights:
# - Laptops generate high average transaction values, indicating strong revenue potential per sale. Marketing could target professionals with cross-selling incentives (e.g., laptop bags or accessories).
# - Headphones lead in quantity sold; promoting bundles (e.g., buying a Smartphone with discounted Headphones) can boost overall basket size.