from turtle import Turtle, Screen
import random


is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title='make your bet',prompt='which turtle win the race enter a color :')
colors=['red','green','orange','yellow','blue','purple']
all_turtles=[]
y=-100
for i in range(len(colors)) :
    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(-230,y)
    new_turtle.color(colors[i])
    y+=40
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on =True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print(f"you've won the race {winning_color} turtle winning")
            else:
                print(f"you've lost the race {winning_color} turtle winning")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
