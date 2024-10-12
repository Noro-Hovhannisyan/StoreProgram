import json


class Store:

    @classmethod
    def display(cls,sorted_names,data):
        for name in sorted_names:
            print(f"************{sorted_names.index(name) + 1}************")
            print(f"Product name: -> {name}")
            print(f"Count: -> {data[name]['count']}")
            print(f"Purchase Price: -> {data[name]['purchase_price']}")
            print(f"Payment Price: -> {data[name]['payment_price']}")

    def enter(self,product_name,count,purchase_price,payment_price):
        #Հաշվի մնացորդի ստուգում և վերահաշվարկ
        with open('balance.json' , 'r') as file:
            data = json.load(file)
            if "balance" in data and data["balance"]>=purchase_price*count:
                data["balance"]-=purchase_price*count
            else:
                print("We have not enough money")
        with open("balance.json", 'w') as file:
            json.dump(data,file)
        #Նոր ապրանքի ավելացում կամ հին ապրանքի վերահաշվարկ
        with open('stock.json', 'r') as file:
            data = json.load(file)
            if product_name in data:
                data[product_name]["count"] += count
                data[product_name]["purchase_price"] = purchase_price
                data[product_name]["payment_price"] = payment_price
            else:
                data[product_name] = {"count":count,"purchase_price":purchase_price,"payment_price":payment_price}
        with open('stock.json', 'w') as file:
            json.dump(data, file)
    def sell(self,product_name,count):
        #Ապրանքի վաճառք
        with open('stock.json', 'r') as file:
            data = json.load(file)
            if product_name in data:
                if data[product_name]["count"] >= count:
                    data[product_name]["count"] -= count
                    #հաշվի վերահաշվարկ
                    with open("balance.json", 'r') as balance_file:
                        balance_data = json.load(balance_file)
                        balance_data["balance"] += count*data[product_name]["payment_price"]
                        balance_data["profit"] += count*(data[product_name]["payment_price"]-data[product_name]["purchase_price"])
                    with open("balance.json", 'w') as balance_file:
                        json.dump(balance_data,balance_file)
                    #__________________
                else:
                    print("We have not enough quantity")
            else:
                print("We have not that product")
        with open('stock.json', 'w') as file:
            json.dump(data, file)

    def filter(self,filter_type='letter'):
        #Ապրքանքի ցուցադրում ըստ ․․․ ֆիլտրի
        with open('stock.json', 'r') as file:
            data = json.load(file)
            #Այբենական կարգի
            if filter_type == 'letter':
                sorted_names = sorted(data)
            #Քանակի
            elif filter_type == 'count':
                sorted_names = sorted(data,key=lambda x:data[x]['count'])
            #Գնի
            elif filter_type == 'price':
                sorted_names = sorted(data,key=lambda x:data[x]['payment_price'])
            else:
                print("We have not that filter type")
                return False
            Store.display(sorted_names, data)
    def top_up_the_balance(self,count):
        with open('balance.json', 'r') as file:
            data = json.load(file)
            if "balance" in data:
                data["balance"] += count
            else:
                data["balance"] = count
        with open('balance.json', 'w') as file:
            json.dump(data, file)

    def display_balance(self):
        with open('balance.json', 'r') as file:
            data = json.load(file)
            print(data["balance"])

    def display_profit(self):
        with open('balance.json', 'r') as file:
            data = json.load(file)
            print(data["profit"])


