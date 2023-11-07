import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy

counter = 0
my_file = open("input.txt", "r")
data = my_file.read().split("\n")
my_file.close()

alive_neigh = 0 # number of live neighbours

grid = [[int(j) for j in i] for i in data]
d0 = copy.deepcopy(grid) # grid to work on at each cycle, used to synchronize evolution of every cells. To prevent modifying the same grid where the rules are checked.
grid = grid[:-1]
d0 = d0[:-1]
print("d0 : ", d0, grid)

# Function to make the cells evolved at every cycle
def evolve(df):
    global grid
    global counter
    counter +=1
    print("this is counter :", counter)
    d0 = copy.deepcopy(df) # Update d0 as last evolution grid
    # For-loop on each cell
    for row in range(len(df)):
        print("row : ", df[row])

        for column in range(len(df[row])):

            alive_neigh = 0 # initialize number of neighbour at 0 for each cell

            try: # Handle the "Out of index" error (due to the borders of the grid)

                # Check the neighbourhood and increment if live cell found
                if df[row + 1][column] == 1:
                    alive_neigh +=1 

                if df[row - 1][column] == 1:
                    alive_neigh +=1

                if df[row][column - 1] == 1:
                    alive_neigh +=1

                if df[row][column + 1] == 1:
                    alive_neigh +=1

                if df[row + 1][column + 1] == 1:
                    alive_neigh +=1

                if df[row - 1][column - 1] == 1:
                    alive_neigh +=1

                if df[row + 1][column - 1] == 1:
                    alive_neigh +=1

                if df[row - 1][column + 1] == 1:
                    alive_neigh +=1
                
                # Conway's game's rules

                if alive_neigh == 2: # 2 neighbours cells alive
                    if df[row][column] == 1: # current cell is alive, stays alive
                        continue
                    
                elif alive_neigh == 3: # 3 neighbours cells alive
                    if df[row][column] == 1: #current cell is alive
                        # stays alive
                        continue
                        
                    elif df[row][column] == 0: # current cell is dead
                        d0[row][column] = 1 # becomes alive
                        
                else: # <2 or >3 neighbours cells alive : overpopulation or underpopulation
                    if df[row][column] == 1: # current cell alive
                        d0[row][column] = 0 # current cell dies

            except IndexError:
                pass # If out of index error, do nothing, out of grid error.
    grid = copy.deepcopy(d0)
    return copy.deepcopy(d0) # return an independant copy of the evolved grid.

f = open("evolve.txt", "w")

f.write(str(grid))
f.close()
i = 0
def updater(frame_number, img):
    global grid
    global i

    if counter == 50:
        f = open("evolve.txt", "w")
        f.write(str(grid))
        f.close
    grid = evolve(grid)
    print("this is i :", i)
    i+=1
    print("this is frame_numb :", frame_number)
    img.set_data(grid)
    return img

fig, ax = plt.subplots() # create a figure
img = ax.imshow(grid,cmap ="gray" ) # plot the first frame

ani = animation.FuncAnimation(fig , updater , fargs =(img,), frames =100 , 
                              repeat = False , interval =200)
plt.show()

#plt.imshow(grid)
#plt.show(block = True)
#plt.close()