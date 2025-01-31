# What should I do solve this problem

'''
I need three methods, the first one will help me to 
find empty elements. : when they don't exist at start meaning the grid is okay
    consider their row and column
    then
Seek the corresponding elements at the row, colum position
    seek an element to replace with it, for the found element,
    check if they already exist in columns and rows 
        also in the 3x3 subgrid
Perform recursive algo 
'''
def find_empty_cell(gridnumbers)->None:
    for row in range(0,9):
        for colum in range(0,9):
            if gridnumbers[row][colum]==0:
                return row,colum

def check_existence_row(gridnumbers,row,num)->False:
    for j in range(0,9):
        if gridnumbers[row][j]==num:
            return True
    '''
    return num in [gridnumbers[row][j] for j in range(9)]
    
    '''
    
def check_existence_column(gridnumbers,col,num)->False:
    for i in range(0,9):
        if gridnumbers[i][col]==num:
            return True
    '''
        return num in [gridnumbers[row][i] for j in range(9)] 
        
    ''' 
def check_existence_in_subgrid(gridnumbers,col,row,num)->False:
    start_col_position = col-col % 3
    start_row_position = row-row % 3
    
    for i in range(3):
        for j in range(3):
            if gridnumbers[i+start_row_position][j+start_col_position]==num:
                return True

def is_present(gridnumbers,col,row,num):
    
    return check_existence_in_subgrid(gridnumbers,col,row,num) and \
           check_existence_column(gridnumbers,col,num) and \
           check_existence_column(gridnumbers,col,num)
        
def let_solve_sudoku(gridnumbers):
    '''def find_empty_cell(gridnumbers)'''
    empty_cell= find_empty_cell(gridnumbers)
    
    if empty_cell==None:
        return True # end
    
    #take colum and row concerned
    row,column=empty_cell
    
    for num in range(1,9):
        '''check if column, row or 3x3 subgrid contains
        num'''
        if not is_present(gridnumbers,column,row,num):
            gridnumbers[row][column]=num
            
            if let_solve_sudoku(gridnumbers):
                return True
            
            gridnumbers[row][column]=0# if the next solve_sudoku returns a false we backtrack
            
    return False
    


