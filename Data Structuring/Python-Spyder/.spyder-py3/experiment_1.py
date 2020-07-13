# -*- coding: utf-8 -*-

#%%
def hello():
    print ("Hello, world!")
    
  #%%  
def gridp(grid):
    counter = 0
    name = 'name'
    total = 0.0
    
    for i in range(3, 1254):
        if (grid.cell(row = i, column = 1).value) == (grid.cell(row = i-1, column = 1).value):
            grid.cell(row = i-1, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = ((grid.cell(row = i-1, column = 2).value) + (grid.cell(row = i, column = 2).value)) / 2
            grid.cell(row = i-1, column = 2).value = 'delete'
            
#%% 
def gridc(grid):
    counter = 0
    total = 0.0
    for i in range(1,1271):
        total = float(total) + (grid.cell(row = i, column = 2).value)
        counter = float(counter) + 1
        
        if i == 1271:
            grid.cell(row = i, column = 2).value = total/float(counter)
            
        elif ((grid.cell(row = i + 1, column = 1).value) != (grid.cell(row = i, column = 1).value)):
            grid.cell(row = i, column = 2).value = total/float(counter)
            total = 0.0
            counter = 0
            
        else:
            grid.cell(row = i, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = 'delete'
            
#%% 
def gridtot(grid):
    total = 0.0
    for i in range(2,1304):
        total = float(total) + (grid.cell(row = i, column = 2).value)
        
        
        if i == 1304:
            grid.cell(row = i, column = 2).value = total
            
        elif ((grid.cell(row = i + 1, column = 1).value) != (grid.cell(row = i, column = 1).value)):
            grid.cell(row = i, column = 2).value = total
            total = 0.0
            
            
        else:
            grid.cell(row = i, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = 'delete'
            
#%% 
def gridrot(grid):
    counter = 0
    total = 0.0
    for i in range(2,7561):
        total = float(total) + (grid.cell(row = i, column = 2).value)
        counter = float(counter) + (grid.cell(row = i, column = 3).value)
        
        if i == 7561:
            grid.cell(row = i, column = 2).value = total/float(counter)
            grid.cell(row = i, column = 3).value = counter
            
        elif ((grid.cell(row = i + 1, column = 1).value) != (grid.cell(row = i, column = 1).value)):
            grid.cell(row = i, column = 2).value = total/float(counter)
            grid.cell(row = i, column = 3).value = counter
            total = 0.0
            counter = 0
            
        else:
            grid.cell(row = i, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = 'delete'
            grid.cell(row = i, column = 3).value = 'delete'
            
#%% 
def gridRaw(grid):
    evalution = ''
    overall = ''
    easiness = ''
    clarity = ''
    grade = ''
    
    for i in range(2,5951):
        
        if grid.cell(row = i, column = 2).value != None:
            evalution = grid.cell(row = i, column = 2).value
        elif grid.cell(row = i, column = 3).value != None:
            overall = grid.cell(row = i, column = 3).value
        elif grid.cell(row = i, column = 4).value != None:
            easiness = grid.cell(row = i, column = 4).value
        elif grid.cell(row = i, column = 5).value != None:
            clarity = grid.cell(row = i, column = 5).value
        elif grid.cell(row = i, column = 6).value != None:
            grade = grid.cell(row = i, column = 6).value
            
            
        
        if i == 5951:
            grid.cell(row = i, column = 2).value = evalution
            grid.cell(row = i, column = 3).value = overall
            grid.cell(row = i, column = 4).value = easiness
            grid.cell(row = i, column = 5).value = clarity
            grid.cell(row = i, column = 6).value = grade
            
        elif ((grid.cell(row = i + 1, column = 1).value) != (grid.cell(row = i, column = 1).value)):
            grid.cell(row = i, column = 2).value = evalution
            grid.cell(row = i, column = 3).value = overall
            grid.cell(row = i, column = 4).value = easiness
            grid.cell(row = i, column = 5).value = clarity
            grid.cell(row = i, column = 6).value = grade
            evalution = ''
            overall = ''
            easiness = ''
            clarity = ''
            grade = ''
            
        else:
            grid.cell(row = i, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = 'delete'
            grid.cell(row = i, column = 3).value = 'delete'
            grid.cell(row = i, column = 4).value = 'delete'
            grid.cell(row = i, column = 5).value = 'delete'
            grid.cell(row = i, column = 6).value = 'delete'
            
#%% 
def gridCount(grid):
    
    for i in range(2,5516):
        
         if grid.cell(row = i, column = 3).value != None and  grid.cell(row = i, column = 4).value != None and grid.cell(row = i, column = 5).value != None:
            grid.cell(row = i, column = 6).value = 5
         else:
            grid.cell(row = i, column = 6).value = 0

#%%        
def gridSingle(grid):
    rmp_value = ''
    uc_value = ''
    
    for i in range(2,5933):
        
        if grid.cell(row = i, column = 3).value != None:
            rmp_value = grid.cell(row = i, column = 3).value
        elif grid.cell(row = i, column = 4).value != None:
            uc_value = grid.cell(row = i, column = 4).value
            
            
        
        if i == 7473:
            grid.cell(row = i, column = 3).value = rmp_value
            grid.cell(row = i, column = 4).value = uc_value

            
        elif ((grid.cell(row = i + 1, column = 1).value) != (grid.cell(row = i, column = 1).value)) or ((grid.cell(row = i + 1, column = 2).value) != (grid.cell(row = i, column = 2).value)):
            grid.cell(row = i, column = 3).value = rmp_value
            grid.cell(row = i, column = 4).value = uc_value
            rmp_value = ''
            uc_value = ''
            
        else:
            grid.cell(row = i, column = 1).value = 'delete'
            grid.cell(row = i, column = 2).value = 'delete'
            grid.cell(row = i, column = 3).value = 'delete'
            grid.cell(row = i, column = 4).value = 'delete'
#%%        
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
    