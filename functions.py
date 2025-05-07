# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 18:34:03 2025

Functions that are used all through all the programs

@author: krati

"""
def num_score(value):
    if value == "Yes":
        return 1
    elif value == "Don't know":
        return 0
    elif value == "No":
        return 0
    elif value == "More":
        return 1
    elif value == "Tap":
        return 1
    elif value == "Well":
        return 1
    elif value == "Never":
        return 0
    elif value == "Sometimes":
        return 1
    elif value == "Often":
        return 2
    elif value == "Female":
        return 1
    elif value =="Male":
        return 2
    elif value == "Parents":
        return 1
    elif value == "Guardian":
        return 2
    elif value == "Relatives":
        return 3
    elif value == "Others":
        return 0
    elif value == "3" or value ==  3:
        return 1
    elif value == "2" or  value == 2:
        return 1
    elif value == "1" or  value == 1:
        return 0
    else:
        return -1 


def assign_score(sheet_in,row_in,col_in,sheet_out,row_out,col_out):
    """
    

    Parameters
    ----------
    sheet_in : TYPE = string
        name of the sheet that is has the qualitative data
    row_in : TYPE integer
        row in which the cell to read is
    col_in : TYPE integer
        column in which the cell to read is
    sheet_out : string
        name of the output sheet
    row_out : TYPE integer
        row of the output cell
    col_out : TYPE integer
        column of the output cell

    Returns
    -------
    None.

    """
    val = sheet_in.cell(row=row_in,column=col_in).value 
    num = num_score(val)
    sheet_out.cell(row=row_out, column=col_out, value = num)

def cutoff_score(sheet_in,row_in,col_in,cutoff,list_name,index):
    
    
    
    """
    

    Parameters
    ----------
    sheet_in : TYPE string
        name of the input sheet
    row_in : TYPE integer
        row of the input cell
    col_in : TYPE integer
        coloumn of the input cell
    cutoff : TYPE float
        the value of cutoff above which the child is considered deprived
    list_name : TYPE list
        list which stores the index of the child who is considered deprived
    index : TYPE index
        index of the deprived child

    Returns
    -------
    None.

    """
    val = sheet_in.cell(row=row_in, column=col_in).value
    if val>= cutoff:
        list_name.append(index)


def vul_cut_cat(score,type_ans):
    """
    

    Parameters
    ----------
    score : float
        the score of the child
    type_ans : string
        the type if the ans

    Returns
    -------
    int
       if returns 1 then the child in vulnerable in the category
       if returns 0 then the child is not vulnerable
       if returns -1 then there is an error

    """
    if(type_ans == "Yes"):
        if(score<1):
            return 1 
        else:
            return 0
    elif(type_ans =="Often"):
        if(score<2):
            return 1 
        else:
            return 0
    elif(type_ans == "Tap"):
        if(score<1):
            return 1
        else:
            return 0
    elif(type_ans == "food"):
        if (score<1):
            return 1
        else:
            return 0
    elif(type_ans == "31"):
        if (score<1):
            return 1
        else:
            return 0
    else:
        return -1

def vul_domain(score,dom_index):
    """
    

    Parameters
    ----------
    score : list of intgers
        the score of the child
    dom_index : integer 
        ratio of categories 
        you need to be vulnerable 

    Returns
    -------
    int
       if returns 1 then the child in vulnerable in the category
       if returns 0 then the child is not vulnerable
       if returns -1 then there is an error

      also the function is structured so that the user can change the criteria according to their need
    """
    if(dom_index == 1):#statelessness
        if(0 in score):
            return 1 
        else:
            return 0
    elif(dom_index ==2):#financial Sec
        vul = []
        if(score[0]==0 or score[0]==1):
            vul.insert(0, 0)
        else:
            vul.insert(0, 1)
        vul.insert(1, score[1])
        if(score[2]==0 or score[2]==1):
            vul.insert(2, 0)
        else:
            vul.insert(2, 1)
        if(vul.count(0)>1):
            return 1 
        else:
            return 0
    elif(dom_index ==3):#home
        if(0 in score):
            return 1
        else:
            return 0
    elif(dom_index ==4):#personal Safety
        if( 0 in score):
            return 1 
        else:
            return 0
    elif(dom_index ==5):#diet
        if((score[1]==0 )or(score[0]) <2 ):
            return 1
        else:
            return 0
    elif(dom_index ==6): #Health to do
        if(0 in score):
            return 1 
        else:
            return 0
    elif(dom_index ==7): #Work Exploitation
        if(score.count(0)==2):
            return 1
        else:
            return 0
    elif(dom_index ==8): #water 
        if(0 in score):
            return 1 
        else:
            return 0
    elif(dom_index ==9):# education
        vul = []
        vul.append(score[0])
        vul.append(score[2])
        vul.append(score[5])
        vul.append(score[6])
        if(0 in vul):
            return 1
        else:
            return 0
    elif(dom_index ==10):# acess to info ask
        if(score.count(0)>1):
            return 1 
        else:
            return 0
    else:
        return -1