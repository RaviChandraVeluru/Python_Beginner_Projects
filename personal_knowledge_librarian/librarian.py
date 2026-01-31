
knowledge_base = {}
print('The Personal Knowledge Librarian')
print()
print('''Select an option:
1 or add-cat
2 or add-fact
3 or search-cat
4 or summary
5 or exit
''')
while True:
    question = input('Enter your option: ')
    # Creating the category.
    if question in ['1', 'add-cat']:
        add_cat = input("Enter the Category name you want to create: ")
        if add_cat not in knowledge_base:
            knowledge_base[add_cat] = []
            print(f'\"{add_cat}\" Category is Created...')
            print()
        else:
            print(f'\"{add_cat}\" Category Already exit.')
            print()

    # adding facts to the category
    elif question in ['2', 'add-fact']:

        cats_kb = [k for k,v in knowledge_base.items()]
        print(cats_kb)
        for i, cat in enumerate(knowledge_base):
            print(i+1," : ", cat)
        get_cat = int(input('Select the Category: '))
        cat_key = cats_kb[get_cat-1]
        if cat_key in knowledge_base:
            add_fact = input(f'Enter the fact for {cat_key}: ')
            knowledge_base[cat_key].append(add_fact)
            print(f"fact \"{add_fact}\" is added to the category {cat_key}")
            print()
        else:
            print('Category does not exist.\nPlease Create Category before adding facts!.')
            print()

    # searching for the categories and displaying facts
    elif question in ['3','search-cat']:
        for cat in knowledge_base:
            print(cat)
        search_cat = input('Which category are you looking for: ')
        if search_cat in knowledge_base:
            if not knowledge_base[search_cat]:
                print("This category is currently a blank slate!")
            else:
                print("\n".join(fact for fact in knowledge_base[search_cat]))
                print()
        else:
            print("Please enter right category: ")
            print()

    elif question in ['4','summary']:
        if not knowledge_base:
            print('Currently there are no Categories to display.')
            print()
        else:
            print('Summary: ')
            for keys,values in knowledge_base.items():
                print(f'{keys}: {len(values)} Facts ')
            print()

    # Exiting the knowledge base
    elif question in ['5','exit']:
        print('Exiting...')
        break

    else:
        print("Please Select the Correct Option...")
        print('''Select an option:
        1 or add-cat
        2 or add-fact
        3 or search-cat
        4 or summary
        5 or exit

        ''')
