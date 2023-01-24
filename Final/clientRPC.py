import rpyc

proxy = rpyc.connect('localhost', 18861, config={'allow_public_attrs': True})

op = input(' 1 - Cadastrar usuário\n 2 - Listar Quantidade\n 3 - Listar códigos cadastrados \n 4 - Listar Codigos da sala\n\n')
list_cod = []
while(op!= '5'):
    if (op == '1'):
        cod = input("Digite o código\n")
        list_cod = (str(proxy.root.listar_usuarios()))
        if cod in list_cod:
            print('Código já está Cadastrado\n')
        else:
            proxy.root.cadastrar_cod(str(cod))
            print("Código Cadastrado\n")
    if (op == '2'):
        print(proxy.root.listar_quantidade())
    if (op == '3'):
        print(proxy.root.listar_usuarios())
    if (op == '4'):
        print(proxy.root.listar_cod_sala())
    op = input(' 1 - Cadastrar usuário\n 2 - Listar Quantidade\n 3 - Listar códigos cadastrados \n 4 - Listar Codigos da sala\n\n')
        



