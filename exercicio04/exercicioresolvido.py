import colorama
from colorama import Fore,Style

#Solicitação da nota ao usuário:
nota = float(input('Digite sua nota de 0 a 10: '))

 # Determinar o resultado com base na nota
if nota >= 7:
    resultado ='APROVADO'
    print(f'Parabéns, você foi {Fore.BLUE}{resultado}{Style.RESET_ALL}')
else:
    resultado ='REPROVADO'
    print(f'Você foi {Fore.RED}{resultado}{Style.RESET_ALL}')