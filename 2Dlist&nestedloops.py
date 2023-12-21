#2D-grid and Nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#for in "[]" i want to put the index of the row that i want to access.
print(number_grid[2][-1]) #perform in L Shape
#by using rows in the grid
for row in number_grid:
    for col in row: #use when you have to print the grid or matrix into a single line
        print(col)
