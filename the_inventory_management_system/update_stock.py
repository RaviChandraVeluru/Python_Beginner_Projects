# inventory = [{'product':'apple','price':10, 'stock':4}]

def update_Stock(inventory,product,stock):
    for i in inventory:
        if product in i.values():
            if int(stock) > 0:
                i.update({'stock':int(stock)})
                return 'Stock is updated'
            elif not stock.isdigit():
                return 'Stock must be a Number'
            else:
                return  'Stock must be Greater than zero'

def update_price(inventory,product,price):
    for i in inventory:
        if product in i.values():
            i.update({'price': price})
            return 'Price is Updated'

def update_price_and_stock(inventory,product,stock,price):
    for i in inventory:
        if product in i.values():
            update_Stock(inventory,product,stock)
            update_Stock(inventory,product,price)






# if __name__=='__main__':
#     product = input("Product: ")
#     price = input('Price: ')
#     stock = input('Stock: ')
#     print('base Inventory')
#     print(inventory)
#     print()
#     print('Inventory Updating Stock')
#     update_Stock(inventory,product,stock)
#     print(inventory)
#     print('Stock Updated Inventory')
#     print()
#     print('Inventory Updating Price')
#     update_price(inventory,product,price)
#     print(inventory)
#     print('Price Updated Inventory')
#     print()
#     price = input('Price: ')
#     stock = input('Stock: ')
#     print('Inventory Updating Price and stock')
#     update_price_and_stock(inventory,product,price,stock)
#     print(inventory)
#     print('Price and stock Updated Inventory')