temp = []
princ = []
mai = men = 0
while True:
  temp.append(str(input('Nome: ')))
  temp.append(float(input('Peso: ')))
  if len(princ) ===0:
    mai = men = temp[1]
  else:
      if temp[1] > mai:
         mai = temp[1]
