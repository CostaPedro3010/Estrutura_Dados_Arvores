class Nodo:
    def __init__(self, chave, pai=None):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.pai = pai
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if not self.raiz:
            self.raiz = Nodo(chave)
        else:
            self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, nodo, chave):
        if not nodo:
            return Nodo(chave)
        elif chave < nodo.chave:
            nodo.esquerda = self._inserir(nodo.esquerda, chave)
            nodo.esquerda.pai = nodo
        else:
            nodo.direita = self._inserir(nodo.direita, chave)
            nodo.direita.pai = nodo

        nodo.altura = 1 + max(self.obter_altura(nodo.esquerda), self.obter_altura(nodo.direita))
        balanceamento = self.obter_balanceamento(nodo)

        if balanceamento > 1 and chave < nodo.esquerda.chave:
            return self.rotacao_direita(nodo)
        if balanceamento < -1 and chave > nodo.direita.chave:
            return self.rotacao_esquerda(nodo)
        if balanceamento > 1 and chave > nodo.esquerda.chave:
            nodo.esquerda = self.rotacao_esquerda(nodo.esquerda)
            return self.rotacao_direita(nodo)
        if balanceamento < -1 and chave < nodo.direita.chave:
            nodo.direita = self.rotacao_direita(nodo.direita)
            return self.rotacao_esquerda(nodo)

        return nodo

    def excluir(self, chave):
        if self.raiz:
            self.raiz = self._excluir(self.raiz, chave)

    def _excluir(self, nodo, chave):
        if not nodo:
            return nodo
        elif chave < nodo.chave:
            nodo.esquerda = self._excluir(nodo.esquerda, chave)
        elif chave > nodo.chave:
            nodo.direita = self._excluir(nodo.direita, chave)
        else:
            if not nodo.esquerda:
                return nodo.direita
            elif not nodo.direita:
                return nodo.esquerda
            temp = self.obter_menor_valor_nodo(nodo.direita)
            nodo.chave = temp.chave
            nodo.direita = self._excluir(nodo.direita, temp.chave)

        nodo.altura = 1 + max(self.obter_altura(nodo.esquerda), self.obter_altura(nodo.direita))
        balanceamento = self.obter_balanceamento(nodo)

        if balanceamento > 1 and self.obter_balanceamento(nodo.esquerda) >= 0:
            return self.rotacao_direita(nodo)
        if balanceamento > 1 and self.obter_balanceamento(nodo.esquerda) < 0:
            nodo.esquerda = self.rotacao_esquerda(nodo.esquerda)
            return self.rotacao_direita(nodo)
        if balanceamento < -1 and self.obter_balanceamento(nodo.direita) <= 0:
            return self.rotacao_esquerda(nodo)
        if balanceamento < -1 and self.obter_balanceamento(nodo.direita) > 0:
            nodo.direita = self.rotacao_direita(nodo.direita)
            return self.rotacao_esquerda(nodo)

        return nodo

    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y

    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y

    def obter_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obter_balanceamento(self, nodo):
        if not nodo:
            return 0
        return self.obter_altura(nodo.esquerda) - self.obter_altura(nodo.direita)

    def obter_menor_valor_nodo(self, nodo):
        if nodo is None or nodo.esquerda is None:
            return nodo
        return self.obter_menor_valor_nodo(nodo.esquerda)

    def imprimir_arvore(self):
        if self.raiz:
            self._imprimir_arvore(self.raiz)

    def _imprimir_arvore(self, nodo, nivel=0):
        if nodo is not None:
            self._imprimir_arvore(nodo.direita, nivel + 1)
            print(' ' * 4 * nivel + '->', nodo.chave)
            self._imprimir_arvore(nodo.esquerda, nivel + 1)

def main():
    arvore = ArvoreAVL()
    while True:
        print("\nMenu:")
        print("1. Inserir elemento")
        print("2. Excluir elemento")
        print("3. Mostrar árvore")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            chave = int(input("Digite o valor a ser inserido: "))
            arvore.inserir(chave)
        elif escolha == '2':
            chave = int(input("Digite o valor a ser excluído: "))
            arvore.excluir(chave)
        elif escolha == '3':
            arvore.imprimir_arvore()
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
