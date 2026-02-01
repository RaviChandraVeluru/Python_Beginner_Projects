
print('''
Select an Option:
1. Deposit
2. Withdraw
3. Balance
4. Transaction History
5. Exit
''')

history = []
balance = 1000

while True:
    option = input('Enter your option: ')

    #deposit amount
    try:
        if option == '1':
            deposit_amount = float(input('Enter the amount you want to deposit: '))
            if deposit_amount <0:
                print('amount must be Greater than Zero')
                print()
            else:
                balance = balance + deposit_amount
                history.append(f"Deposit : {deposit_amount}")
                history.append(f"Balance : {balance}")
                print(deposit_amount," Added to your Balance")
                print()


        # Withdraw amount
        elif option == '2':
            withdraw_amount = float(input('Enter amount you want to withdraw: '))
            if withdraw_amount>0:
                if withdraw_amount <= balance:
                    balance = balance - withdraw_amount
                    history.append(f"withdrew : {withdraw_amount}")
                    history.append(f"Balance : {balance}")
                    print(withdraw_amount," amount is withdrew.")
                    print()
                elif withdraw_amount > balance:
                    print(f"withdraw amount more than balance.")
                    print()
            else:
                print('amount must be Greater than Zero')
                print()

        # Balance amount
        elif option =='3':
            print('Current Balance: ',balance)
            print()

        # Transaction History:
        elif option == '4':
            print('Transaction History: ')
            for i,j in enumerate(history):
                print(i+1,".",j)
            print()

        # Exiting..
        elif option == '5':
            print('Thank You. \nCome Again!. ')
            print()
            break

        # if Option does not Exist
        else:
            print('''Choose an option from below:
    1. Deposit
    2. Withdraw
    3. Balance
    4. Transaction History
    5. Exit''')
            print()
    except ValueError:
        print('Please enter Valid input')
    except TypeError:
        print('Please enter Valid input')
