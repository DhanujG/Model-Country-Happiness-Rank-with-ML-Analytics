    
    for i in range(2,6436):
        
        if grid.cell(row = i, column = 3).value != None:
            dept = grid.cell(row = i, column = 3).value
        if grid.cell(row = i, column = 4).value != None:
            rmp_value = grid.cell(row = i, column = 4).value
        if grid.cell(row = i, column = 5).value != None:
            uc_value = grid.cell(row = i, column = 5).value
        
        
        
        if i == 6436:
            grid.cell(row = i, column = 3).value = dept
            grid.cell(row = i, column = 4).value = rmp_value
            grid.cell(row = i, column = 5).value = uc_value
        
        
        elif ((grid.cell(row = i + 1, column = 1).value) != (grid.cell(row = i, column = 1).value)) or ((grid.cell(row = i + 1, column = 2).value) != (grid.cell(row = i, column = 2).value)):
            grid.cell(row = i, column = 3).value = dept
            grid.cell(row = i, column = 4).value = rmp_value
            grid.cell(row = i, column = 5).value = uc_value
            dept = ' '
            rmp_value = ''
            uc_value = ''
        
        else:
            grid.cell(row = i, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = 'delete'
            grid.cell(row = i, column = 3).value = 'delete'
            grid.cell(row = i, column = 4).value = 'delete'
            grid.cell(row = i, column = 5).value = 'delete'
grid = wb['Sheet1']
gridSDept(grid)
wb.save('Dept_Reponses_Number.xlsx')
wb = o
wb = openpyxl.load_workbook(filename = 'Dept_Responses_Number.xlsx')
wb = openpyxl.load_workbook(filename = 'Dept_Reponses_Number.xlsx')
grid = wb['Sheet1']
def gridCount(grid):
    
    for i in range(2,5516):
         
         if grid.cell(row = i, column = 3).value != None and  grid.cell(row = i, column = 4).value != None and grid.cell(row = i, column = 5).value != None:
            grid.cell(row = i, column = 6).value = 5
         else:
            grid.cell(row = i, column = 6).value = 0
gridCount(grid)
wb.save('Dept_Reponses_Number.xlsx')
def gridSDept(grid):
    dept = ' '
    rmp_value = ''
    uc_value = ''
    
    for i in range(2,6421):
        
        if grid.cell(row = i, column = 3).value != None:
            dept = grid.cell(row = i, column = 3).value
        if grid.cell(row = i, column = 4).value != None:
            rmp_value = grid.cell(row = i, column = 4).value
        if grid.cell(row = i, column = 5).value != None:
            uc_value = grid.cell(row = i, column = 5).value
        
        
        
        if i == 6421:
            grid.cell(row = i, column = 3).value = dept
            grid.cell(row = i, column = 4).value = rmp_value
            grid.cell(row = i, column = 5).value = uc_value
        
        
        elif ((grid.cell(row = i + 1, column = 1).value) != (grid.cell(row = i, column = 1).value)) or ((grid.cell(row = i + 1, column = 2).value) != (grid.cell(row = i, column = 2).value)):
            grid.cell(row = i, column = 3).value = dept
            grid.cell(row = i, column = 4).value = rmp_value
            grid.cell(row = i, column = 5).value = uc_value
            dept = ' '
            rmp_value = ''
            uc_value = ''
        
        else:
            grid.cell(row = i, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = 'delete'
            grid.cell(row = i, column = 3).value = 'delete'
            grid.cell(row = i, column = 4).value = 'delete'
            grid.cell(row = i, column = 5).value = 'delete'
wb = openpyxl.load_workbook(filename = 'Comb_Overall_Final.xlsx')
grid = wb['Sheet1']
gridSDept(grid)
wb.save('Dept_Overall_Rating.xlsx')
def gridCount(grid):
    
    for i in range(2,5516):
         
         if grid.cell(row = i, column = 3).value != None and  grid.cell(row = i, column = 4).value != None and grid.cell(row = i, column = 5).value != None:
            grid.cell(row = i, column = 6).value = 5
         else:
            grid.cell(row = i, column = 6).value = 0
wb = openpyxl.load_workbook(filename = 'Dept_Overall_Rating.xlsx')
grid = wb['Sheet1']
gridCount(grid)
wb.save('Dept_Overall_Rating.xlsx')