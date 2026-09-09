class Solution:

    def encode(self, strs: List[str]) -> str:

        qtd_palavra = list()
        for palavra in strs:
            qtd_palavra.append(len(palavra))
        
        qtd_assinatura = ",".join(str(n) for n in qtd_palavra)

        qtd_assinatura_count = len(qtd_assinatura)
        qtd_assinatura_count = str(qtd_assinatura_count)
        qtd_assinatura_count = qtd_assinatura_count + "_"

        encoding = "".join(strs)

        encoded_string = qtd_assinatura_count + qtd_assinatura + encoding

        return encoded_string

    def decode(self, s: str) -> List[str]:

        acumulador = list()
        contador = 0
        while s[contador] != "_":
            acumulador.append(s[contador])
            contador += 1

        tirar = len(acumulador) + 1

        acumulador = int("".join(acumulador))
        
        s = s[tirar:]

        aux = list()
        for i in range(0, acumulador):
            aux.append(s[i])

        cabecalho_texto = "".join(aux)
        if cabecalho_texto == "":
            tamanhos = []
        else:
            partes = cabecalho_texto.split(",")
            tamanhos = [int(p) for p in partes]

        s = s[acumulador:]

        resultado = list()
        inicio = 0
        for tamanho in tamanhos:
            pedaco = s[inicio:inicio + tamanho]
            resultado.append(pedaco)
            inicio += tamanho

        decoded_strs = resultado

        return decoded_strs


