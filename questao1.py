if __name__ == '__main__':
  grafo = {
    'A' : [0,1,1,1,1,1],#A
    'B' : [1,0,1,0,0,0],#B
    'C' : [1,1,0,1,0,0],#C
    'D' : [1,0,1,0,1,0],#D
    'E' : [1,0,0,1,0,1],#E
    'F' : [1,0,0,0,1,0] #F
  }
  a = 0 
  b = 0 
  c = 0
  d = 0 
  e = 0
  f = 0
  for i in grafo:
    for j in range(len(grafo[i])):
      grafos = ['A','B','C','D','E','F']
      print(f' {i}{grafos[j]} = {grafo[i][j]}', end=' ')
         
    print("\n")

  for i in grafo:
    for j in range(len(grafo[i])):
      #print(i)
      if grafo[i][j] > 0 and i == 'A':
        a+=1
      elif grafo[i][j] > 0 and i == 'B':
        b+=1
      elif grafo[i][j] > 0 and i == 'C':
        c+=1
      elif grafo[i][j] > 0 and i == 'D':
        d+=1
      elif grafo[i][j] > 0 and i == 'E':
        e+=+1
      elif grafo[i][j] > 0 and i == 'F':
        f+=1
        
  print(f'A = {a} B = {b} C = {c} D = {d} E = {e} F = {f}')