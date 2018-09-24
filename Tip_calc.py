total_bill_amount = float(input("Total Bill amount"))
level_of_service = input("How was the level of service? good,fair,bad? ")
good = "good"
fair = "fair"
bad = "bad"
good_tip = .2
fair_tip = .15
bad_tip = .10

tip = 0.0
print(level_of_service)

if level_of_service == good:
    tip = total_bill_amount * good_tip
    print(tip)
elif level_of_service == fair:
    tip = total_bill_amount * fair_tip
    print(tip)
elif level_of_service == bad:
    tip = total_bill_amount * bad_tip
    print(tip)
print(total_bill_amount + tip)
