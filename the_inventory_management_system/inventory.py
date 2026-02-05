from adding_stock import add_stock
from update_stock import update_Stock,update_price,update_price_and_stock
from sell_stock import  sell_stock

inventory = [{'product':'apple','price':10, 'stock':4}]

print("The Inventory Management System.")
print()
print('''Options: 
1. Add Stock
2. Update Stock
3. Sell Stock
4. Summary Report
5. Exit
''', end='\n')

while True:
    option = input('Enter your Option : ')
    print()
    if option.isdigit():
        if option == '1':
            product = input('Enter the Product Name: ')
            price = input(f'Enter Price of the {product}: ')
            stock = input(f'Enter the Stock or {product}: ')
            add_product = add_stock(inventory,product,price,stock)
            print(add_product, end='\n')



        elif option == '2':
            print('''What do you wish to update:
                            1. Stock
                            2. price
                            3. Both Stock and Price
                            ''', end='\n')
            update = input("Enter your option: ")
            print()
            if update == '1':
                product = input('Enter the Product Name: ')
                for i in inventory:
                    if product in i.values():
                        up_stock = input('Enter updated stock: ')
                        if up_stock.isdigit():
                            up_st = update_Stock(inventory, product, int(up_stock))
                            print(up_st)
                            break
                        else:
                            print('Stock must be a number. ', end='\n')
                else:
                    print('Product does not exist in inventory', end='\n')
            elif update == '2':
                product = input('Enter the Product Name: ')
                for i in inventory:
                    if product in i.values():
                        up_price = input('Enter the updated price: ')
                        up_p = update_price(inventory, product, up_price)
                        print(up_p, end='\n')
                        break
                else:
                    print('Product does not exist in inventory', end='\n')
            elif update == '3':
                product = input('Enter the Product Name: ')
                for i in inventory:
                    if product in i.values():
                        up_price = input('Enter the updated price: ')
                        up_stock = input('Enter updated stock: ')
                        up_all = update_price_and_stock(inventory, product, up_price, up_stock)
                        print(up_all, end='\n')
                        break
                else:
                    print('Product does not exist in inventory', end='\n')

            else:
                print('Must Select one option')
                print('Try Again!.', end='\n')

        elif option == '3':
            product = input('Enter the Product Name: ')
            sell = sell_stock(inventory,product)
            print(sell, end='\n')

        elif option == '4':
            print('Summary Report.','\n')
            print(f'{"No.":<4}', end='\t')
            print(f"{'Product':<15}", end='\t')
            print(f"{'Price':>8}", end='\t')
            print(f"{'Stock':>8}", end='\n')
            for i, data in enumerate(inventory):
                print(f'{i+1:<4}',end='\t')
                print(f"{data['product']:<15}",end='\t')
                print(f"{data['price']:>8}",end='\t')
                print(f"{data['stock']:>8}",end='\n')
            print()
        elif option =='5':
            print('Exiting Inventory. ', end='\n')
            break
        else:
            print('Please Select Correct Option.', end='\n')
    else:
        print('Please Enter an Option.', end='\n')
        print('''Options: 
        1. Add Stock
        2. Update Stock
        3. Sell Stock
        4. Summary Report
        : ''')