i = 0
def sorting(li,key = None):
  
  li_cop = li.copy()
  ret = []
  while li_cop:
    ap_list = [key if key != None else li_cop][0]
    to_append =  ap_list.index(max(ap_list))
    
    ret.append(li_cop[to_append])
    li_cop.remove(li_cop[to_append])
  return ret
def zap(li1,li2):
  return [(li1[i],li2[i]) for i in range(0,len(li1))]

data = {'sport':None,'names':{}}
def inc(val):
  global i
  i+=val
def dec(val):
  global i
  i-=val
def times(val):
  global i
  
  i*=val
def add():
  global i
  i = 0
  person_name = input('what is the persons name')
  county = input('witch country is that person from? ')
  while True:
    inp = input('what happend')
    if inp == 'done':
      break
    if inp == '+':
      amount = float(input('what is the amount'))
      inc(amount)
    if inp == '-':
      amount = float(input('what is the amount'))
      dec(amount)
    if inp == '*':
      amount = float(input('what is the amount'))
      times(amount)
    print(f"the amount is:{i}")
  print(f"the final score is:{i}")
  data['names'][f"{person_name}        {county}"] = i
def show_scoreboard():
  print(data['sport'])
  print('______________________')
  print(' name         country       score')
  k = list(data['names'].keys())
  v = list(data['names'].values())
  v = sorting(v)
  k = sorting(k,key=v)
  num = 1

  for name, score in zap(k,v):
    print(f'{num}.{name}  :  {score}')
    num+=1
def main():
  race = input('what race is this?')
  data['sport'] = race
  while True:
    todo = input('what happend')
    if todo == 'done':
      break
    else:
      add()
  show_scoreboard()
if __name__ == '__main__':
  main()
print('done')
