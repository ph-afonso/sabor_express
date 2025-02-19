# Sabor Express

**Sabor Express** é um sistema de gerenciamento de restaurantes. Com ele, você pode cadastrar novos restaurantes, listar os já cadastrados e alternar o status de ativo ou inativo de cada restaurante. Esse programa foi desenvolvido em Python e executa no terminal.

## Funcionalidades

1. **Cadastro de Restaurante**: Permite adicionar novos restaurantes à lista, especificando o nome e a categoria.
2. **Listar Restaurantes**: Exibe uma lista completa de todos os restaurantes cadastrados, com seu nome, categoria e status (ativado ou desativado).
3. **Alternar Estado do Restaurante**: Altera o status do restaurante entre ativo e inativo.
4. **Sair**: Encerra o programa.

---

## Pré-requisitos

- Python 3 instalado no sistema.
- Um terminal para execução do script.

## Como Executar

1. **Clonar ou Baixar o Código**: Certifique-se de ter o código em sua máquina local.
2. **Navegar para o Diretório**: No terminal, vá até o diretório onde o código está localizado.
3. **Executar o Programa**: Digite o comando abaixo no terminal para iniciar o sistema:

    ```bash
    python nome_do_arquivo.py
    ```

   Substitua `nome_do_arquivo.py` pelo nome do arquivo onde o código está salvo.

---

## Uso do Sistema

1. **Início**:
   - Ao iniciar o programa, será exibido o nome do sistema junto com as opções do menu.

2. **Menu de Opções**:
   - Escolha uma das opções do menu digitando o número correspondente e pressionando "Enter".

3. **Funções Principais**:
   - **Cadastrar Restaurante**:
     - Insira o nome e a categoria do restaurante que deseja adicionar.
     - O sistema confirma o cadastro e retorna ao menu principal.
   - **Listar Restaurantes**:
     - Exibe todos os restaurantes com seus nomes, categorias e status.
   - **Alternar Estado do Restaurante**:
     - Insira o nome do restaurante cujo status deseja alternar.
     - O sistema confirma a alteração, que ativa ou desativa o restaurante.
   - **Sair**:
     - Encerra a execução do programa.

4. **Opção Inválida**:
   - Se for inserido um número fora das opções ou algo que não seja um número, o sistema exibirá uma mensagem de erro e pedirá para tentar novamente.

## Estrutura do Código

- **`main()`**: Função principal que inicializa o sistema e exibe o menu.
- **`exibir_nome_do_programa()`**: Exibe o título do sistema em ASCII art.
- **`exibir_opcoes()`**: Mostra o menu de opções.
- **`cadastrar_novo_restaurante()`**: Realiza o cadastro de um novo restaurante.
- **`listar_restaurantes()`**: Exibe todos os restaurantes cadastrados.
- **`alternar_estado_do_restaurante()`**: Alterna o status de um restaurante entre ativo e inativo.
- **`escolher_opcao()`**: Lida com a escolha do usuário e chama a função correspondente.
- **`finalizar_app()`**: Finaliza o sistema.
- **`opcao_invalida()`**: Exibe uma mensagem de erro quando a opção escolhida é inválida.

## Personalização e Manutenção

Para adicionar mais funcionalidades, como editar detalhes do restaurante, basta criar novas funções e adicionar uma opção no menu.