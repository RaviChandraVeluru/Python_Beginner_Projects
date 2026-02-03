score_board = {}

print('''
[1] Add/Update.
[2] View Leaderboard
[3] Exit''')

while True:
    option = input('select an option: ')
    if option == '1':
        player_name = input('enter the player name: ')
        try:
            if player_name in score_board:
                score = int(input('Enter updated score: '))
                score_board[player_name] +=score
            else:
                score = int(input('Enter score: '))
                score_board[player_name]=score
        except TypeError:
            print('Score must be a number.')
        except ValueError:
            print('Score must be a number.')

    elif option == '2':
        leader_board = sorted(score_board.items(), key= lambda item: item[1],reverse=True)
        start = int(input('Enter the start rank: '))-1
        stop = int(input('Enter the Stop rank: '))
        stop = min(stop, len(leader_board))
        print("Rank", end=' ')
        print('Name', end=' ')
        print('Score', )
        for i,(name,rank) in enumerate(leader_board[start:stop], start=start + 1):
            print(f"{i}\t {name}\t {rank}")
    elif option =='3':
        print('Thank You!.')
        break
    else:
        print('Please Select Correct Option. ')
        print('''
[1] Add/Update.
[2] View Leaderboard
[3] Exit''')



