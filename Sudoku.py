import random
import pygame

#Decide Level of Diffculty (Based on how many numbers are added befor each game starts)
#filled = random. 
# Assure Game Rules are Met
def rules_met(x,y,n,newgrid):
	grid = newgrid
	#print('Hello')
	#Check if the Column are all different Numbers
	for i in range(0,9):
		#print(grid[i][y])
		if grid[i][y] == n:
			#print('Column Error')
			return False 

	#check if the Row are all  different Numbers
	for j in range(0,9):
		#print(grid[x][j])
		if grid[x][j] == n:
			#print('Row Error')
			return False

	#Check if the Current Quadrant are all different Numbers
	boxx = x//3*3
	boxy = y//3*3
	#print(boxx)
	#print(boxy)
	for i in range(0,3) :
		for j in range(0,3): 	
			if grid[boxx+i][boxy+j] == n:	
				#print('Box Error')	
				return False
	#print('Valid')
	return True

def check_win(grid)
	newgrid = grid
	for x in range(9):
		for y in range(9):
			n = grid[x][y]
			if(n == 0):
				return False
			if (rules_met(x,y,n,newgrid)==False):
				print("Not a Win")
				return False
	return True

def createGrid ():
	row = 9
	col = 9
	grid = [[0 for x in range(row)]for y in range(col)]
	return grid
	
def printGrid(grid):
	row = 9
	col = 9
	for i in range(0,row):
		print(grid[i])

def setDifficulty(difficulty,grid):	
	dif = [50,45,40,35,30,25,20,15,10] 
	level = dif[difficulty]
	newGrid = grid
	k=0
	#tot = 0
	while(k!=level):
		check = False
		while(check == False):
			x = random.randint(0,8)
			y = random.randint(0,8)
			n = random.randint(1,9)
			check = rules_met(x,y,n,newGrid)
			if check == True:	
				newGrid[x][y] = n
				#tot = tot+1
		k= k + 1
	print(tot)	
	return newGrid

def enterNum(x,y,n,grid):
	newgrid = grid
	if(rules_met(x,y,n,newgrid)==True):
		newgrid[x][y]=n
	return newgrid

def deleteNum(x,y,grid):
	newgrid = grid
	newgrid[x][y]=0
	return newgrid

def solve(grid):
	grid
	for x in range(9):
		for y in range(9):
			if(grid[x][y]==0):
				for n in range (1,10):
					if (rules_met(x,y,n,grid)):
						grid[x][y] = n
						solve(grid)
						grid[x][y]=0
				return grid
	print("")
	for i in range(0,9):
		print(grid[i])
	input("more?")
		
#The Grid
#row = 9
#col = 9
#grid = [[0 for x in range(row)]for y in range(col)]
#Print the grid for the Sudoku Game
gamegrid = createGrid()
gamegrid = setDifficulty(8,gamegrid)
printGrid(gamegrid)
gamegrid = enterNum(0,0,2,gamegrid)
printGrid(gamegrid)
#gamegrid = deleteNum(0,0,gamegrid)
#gamegrid = solve(gamegrid)
printGrid(gamegrid)

	
	
	
	
	
	
