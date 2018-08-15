#Chapter 3
#lists, strings, embedding values in strings

#dict/map
bad_skill = {'Sauce' : 'nothing' ,
                'Nathan' : 'board games' , 
                'Alex' : 'winking' , 
                'Gabino' : 'hiding his love of Betos' ,
                'Robin' : 'ninjitsu' ,
                'Dwayne' : 'all the things' ,
                'Palfreyman' : 'bowling one-handed'}

#print("What is Gabino\'s worst skill?")
#print(bad_skill['Gabino'])

print("Everyone is terrible at something.  Who would you like to see what they are terrible at?")
print('''Please enter one of the following: Sauce, Nathan, Alex, Gabino, Robin, Dwayne, or Palfreyman?''')

def skills():
    person = input()
    
    if person == 'Sauce':
        print("Is bad at")
        print(bad_skill['Sauce'])
    elif person == 'Nathan':
        print("Is bad at")
        print(bad_skill['Nathan'])
    elif person == 'Alex':
        print("Is bad at")
        print(bad_skill['Alex'])
    elif person == 'Gabino':
        print("Is bad at")
        print(bad_skill['Gabino'])
    elif person == 'Robin':
        print("Is bad at")
        print(bad_skill['Robin'])
    elif person == 'Dwayne':
        print("Is bad at")
        print(bad_skill['Dwayne'])
    elif person == 'Palfreyman':
        print("Is bad at")
        print(bad_skill['Palfreyman'])
    else : 
        print('''Bad Input''')
        print("Everyone is terrible at something.  Who would you like to see what they are terrible at?")
        print('''Please enter one of the following: Sauce, Nathan, Alex, Gabino, Robin, Dwayne, or Palfreyman?''')
        skills()
skills()