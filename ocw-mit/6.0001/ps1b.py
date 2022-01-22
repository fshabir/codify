

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of salary to save, as a decimal: "))
total_cost = float(input("Total the cost of dream house: "))
annual_raise = float(input("Enter the semi-annual raise, as decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

down_payment_amount = total_cost * portion_down_payment
months = 0

while current_savings < down_payment_amount:
    monthly_salary = annual_salary / 12
    current_savings = current_savings + (current_savings * (r / 12)) + (monthly_salary * portion_saved)
    months += 1
    if months % 6 == 0:
        annual_salary += (annual_salary * annual_raise)

print("Number of months: ", months)