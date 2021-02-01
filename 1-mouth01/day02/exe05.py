"""收银台
"""
the_total_cost=int(input("what ur budget for apple:"))
number_of_item=int(input("the price of apple is 5 usd,how much apple do u want:"))
price_of_apple= 5
exchange=the_total_cost-number_of_item*price_of_apple
print("ur exchange is"+str(exchange))
