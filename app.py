import os;

restaurantes = [
    {'nome': 'Laguápa', 'categoria':'Brasileira', 'ativo': False},
    {'nome': 'Nau - Frutos do Mar', 'categoria': 'Portuguesa', 'ativo': True},
    {'nome': 'Manu', 'categoria': 'Brasileira', 'ativo': False},
];

def exibir_nome_do_programa():
    '''Essa função é responsável pela exibição do nome do app'''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """);

def exibir_opcoes():
    '''Essa função é responsável por mostrar as opções do menu'''
    print('1. Cadastrar restaurante.');
    print('2. Listar restaurante. ');
    print('3. Alternar estado do restaurante. ');
    print('4. Sair.\n');

def finalizar_app():
    exibir_subtitulo('Finalizando o app.');

def opcao_invalida():
    '''Essa função é respnsável pela mensagem de erro quando escolhemos uma opção errada no menu.'''
    print('Opção inválida!\n');
    voltar_ao_menu_principal();

def voltar_ao_menu_principal():
    '''Essa função é responsável pelo reload do app'''
    input('\nDigite uma tecla para voltar ao menu principal: ');
    main();

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibit os subtitulos do app'''
    os.system('cls');
    linha = '*' * (len(texto));
    print(linha);
    print(f'{texto}\n');
    print(linha);

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo resataurante.

    Inputs:
    - Nome do Restaurante
    - Categoria do Restaurante

    Outputs:
    - Adiciona um novo  restaurante a lista de restaurantes.
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes.');

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ');

    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ');

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False};
    restaurantes.append(dados_do_restaurante);
    print(f'\nO {nome_do_restaurante} foi cadastrado com sucesso!');

    voltar_ao_menu_principal();

def listar_restaurantes():
    '''Essa função é responsável por listar todos os restaurantes'''
    exibir_subtitulo('Listando os restaurantes.');
    print(f"{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}");
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome'];
        categoria_restaurante = restaurante['categoria'];
        status_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado';
        print(f'.{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante.ljust(20)}');

    voltar_ao_menu_principal();

def alternar_estado_do_restaurante():
    '''Essa função é responsável por alternar o status do restaurante.'''
    exibir_subtitulo('Alternando o estado do restaurante');

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o esdado: ');
    restaurante_encontrado = False;

    for restaurante in restaurantes:
        if(nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True;
            restaurante['ativo'] = not restaurante['ativo'];

            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O resataurante {nome_restaurante} foi desativado com sucesso';

            print(mensagem);
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado');
    voltar_ao_menu_principal();

def escolher_opcao():
    '''Essa função é responsável pela exibição do menu de opções do app'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '));
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante();
        elif opcao_escolhida == 2:
            listar_restaurantes();
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante();
        elif opcao_escolhida == 4:
            finalizar_app();
        else:
            opcao_invalida();
    except:
        opcao_invalida();

def main():
    os.system('cls');
    exibir_nome_do_programa();
    exibir_opcoes();
    escolher_opcao();

if __name__ == '__main__':
    main()