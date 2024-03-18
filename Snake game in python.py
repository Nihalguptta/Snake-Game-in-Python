import turtle
import random
import time

delay=0.1  #time
sc=0  #score
hs=0  #high score
bodies=[]

#creating a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue") #background colour
s.setup(width=600,height=600) #size of a screen

#creating a head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.fillcolor("white") #to fill the colour in head
head.penup() #not to show the line when turtle will move
head.goto(0,0) 
head.direction = "stop"

#creating a food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.fillcolor("green")
food.penup()
food.ht() #for hiding turtle
food.goto(150,200) #send the turtle in quadrant (x,y)
food.st() #for showing a turtle

#creating a score board #sb
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score:0   |   Highest Score:0")#to print a score on the screen for the 1st time

#creating function for moving in all directions
def moveUp():                   #whenever we write direction 1st letter should be capital Up
    if head.direction!="down":
        head.direction="up"
def moveDown():
    if head.direction!="up":
        head.direction="down"
def moveLeft():
    if head.direction!="right":
        head.direction="left"
def moveRight():
    if head.direction!="left":
        head.direction="right"
def moveStop():
    head.direction="stop"

def move():   #this 'def' define that if turtle will move # how much to move
    if head.direction=="up":
        y=head.ycor()           #cor means co-ordinate
        head.sety(y+20)
    if head.direction=="left":
        x=head.xcor()         
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()           
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()           
        head.setx(x+20)

#event handling
s.listen()  #button selection for running turtle
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down") # the key which we set here will run the turtle.
s.onkey(moveLeft,"Left")
s.onkey(moveRight,"Right")
s.onkey(moveStop,"space") #we can set any key to stop our function #here we have used space

#mainloop
while True:    # while true will let the turtle keep on running infinite 
    s.update() #to update the screen
    #check collision with border
    if head.xcor()>290:   #this is for movement of turtle
        head.setx(-290)   #when the turtle passes the x axis then it will come from -x

    if head.xcor()<-290:  #this is when turtle pass from -x to +x 
        head.setx(290)    #the moment it cross -x it comes from +x

    if head.ycor()>290:   #this is when turtle pass +y and comes form -y
        head.sety(-290)   # moves from +y to -y.

    if head.ycor()<-290:  #this is when turtle pass -y and comes from +y
        head.sety(290)    #moves form -y to +y.
 
    #check collision with food   #remove food and keep it in another place when the snake reach the food
    if head.distance(food)<20:  #this is for movement of food. 
        x= random.randint(-290,290) # this is the range for food.
        y= random.randint(-290,290) # by this we have make a field were we can see the food
        food.goto(x,y) #goto means going to #snake is going toward food

        #increase the body of snake
        body= turtle.Turtle() #moment when the snake reach food the food gets remove and
        body.speed(0)           #snake body get added with new body
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body) #append the new body in list #so that we can show the growth of snake

        #now when the snake have food, we also have to show the score increasing.

        #increase the score
        sc = sc+100  #whenever a new body appends increase the score by 100 
        #increase the speed
        delay = delay-0.001 #for increasing speed we are using "-time delay"
                            #this will let the speed increase as the delay in time get increases.

        #update highest score
        if sc>hs:
            hs = sc #update high score
        sb.clear()   #to clear old score
        sb.write("Score:{}  |  Higest score:{}".format(sc,hs)) #this will update score
        
        #move snake bodies
    for i in range(len(bodies)-1,0,-1):#len of body is 5 #here we will use for loop
        x = bodies[i-1].xcor() #by this it will start decreasing #
        y = bodies[i-1].ycor()
        bodies[i].goto(x,y) #this will send 4th element in 3rd #and by this bodies will move on continue 
    if len(bodies)>0: 
        x = head.xcor() #to know the quadrant
        y = head.ycor()
        bodies[0].goto(x,y) #if len of body more that 0 ,then send it to quadrant 
    move()

    #check collision with snake body
    for body in bodies:   #if the head touch the body "element" then game over
          if body.distance(head)<20: #this is to check weather element are touching body or not
              time.sleep(1)   #time sleep means game over.
              head.goto(0,0)
              head.direction="stop" #this is for #if body get touch by head
              #hide bodies
              for body in bodies:
                  body.ht()  #we also have to hide body #when the loop will run the bodies one by one gets hide 
              bodies.clear() 
              sc = 0
              delay = 0.1
              sb.clear() #using clear to remove old score  
              sb.write("Score:{}  |  Higest Score:{}".format(sc,hs))#for updating new score 
    time.sleep(delay)
s.mainloop() #mainloop is used so that when the game is over screen doesn't disappears

                                                       





    



































