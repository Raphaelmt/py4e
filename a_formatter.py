def arithmetic_arranger(problems, result = False):
    op1 = list()
    op2 = list()
    op3 = list()
    arranged_problems = ''
    

    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    for problem in problems:
      op1.append(problem.split()[0])
      op2.append(problem.split()[1])
      op3.append(problem.split()[2])
      if op2[-1] != '+' and op2[-1] != '-':
        return "Error: Operator must be '+' or '-'."
      if op1[-1].isdigit() == False or op3[-1].isdigit() == False:
        return "Error: Numbers must only contain digits."
      if len(op1[-1]) > 4 or len(op3[-1]) > 4:
        return "Error: Numbers cannot be more than four digits."
          
     
    
    longest = list()
    for i in range(0,len(problems)):
      if len(op1[i]) == len(op3[i]):
        longest.append(0)
      elif len(op1[i]) > len(op3[i]):
        longest.append(1)
      else:
        longest.append(2)

    
    for i in range(0,len(problems)):
      if longest[i] == 2:
        spaces = 2 + len(op1[i]) + len(op3[i]) - len(op1[i])
      else:
        spaces = 2 +len(op1[i])
      
      if i != len(problems) - 1:
        arranged_problems = arranged_problems + op1[i].rjust(spaces) + '    '
      else:
        arranged_problems = arranged_problems + op1[i].rjust(spaces)
    arranged_problems = arranged_problems + '\n'
    

    for i in range(0,len(problems)):
      if longest[i] == 1 :
        spaces = 1 + len(op3[i]) + len(op1[i]) - len(op3[i])
      else:
        spaces = 1 + len(op3[i])
      
      if i != len(problems) - 1:
        arranged_problems = arranged_problems + op2[i] + op3[i].rjust(spaces) + '    '
      else:
        arranged_problems = arranged_problems + op2[i] + op3[i].rjust(spaces)
    arranged_problems = arranged_problems + '\n'

    for i in range(0,len(problems)):
      if i != len(problems) - 1:
        if longest[i] == 1 :
          arranged_problems = arranged_problems + ('-'*(len(op1[i])+2)) + '    '
        else:
          arranged_problems = arranged_problems + ('-'*(len(op3[i])+2)) + '    '
      else:
        if longest[i] == 1 :
          arranged_problems = arranged_problems + ('-'*(len(op1[i])+2))
        else:
          arranged_problems = arranged_problems + ('-'*(len(op3[i])+2))
    

    if result == True:
      arranged_problems = arranged_problems + '\n'
      for i in range(0,len(problems)):
        if op2[i] == '+':
          r = int(op1[i]) + int(op3[i])
        else:
          r = int(op1[i]) - int(op3[i])
        r = str(r)
        if i != len(problems) - 1:
          if longest[i] == 1 :
            arranged_problems = arranged_problems + r.rjust(len(r) + (len(op1[i])+2) - len(r)) + '    '
          else:
            arranged_problems = arranged_problems + r.rjust(len(r) + (len(op3[i])+2) - len(r)) + '    '
        else:
          if longest[i] == 1 :
            arranged_problems = arranged_problems + r.rjust(len(r) + (len(op1[i])+2) - len(r))
          else:
            arranged_problems = arranged_problems + r.rjust(len(r) + (len(op3[i])+2) - len(r))

      
  
        
    return arranged_problems

print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
