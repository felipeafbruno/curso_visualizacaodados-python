entrada = open('./visualização_dados_python/dados/16s_bacteria.fasta').read()
saida = open('./visualização_dados_python/html/bacteria.html', 'w')

cont = {}

# Montatando par dinucleotídeo e cada um vai valer 0
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

# contagem de dinucleotídeo com o arquivo 16s_bacteria.fasta('entrada')
entrada = entrada.replace('\n', '')
for k in range(0, len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

# HTML que contem uma série de tags <div> pintadas com cores representado a quantidade de cada para de dinucleotídeo
'''
transparencia é utilizada como o alfa no rgba 
de modo que o valor de cada um dos pares é dividido 
pelo valor do par com maior quantidade
'''
# por fim dentro do arquivo de saida que é um html é escrita cada div com sua respectiva transparência
i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='text-align:center; color:#fff; width:100px; border:1px solid #111; \
        height:100px; float:left; background-color:rgba(0,0,255,"+str(transparencia)+")'>"+k+"</div>")
    if i%4 == 0:
        saida.write('<div style="clear:both"></div>')
    i += 1

saida.close()

entrada = open('./visualização_dados_python/dados/18s_humano.fasta').read()
saida = open('./visualização_dados_python/html/humano.html', 'w')

cont = {}

# Montatando par dinucleotídeo e cada um vai valer 0
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

# contagem de dinucleotídeo com o arquivo 16s_bacteria.fasta('entrada')
entrada = entrada.replace('\n', '')
for k in range(0, len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

# HTML que contem uma série de tags <div> pintadas com cores representado a quantidade de cada para de dinucleotídeo
'''
transparencia é utilizada como o alfa no rgba 
de modo que o valor de cada um dos pares é dividido 
pelo valor do par com maior quantidade
'''
# por fim dentro do arquivo de saida que é um html é escrita cada div com sua respectiva transparência
i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='text-align:center; color:#fff; width:100px; border:1px solid #111; \
        height:100px; float:left; background-color:rgba(0,0,255,"+str(transparencia)+")'>"+k+"</div>")
    if i%4 == 0:
        saida.write('<div style="clear:both"></div>')
    i += 1

saida.close()
