from random import randint


def create_field(rows, columns, mines):
    tiles_list = {}  # dictionnary containing coordinates and value of each tile
    tile_number = 0 # value of the tiles (initially, they're all equal to 0)
    for i in range(rows): # create the rows
        for j in range(columns): # create the columns
            tiles_list[i, j] = tile_number # add the created tile with its values
                                           # and coordinates to the dictionnary

    k = 0 # k = number of mines planted so far
    while k < mines: # mines = number of mines you want to plant in the grid
        mine_r = randint(0, rows-1) # creating random row coordinate for the mine
        mine_c = randint(0, columns-1) # creating random column coordinate 
                                       # for the mine
        if tiles_list[mine_r, mine_c] == 0: # if the tile is empty (equal to 0)
            tiles_list[mine_r, mine_c] = 100 # replacing 0 by 100 (=mine)
            k += 1 # we planted a mine, so we're counting it
    return rows, columns, tiles_list # returning the updated tiles list


def print_field(field): # field contains three variables : 
    rows = field[0]     # the number of rows
    columns = field[1]     # the number of columns
    tiles_list = field[2]     # the tiles dictionary (tile coordinates and value)
    for row in range(rows):
        for col in range(columns):
            print("%5d" % tiles_list[row, col], end="") # "5%d" : padding
         # end="" : no "saut de ligne" after printing an element of a row 
         # (or else you'd only have the values printed one after the other
         # in separate lines)
        print() # saut de ligne after a row is completed
    print() 

# this function counts the number of mines around each tile
def count_mines(field, row, col):
    rows = field[0] # number of rows
    cols = field[1] # number of columns
    fld = field[2] # the tiles dictionary (tile coordinates and value)

    if fld[row, col] == 100: # if tile contains mine :
        return # not changing the value of the tile
               # else : we can carry on

    mines = 0 # mine count is 0 initially
    # we want to check if there's a mine in the tiles that are in the 
    # tile's row (0), the one above (-1) and the one beneath (1)
    for i in [-1, 0, 1]:
        # we want to check if there's a mine in the tiles that are in the 
        # tile's column (0), the one on the left (-1) and on the right (1)
        for j in [-1, 0, 1]:
            r = row + i # checking rows around the tile's "row"
            c = col + j # checking columns around the tile's "col"

            if r < 0 or r >= rows: # if the row is out of reach : continuing
                continue
            if c < 0 or c >= cols: # if the column is out of reach : continuing
                continue
            if r == row and c == col: # we don't want to count the tile we're on
                continue
            if fld[r, c] == 100: # if tile around inspected tile contains a mine
                mines += 1 # adding 1 to the mine count

    fld[row, col] = mines 
    # updating the value of the tile to the number of mines around it


# this function fills a created field with the number of mines around each tile
def fill_field(field):
    rows = field[0]
    cols = field[1]
    for r in range(rows):
        for c in range(cols):
            count_mines(field, r, c)


# creating a field with 5 rows, 5 columns and 3 mines
field1 = create_field(5, 5, 3)
print_field(field1)
fill_field(field1)
print_field(field1)
