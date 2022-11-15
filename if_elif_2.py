# Class work
# transport = input('Which transport will you choose: fly, train, bus: ')

# if transport == 'fly':
#     ticket_type = input('In which class you want to fly: economy, buisness: ')
#     if ticket_type == 'economy':
#         place = input('Where you want place: window, corridor: ')
#     else:
#         place = 'you have you own room'

# elif transport == 'train':
#     ticket_type = input('How you want to go: kupe, plaskart: ')
#     if ticket_type == 'kupe':
#         place = input('Choise one of the place: 12, 54, 56: ')
#     elif ticket_type == 'plaskart':
#         print('no place in plaskart, wait for next')
#         exit()
# elif transport == 'bus':
#     ticket_type = input('How you want to go: sit, stand: ')
#     if ticket_type == 'sit':
#         place = input('choise place: 5,6,8: ')
#     elif ticket_type == 'stand':
#         place = 'you can go anywhere'
# else:
#     print('there is no transport')

# print('Shut up and give your money')
# print(f' you chose {transport}, your place: {place}')


# Work myself
food = input('Which food you want: shaurma, samsa, pirojki: ')

if food == 'shaurma':
    filling = input('Which filling you want: beef, chicken: ')
elif food == 'samsa':
    filling = input('Which filling you want: beef, chicken, cheese: ')
    if filling == 'cheese':
        client_answer = input('There are no samsa with cheese, do you want to wait? yes, no: ')
        if client_answer == 'no':
            print('you ordered nothing')
            exit()
elif food == 'pirojki':
    filling = input('Which filling you want: potato, cabbage: ')
else:
    print('soryy, there is no food which you want')

piece = input('how many pieces you want?')

drink = input('Which drink you want: tea, coffee, cola, mineral water: ')

print(f'you ordered: {food},with {filling}, {piece} pices, ... and drink {drink} ')