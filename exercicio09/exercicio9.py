contagem_pares =0
contagem_impar= 0


while True:
  numero = int(input('Digite um numero(0 para encerrar)'))
  if numero == 0:
   break
  if numero<0:
    print("Digite um numero positivo")
    continue
   
  if numero %2 ==0:
    contagem_pares +=1

  else:
   contagem_impar +=1



print(f'A quantidade de numeros pares sao: {contagem_pares}')
print(f'A quantidade de numeros Impares sao: {contagem_impar}')
