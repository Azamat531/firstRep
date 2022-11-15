# Problem0
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6,7}
# dates_of_birth.remove(7)
# print(dates_of_birth)


# Problem1
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_1.intersection(farm_2))


# Problem2 
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_2.difference(farm_1))


# Problem3
# teams = {'arsenal', 'manchester city','liverpool','chelsea','manchester united'}
# teams.add('tottenham')
# teams.pop()
# print(teams)


# Dictionary

# Problem000
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak'] = 130
# menu['lagman'] = 135
# menu.pop('borsh')
# print(menu)


# Problem10
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu.setdefault('drinks',['Coca-Cola','Sprite','Fanta'])
# print(menu)


# Problem020
# set1 = {'intersection','difference','add','pop','update','copy','clear','remove'}
# dict1 = {'update','clear','pop','remove','values','keys','items','get'}
# print(set1.intersection(dict1))


# Problem31
# dict1={}
# for i in range(3):
#     name = input('input your name: ')
#     password = input('input password: ')

#     dict1.setdefault(name,password)
    
# print(dict1)


# Problem27
# dict1 = {
#     'azamat': 'developer',
#     'bakai': 'bus rider',
#     'aslan': 'doctor',
#     'bayel': 'haircutter',
#     'atai': 'teacher'
# }
# for name, profession in dict1.items():
#     print(f'Hello {name} great profession {profession}')


# Problem22
# set1 = set()
# for i in range(10):
#     num = int(input('input number: '))
#     set1.add(num)
# set1 = tuple(set1)
# print(type(set1))

# Problem11
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 
# 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 
# 'Uruguay', 'Venezuela']

# south_american_countries = set(south_american_countries)
# south_american_countries = list(south_american_countries)
# print(south_american_countries)
# print(type(south_american_countries))


# Problem101
# suitcase = []
# for i in range(5):
#     object = input('input: ')
#     suitcase.append(object)
# print(suitcase)
# suitcase.pop(len(suitcase)-1)
# print(suitcase)


# Problem001
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_1.intersection(farm_2))


# Problem100
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_2.difference(farm_1))