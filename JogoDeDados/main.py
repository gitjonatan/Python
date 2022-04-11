import tkinter as tk
from PIL import ImageTk, Image
import random


valor_minimo = 1
valor_maximo = 6
janelaRaiz = tk.Tk()
janelaRaiz.geometry('650x450')
janelaRaiz.resizable(width=0, height=0)
janelaRaiz.configure(bg='white')
res = 'Clique em jogar'


def tela(janelaRaiz):
    mostrarImagem()

    botao = tk.Button(janelaRaiz, text='JOGAR', height=2,
                           width=9, command= mostrarImagem)
    botao.place(x=300, y=350)

    lbl = tk.Label(janelaRaiz, text='Jogador', bg='white', fg='red', font=('', '16'), relief='raised')
    lbl.place(relx=0.27, rely=0.2)
    lbl2 = tk.Label(janelaRaiz, text='Computador', bg='white', fg='red', font=('', '16'), relief='raised')
    lbl2.place(relx=0.6, rely=0.2)




texto = tk.Label(janelaRaiz, text=res,bg='white', fg='black', font=('Times New Roman', 20))
texto.pack()


def res_texto(res):
    texto.config(text=res)


def mostrarImagem():
    jogador = gerarValorDoDado()
    computador = gerarValorDoDado()
    path = ''
    path2 = ''

    if jogador:
        if jogador == 1:
            path = '1.png'
        elif jogador == 2:
            path = '2.png'
        elif jogador == 3:
            path = '3.png'
        elif jogador == 4:
            path = '4.png'
        elif jogador == 5:
            path = '5.png'
        else:
            path = '6.png'


        img = Image.open('../JogoDeDados/imagens/'+ path)
        minhaImagem = ImageTk.PhotoImage(img)
        lbl = tk.Label(janelaRaiz, image=minhaImagem,
                            compound=tk.TOP)
        lbl.image = minhaImagem
        lbl.place(relx=0.25, rely=0.3)

    if computador:
        if computador == 1:
            path2 = '1.png'
        elif computador == 2:
            path2 = '2.png'
        elif computador == 3:
            path2 = '3.png'
        elif computador == 4:
            path2 = '4.png'
        elif computador == 5:
            path2 = '5.png'
        else:
            path2 = '6.png'


        img = Image.open('../JogoDeDados/imagens/'+ path2)
        minhaImagem = ImageTk.PhotoImage(img)
        lbl = tk.Label(janelaRaiz, image=minhaImagem,
                            compound=tk.TOP)
        lbl.image = minhaImagem
        lbl.place(relx=0.6, rely=0.3)


    if jogador > computador:
        r = 'Você Venceu!'
        res_texto(r)
    elif jogador < computador:
        r = 'Computador Venceu!'
        res_texto(r)
    else:
        r = 'Empatou'
        res_texto(r)



def resultado(jogador, computador):
    result = ''
    if jogador>computador:
        result = 'Voce venceu!'


    else:
        result = 'Computador venceu'
        return result


def gerarValorDoDado():
    return random.randint(valor_minimo, valor_maximo)



tela(janelaRaiz)
janelaRaiz.mainloop()

