import message


class Store:
    def __init__(self, stock, balance, manager):
        self.stock = stock
        self.balance = balance
        self.manager = manager

    @classmethod
    def display(cls, sorted_names, data):
        if not data:
            print("The stock is empty")
        for name in sorted_names:
            print(f"************{sorted_names.index(name) + 1}************")
            print(f"Product name: -> {name}")
            print(f"Count: -> {data[name]['count']}")
            print(f"Purchase Price: -> {data[name]['purchase_price']}")
            print(f"Payment Price: -> {data[name]['payment_price']}")

    def enter(self, product_name, count, purchase_price, payment_price):
        # Հաշվի մնացորդի ստուգում և վերահաշվարկ
        data = self.manager.load(self.balance)
        if "balance" in data and data["balance"] >= purchase_price * count:
            data["balance"] -= purchase_price * count
        else:
            print(message.error_money)
        self.manager.dump(data, self.balance)
        # Նոր ապրանքի ավելացում կամ հին ապրանքի վերահաշվարկ
        data = self.manager.load(self.stock)
        if product_name in data:
            data[product_name]["count"] += count
            data[product_name]["purchase_price"] = purchase_price
            data[product_name]["payment_price"] = payment_price
        else:
            data[product_name] = {"count": count, "purchase_price": purchase_price, "payment_price": payment_price}
        self.manager.dump(data, self.stock)

    def sell(self, product_name, count):
        # Ապրանքի վաճառք
        data = self.manager.load(self.stock)
        if product_name in data:
            if data[product_name]["count"] >= count:
                data[product_name]["count"] -= count
                # հաշվի վերահաշվարկ
                balance_data = self.manager.load(self.balance)
                balance_data["balance"] += count * data[product_name]["payment_price"]
                balance_data["profit"] += count * (
                        data[product_name]["payment_price"] - data[product_name]["purchase_price"])
                self.manager.dump(balance_data, self.balance)
                # __________________
            else:
                print(message.error_count)
        else:
            print(message.error_product)
        self.manager.dump(data, self.stock)

    def filter(self, filter_type='letter'):
        # Ապրքանքի ցուցադրում ըստ ․․․ ֆիլտրի
        data = self.manager.load(self.stock)
        # Այբենական կարգի
        if filter_type == 'letter':
            sorted_names = sorted(data)
        # Քանակի
        elif filter_type == 'count':
            sorted_names = sorted(data, key=lambda x: data[x]['count'])
        # Գնի
        elif filter_type == 'price':
            sorted_names = sorted(data, key=lambda x: data[x]['payment_price'])
        else:
            print(message.error_filter)
            return False
        Store.display(sorted_names, data)

    def top_up_the_balance(self, count):
        data = self.manager.load(self.balance)
        if "balance" in data:
            data["balance"] += count
        else:
            data["balance"] = count
        self.manager.dump(data, self.balance)

    def display_balance(self):
        data = self.manager.load(self.balance)
        print(data["balance"])

    def display_profit(self):
        data = self.manager.load(self.balance)
        print(data["profit"])
