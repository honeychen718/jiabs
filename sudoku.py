def checkfinish(matrixlist):
	for i in range(9):
		for j in range(9):
			if len(matrixlist[i][j])!=1:
				return 0
	return 1

def jiadel(l,n):
	while n in l:
		l.remove(n)
		
def printmatrix():
	for i in range(9):
		print(matrixlist[i])

'''/////////////////////////////////////////////////'''
matrixlist=[[[] for i in range(9)]for j in range(9)]
matrixx=[[]for i in range(9)]
matrixy=[[]for i in range(9)]
matrixz=[[]for i in range(9)]
with open('source.txt') as file_obj:
	i=0
	for line in file_obj:
		tokens=line.split()
		for j in range(9):
			if tokens[j]!='0':
				matrixlist[i][j]=[int(tokens[j])]
		i=i+1


for i in range(9):
	for j in range(9):
		if len(matrixlist[i][j])==1:
			matrixx[i].append(matrixlist[i][j][0])
			matrixy[j].append(matrixlist[i][j][0])
			matrixz[int(i/3)*3+int(j/3)].append(matrixlist[i][j][0])

mark3=1
while checkfinish(matrixlist)==0 and mark3==1:
	mark3=0
	tdmatrixx=[[]for i in range(9)]
	tdmatrixy=[[]for i in range(9)]
	tdmatrixz=[[]for i in range(9)]
	for i in range(9):
		for j in range(9):
			if len(matrixlist[i][j])==1:
				continue
			for k in range(1,10):
				if k not in matrixx[i]:
					if k not in matrixy[j]:
						if k not in matrixz[int(i/3)*3+int(j/3)]:
							matrixlist[i][j].append(k)

	for i in range(9):
		for j in range(9):
			if len(matrixlist[i][j])!=1:
				tdmatrixx[i]=tdmatrixx[i]+matrixlist[i][j]
				tdmatrixy[j]=tdmatrixy[j]+matrixlist[i][j]
				tdmatrixz[int(i/3)*3+int(j/3)]=tdmatrixz[int(i/3)*3+int(j/3)]+matrixlist[i][j]

	mark2=1
	while mark2==1:
		mark2=0
		for i in range(9):
			for j in range(9):
				if len(matrixlist[i][j])==1:#for single number
					if matrixlist[i][j][0] not in matrixx[i]:#for number single but not set
						matrixx[i].append(matrixlist[i][j][0])
						matrixy[j].append(matrixlist[i][j][0])
						matrixz[int(i/3)*3+int(j/3)].append(matrixlist[i][j][0])
						jiadel(tdmatrixx[i],matrixlist[i][j][0])
						jiadel(tdmatrixy[j],matrixlist[i][j][0])
						jiadel(tdmatrixz[int(i/3)*3+int(j/3)],matrixlist[i][j][0])
						mark2=1
						mark3=1
					


	for i in range(9):
		for j in range(9):
			if len(matrixlist[i][j])!=1:
				mark=0
				for number in matrixlist[i][j]:
					if tdmatrixx[i].count(number)==1 or tdmatrixy[j].count(number)==1 or tdmatrixz[int(i/3)*3+int(j/3)].count(number)==1:
						mark=1
						matrixx[i].append(number)
						matrixy[j].append(number)
						matrixz[int(i/3)*3+int(j/3)].append(number)
						jiadel(tdmatrixx[i],number)
						jiadel(tdmatrixy[j],number)
						jiadel(tdmatrixz[int(i/3)*3+int(j/3)],number)
						mark3=1
						break
				if mark==1:#if hit
					matrixlist[i][j]=[number]
				else:
					matrixlist[i][j]=[]
			
			
	
if checkfinish(matrixlist)==0:
	print('cant solve\n')
	printmatrix()
else:
	print('finished!\n')
	printmatrix
	
