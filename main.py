import store
from input_only import input_int
xanut = store.Store()
print("*****************************Welcome to Store Program*****************************")
print("-----------For entering a new product -> enter")
print("-----------For selling a product -> sell")
print("-----------For viewing the stock -> stock")
print("-----------For viewing balance -> balance")
print("-----------For calculating the profit -> profit")
print("-----------For top up the balance -> +{money} ex.(+5000)")
while True:
    ans = input("Enter a command: ")
    if ans == "exit":
        break
    elif ans == "enter":
        product_name = input("Enter a product name: ")
        count = input_int("Enter the count of product: ")
        purchase_price = input_int("Enter the purchase price: ")
        payment_price = input_int("Enter the payment price: ")
        xanut.enter(product_name, count, purchase_price, payment_price)
    elif ans == "sell":
        product_name = input("Enter a product name: ")
        count = input_int("Enter the count of product: ")
        xanut.sell(product_name, count)
    elif ans == "balance":
        xanut.display_balance()
    elif ans == "profit":
        xanut.display_profit()
    elif ans[0] == '+':
        try:
            if isinstance(int(ans[1::]), int) and int(ans[1::]) >= 0:
                xanut.top_up_the_balance(int(ans[1::]))
        except ValueError:
            print("Invalid input")
    elif ans == 'stock':
        ans = input("Filter by letter/count/price ?: ")
        xanut.filter(ans)
    else:
        print("Invalid input")


