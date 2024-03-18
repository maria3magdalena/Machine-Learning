# -*- coding: utf-8 -*-



def convert_file (filepath, nazwa):
    
  file = open(filepath, "r")
  with open(filepath) as file:
    lines = []
    with open(filepath) as file:
       lines = [line.rstrip() for line in file]
  
  file2 = open(nazwa, 'w')
  n = int(lines[0])
  file2.write(str(n) + '\n')
  i = 1
  
  for x in range(2):
      while(len(lines[i]) <= 1):
           i=i+1
      line = lines[i].split()     
      if len(line) == n:
         for j in range(n):
             line = lines[i+j].split()
             for k in range(n):
                 file2.write(line[k]+' ')
             file2.write('\n')
         i = i + n
      else:
          for j in range(n): 
              m = 0
              while m<n:
                  line = lines[i].split()
                  l = 0
                  while m<n and l<len(line):
                      file2.write(line[l]+' ')
                      m = m+1
                      l = l+1
                  i = i+1
              file2.write('\n')
      file2.write('\n')
              
     
 
              
      
      
 
