# inicia um contator
i = 1

# determina um máximo de tentativas em 3 usando o contator
while i < 4:
    login = input('Digite seu nome de usuário: \n')
    senha = input('Digite sua senha: \n')
    i +=  1

    # guarda a expressão booleana de comparação numa variável e a avalia na sequência 
    sucesso = senha == 'admin123' and login == 'admin'
    if sucesso:
        print('Bem vindo!')
        break
    else:
        print('Login ou senha inválidos. Tente novamente.')

if not sucesso:
    print('Tentativas excedidas')