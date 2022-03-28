import re
def checkValidity(param):
  tmp = param.split()
  if re.match('^(\d+)$',tmp[0]) and re.match('^(\d+)$',tmp[2]):
    if len(tmp[0])<=4 and len(tmp[2])<=4:
      if tmp[1]=='+' or tmp[1]=='-':
        return True,""
      return False,"Error: Operator must be '+' or '-'."
    return False,"Error: Numbers cannot be more than four digits."
  return False,"Error: Numbers must only contain digits."


def list_2_string(lst,separator='    '):
  return separator.join(lst)

def arithmetic_arranger(params,show=False):
  number_1 = []
  number_2 = []
  size_sep = []
  operand = []

  result = []
  if len(params)>5:
    return "Error: Too many problems."

  for ar in params:
    res = checkValidity(ar)
    tmp=ar.split()
    if res[0]:
      print(tmp)
      number_1.append(int(tmp[0]))
      number_2.append(int(tmp[2]))
      size_sep.append(max(len(tmp[0]),len(tmp[2]))+2)
      operand.append(tmp[1])
      result.append(number_1[-1]+number_2[-1] if operand[-1]=='+' else number_1[-1]-number_2[-1])
    
    else:
      print(res[1])
      return

  line_1=[]
  line_2=[]
  line_3=[]
  line_4=[]
  for i in range(len(result)):
    line_1.append(str(number_1[i]).rjust(size_sep[i]," "))
    line_2.append(str(number_2[i]).rjust(size_sep[i]," "))
    line_2[-1]=line_2[-1].replace(line_2[-1][0:1],operand[i],1)
    line_3.append("-"*size_sep[i])
    line_4.append(str(result[i]).rjust(size_sep[i]," "))
    
  line_1=list_2_string(line_1)
  line_2=list_2_string(line_2)
  line_3=list_2_string(line_3)
  line_4=list_2_string(line_4)
  print(f"{line_1}\n{line_2}\n{line_3}")
  if show:
    print(f"{line_4}")

