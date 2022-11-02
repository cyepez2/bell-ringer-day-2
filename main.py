from dynamic_functions import check_3digits, all_positives, sum_less, count_even
coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]


for coffee, price in coffee_prices:
 print(f" the cost of one {coffee} is {price}")
#create a function to get the highest priced coffee and its name
def highroller(coffee_prices):
  highest_price = 0
  pricest_coffee = ''
  for coffee, price in coffee_prices:
    if price > highest_price:
      highest_price = price 
      most_expensive = coffee
    else:
      pass
  return(most_expensive,highest_price)    
print(highroller(coffee_prices))
 

highroller(coffee_prices)

data = check_3digits([191,999,610,191,11,531,511,566,911,711,696,420,117,118])
print(data)
data2 = all_positives([1,33,-1,55])
print(data2)
test = sum_less([1,10,25,50,999])
print(test)
test4 = count_even([55, 99, 600, 78, 120, 500, 20, 78, 333])
print(test4)