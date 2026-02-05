# inventory = [{'product':'apple','price':10, 'stock':4}]



def add_stock(inventory,product,price,stock):
    for i in inventory:
        if product not in i.values():
                inventory.append( {'product':product,
                                  'price':price,
                                  'stock':int(stock)})
                return 'Product added to inventory'
        else:
            return 'Product already exist in inventory'





# if __name__=='__main__':
#     product = input("Product: ")
#     price = input('Price: ')
#     stock = input('Stock: ')
#     print(add_stock(inventory,product,price,stock))
#     print(inventory)