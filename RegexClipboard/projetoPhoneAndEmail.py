#extrator de números de telefone e de endereços de email
#padrões aceitaveis de telefones: 0800 729 0721/ (22) 324 43567

import pyperclip, re


#regex para telefone
foneRegex = re.compile(r'''(
(\d{2,4}|\(\d{2}\))? # código de área
(\s|-|\.)+ # separador
(\d{3}) # primeiros 3 dígitos /////
(\s|-|\.) # separador /////
(\d{2,}) # últimos 4 dígitos
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extensão
)''', re.VERBOSE)


#regex para endereço de email
emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+ # nome do usuário
 @ # símbolo @
 [a-zA-Z0-9.-]+ # nome do domínio
(\.[a-zA-Z]{2,4}) # ponto seguido de outros caracteres
)''', re.VERBOSE)

#Encontra as correspodências no texto do clipboard
texto = str(pyperclip.paste())
lista = []
for grupos in foneRegex.findall(texto):
    foneNum = '-'.join([grupos[1], grupos[3], grupos[5]])
    if grupos[8] != '':
        foneNum += ' x' + grupos[8]
    lista.append(foneNum)
for grupos in emailRegex.findall(texto):
    lista.append(grupos[0])

# Copia os resultados para o clipboard.
if len(lista) > 0:
    pyperclip.copy('\n'.join(lista))
    print('Copiado para o clipboard:')
    print('\n'.join(lista))
else:
    print('Não foram detectados números ou emails')