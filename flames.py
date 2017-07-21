def friend():
	print "friend"
def love():
	print "love"
def affection():
	print "affection"
def marriage():
	print "marriage"
def enemy():
	print "enemy"
def sister():
	print "sister"

def start():	
	#assigning names to variabes
	boy=raw_input("enter boys name ")
	boys=list(boy)
	girl=raw_input("enter girls name ")
	girls=list(girl)		
	options={
	0: friend,
	1: love,
	2: affection,
	3: marriage,
	4: enemy,
	5: sister
	}
		#clearing the letters that match with the other name
	for i in range(len(boy)):
		for j in  range(len(girl)):
			if(boy[i]==girl[j]):
				boys[i]='*'
				boy=''.join(boys)
				girls[j]='*'
				girl=''.join(girls)

	# counting the no of letters remaining in both names
	count=0
	for i in range(len(boy)):
		if(boy[i]!='*'):
			count=count+1
	for i in range(len(girl)):
		if(girl[i]!='*'):
			count=count+1
	# finding the letter in flames that matches to the count
	pgm="flames"
	pgmlist=list(pgm)
	strcnt=0
	mnt=0
	while(strcnt<=4):
		for i in range(len(pgm)):
			if(pgm[i]!='*'):
				mnt=mnt+1
			if(mnt==count):
				mnt =0
				pgmlist[i]='*'
				pgm=''.join(pgmlist)
				strcnt=strcnt+1
	mk=0
	for i in range(len(pgm)):
		if(pgm[i]!='*'):
			mk=i
	options[mk]()
start()




