#to develop a game of hangman using python
import turtle
from random import randint
k=turtle.Turtle()
s=turtle.Screen()
def one():
	k.penup()
	k.setposition(-40,-80)
	k.pendown()
	k.left(90)
	k.forward(120)
	k.right(90)
	k.forward(50)
	

def two():
	
	k.right(90)
	k.forward(20)
	k.penup()
	k.forward(20)
	k.pendown()
	k.left(90)
	k.circle(10)
	

def three():
	k.right(90)
	k.forward(40)
	k.backward(20)

def four():
	k.left(45)
	k.forward(20)
	k.backward(20)
	k.right(90)

def five():
	k.forward(20)
	k.backward(20)
	k.left(45)

def six():
	k.forward(20)
	k.left(45)
	k.forward(20)
	k.backward(20)

def seven():
	k.right(90)
	k.forward(20)



def find(aliase):
	return any('*' in word for word in aliase)







def start():
	options={
	1: one,
	2: two,
	3: three,
	4: four,
	5: five,
	6: six,
	7: seven
	}
	words=['hello','asking','vulture','assignment','accomplish','multiple','variance','academics']
	global hang

	#assignning a random word from the list to the variable hang
	hang = words[randint(0,7)]
	lent = len(hang)

	#assiging equal no of letters to the variable aliase
	aliase='*'*lent
	print aliase
	print aliase[1]

	print "guess the word"
	count = 0

	while(count<7):
		mnt=0
	   	finish=2

		met = raw_input("enter the letter:")
		let = str(met)
		for i in range(0,lent):
			if(hang[i]==let):
				list1=list(aliase)
				list1[i]=let
				aliase= ''.join(list1)
				mnt=1


		if(mnt==0):
			count=count+1
		else:
			if(find(aliase)):
				finish=0
			else:
				finish=1
	


		if(finish==1):
			print "you have found the word"+aliase
			return 1
		elif(mnt==0):
			print aliase
			options[count]()
		else:
			print aliase
	return 0
		

if(start()):
	print "he is safe"
	s.exitonclick()
else:
	print "he is dead"
	print "the word is "+hang
	s.exitonclick()





