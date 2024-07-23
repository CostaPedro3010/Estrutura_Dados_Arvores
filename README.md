# Árvore AVL em Python

Este projeto implementa uma árvore AVL (Árvore Binária de Busca Auto-Balanceada) em Python. A árvore AVL é uma estrutura de dados que mantém a árvore balanceada após cada inserção e remoção, garantindo uma busca eficiente.

## Funcionalidades

- Inserção de nós
- Remoção de nós
- Impressão da árvore
- Balanceamento automático usando rotações

## Estrutura do Projeto

- `avl_tree.py`: Contém a implementação da árvore AVL e do nó.
- `README.md`: Este arquivo, contendo informações sobre o projeto.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. Navegue até o diretório onde o arquivo `avl_tree.py` está localizado.
4. Execute o arquivo `avl_tree.py` com o comando:

```bash
python avl_tree.py
```

## Menu do Programa
Ao executar o programa, você verá um menu com as seguintes opções:

Inserir elemento: Insira um novo valor na árvore AVL.

Excluir elemento: Exclua um valor existente da árvore AVL.

Mostrar árvore: Exiba a estrutura atual da árvore AVL.

Sair: Encerre o programa.

##
## Exemplo de Uso


Ao escolher a opção "Inserir elemento", você será solicitado a digitar o valor a ser inserido. O programa irá automaticamente balancear a árvore se necessário.

Menu:
1. Inserir elemento
2. Excluir elemento
3. Mostrar árvore
4. Sair
Escolha uma opção: 1
5. Digite o valor a ser inserido: 10


Ao escolher a opção "Mostrar árvore", a estrutura da árvore será exibida no console:

        -> 20
    -> 10
        -> 5
