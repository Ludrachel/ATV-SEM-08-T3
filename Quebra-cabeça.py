# A função "remover_acentos" recebe como parâmetro um "texto" e , utilizando funções
#importadas retorna uma versão do texto original sem caracteres acentuados.
def remover_acentos(texto):
    from unicodedata import normalize
    return normalize('NFKD',texto).encode('ASCII','ignore').decode('ASCII')

# A função "horoscopo" recebe como parâmetro um "signo_desejado" e , utilizando funções
# importadas retorna o signo da pessoa mais um texto sobre aquele signo
def horoscopo(signo_desejado):
    import urllib.request,ssl
    signo_formatado = remover_acentos(signo_desejado).lower()
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    contexto_ssl = ssl.create_default_context()
    contexto_ssl.check_hostname = False
    contexto_ssl.verify_mode = ssl.CERT_NONE

    resposta = urllib.request.urlopen(requisicao, context=contexto_ssl)
    pagina = resposta.read().decode('utf-8')
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '<a class="webshare-link">compartilhar</a>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final,inicio)

    return signo_desejado + ' : ' + pagina[inicio:final].strip()

# A função "signo" recebe como parâmetro o "dia" e o "mes" de uma determinada pessoa
# e oferece condições , caso a condição for verdadeira de acordo com o parâmetro entao
# a função é executada retornando o resultado estabelecido pela condição.
def signo(dia,mes):
    if mes ==3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sargitário'
    if mes == 12:
        return 'Sargitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'
    
# A função "separar_data" recebe como parâmetro "dma" que representa o dia , o mes e o ano de
# uma determinada pessoa , assim essa funçao calcula e  retorna a data separada em formato ddmmaaaa. 
def separar_data(dma):
    a = dma % 10000
    dma //= 10000
    m = dma % 100
    dma //=100
    d = dma
    return d, m, a

# A funçao "main" recebe a entrada de dados onde a variável "nascimento" recebe ,convertido
# para inteiro a mensagem que é feita pelo teclado, logo em seguida faz o processamento
# colocando as funções dentro de variáveis para na hora da saída de dados chamar somente a função final.
def main():
    #Entrada de dados
    nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))
    #Processamento
    dia,mes,_ = separar_data(nascimento)
    meu_signo = signo(dia,mes)
    horoscopo_de_hoje = horoscopo(meu_signo)
    #saída de dados
    print(horoscopo_de_hoje)

# A função "main" só será executada se tudo isso for verdade
if __name__ == '__main__':
    main()
