import store
from input_only import input_int
import const
import message
import manager
manager = manager.JsonManager()
xanut = store.Store(const.stock,const.balance, manager)
print(message.welcome)
while True:
    ans = input(message.command)
    if ans == "exit":
        break
    elif ans == "enter":
        product_name = input(message.product)
        count = input_int(message.count)
        purchase_price = input_int(message.purchase)
        payment_price = input_int(message.payment)

        xanut.enter(product_name, count, purchase_price, payment_price)
    elif ans == "sell":
        product_name = input(message.product)
        count = input_int(message.count)
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
            print(message.invalid)
    elif ans == 'stock':
        ans = input(message.filter)
        xanut.filter(ans)
    else:
        print(message.invalid)


