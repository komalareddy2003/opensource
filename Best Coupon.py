x = int(input())
amount_with_10_percent_discount = x * 0.90
amount_with_flat_discount = max(0, x - 100)
amount_to_pay = min(amount_with_10_percent_discount, amount_with_flat_discount)
print(int(amount_to_pay))
