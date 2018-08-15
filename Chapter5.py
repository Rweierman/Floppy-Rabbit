#Chapter5 If and Else
print('''Do you like boxes without corners? [yes/no]''')
def box():
    answer=input()
    if answer == 'yes':
        import turtle
        t=turtle.Pen()
    
        #draw box without corners
        t.forward(50)
        t.up()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.down()
        t.forward(50)
        t.up()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.down()
        t.forward(50)
        t.up()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.down()
        t.forward(50)
    
    elif answer == 'no':
        import turtle
        t = turtle.Pen()
        
        #draw box with corners
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        
    else :
        print('''Please answer yes or no''')
        box()
box()
