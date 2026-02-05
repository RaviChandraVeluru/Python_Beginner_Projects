# inventory = [{'product':'apple','price':10, 'stock':4}]

def sell_stock(inventory, product):
    for i in inventory:
        if product in i.values():
            selling_stock = input('Enter the stock you want to sell: ')
            if int(selling_stock)>0:
                if i['stock'] >= int(selling_stock):
                    i['stock'] -=int(selling_stock)
                    return f"Product: {i['product']} remaining Stock is '{i['stock']}' "
                else:
                    return 'Not enough Stock to sell'
        else:
            return 'Selling stock must be a integer'

# if __name__=="__main__":
     # print(inventory)
    # product = input('Product: ')
    # print(sell_stock(inventory,product))
    # print(inventory)