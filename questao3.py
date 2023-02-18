if __name__ == '__main__':
  # Variables:
  grafo = {
    'A' : [0,1,1,0,0,0],#A
    'V' : [-1,0,0,1,0,1],#V
    'C' : [-1,0,0,0,0,1],#C
    'D' : [0,-1,0,0,1,0],#D
    'F' : [0,0,0,-1,0,-1],#F
    'W' : [0,-1,-1,0,1,0] #W
  }
  a = 0 
  v = 0 
  c = 0
  d = 0 
  f = 0
  w = 0
  ae = 0
  ve = 0
  ce = 0
  de = 0
  fe = 0
  we = 0

  # Matrix Printer:
  for i in grafo:
    for j in range(len(grafo[i])):
      grafos = ['A','V','C','D','F','W']
      if grafo[i][j]:
        print(f' {i}{grafos[j]} = 1', end=' ')
      else:
        print(f' {i}{grafos[j]} = 0', end=' ')
        
         
    print("\n")

  # Degree Counter:
  for i in grafo:
    for j in range(len(grafo[i])):
      #print(i)
      if grafo[i][j] > 0 and i == 'A':
        a+=1
      elif grafo[i][j] < 0 and i == 'A':
        ae+=1
      if grafo[i][j] > 0 and i == 'V':
        v+=1
      elif grafo[i][j] < 0 and i == 'V':
        ve+=1
      if grafo[i][j] > 0 and i == 'C':
        c+=1
      elif grafo[i][j] < 0 and i == 'C':
        ce+=1
      if grafo[i][j] > 0 and i == 'D':
        d+=1
      elif grafo[i][j] < 0 and i == 'D':
        de+=1
      if grafo[i][j] > 0 and i == 'F':
        f+=1
      elif grafo[i][j] < 0 and i == 'F':
        fe+=1
      if grafo[i][j] > 0 and i == 'W':
        w+=1
      elif grafo[i][j] < 0 and i == 'W':
        we+=1
        
  print('Entradas:')
  print(f'A_S={a} V_S={v} C_S={c} D_S={d} F_S={f} W_S={w} \n')
  print('Saidas:')
  print(f'A_E={ae} V_E={ve} C_E={ce} D_E={de} F_E={fe} W_E={we}')