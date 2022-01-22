

annual_salary = float(input("Enter your annual salary: "))


def saving_duration(portion_saved, annual_salary):
    total_cost = 1000000
    semi_annual_raise = 0.07
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04

    down_payment_amount = total_cost * portion_down_payment
    months = 0
    difference_from_actual_savings = 100

    while (current_savings + difference_from_actual_savings) < down_payment_amount:
        monthly_salary = annual_salary / 12
        current_savings = current_savings + (current_savings * (r / 12)) + (monthly_salary * portion_saved)
        months += 1
        if months % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
    return months


min_rate = 0.01
max_rate = 1
months = None
steps = 0
while steps < 100:
    saving_rate = (min_rate + max_rate) / 2
    steps += 1
    months = saving_duration(saving_rate, annual_salary)
    if months == 36:
        break
    elif months < 36:
        max_rate = saving_rate
    else:
        min_rate = saving_rate

if months != 36:
    print("It is not possible to pay the down payment in three years")
else:
    print("Best savings rate: ", saving_rate)
    print("Steps in bisection search: ", steps)