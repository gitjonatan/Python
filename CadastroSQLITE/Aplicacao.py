import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import banco as bc



janela = tk.Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()


        janela.mainloop()


    def tela(self):
        self.janela.title('Cadastro de Clientes')
        self.janela.configure(background='grey31')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame1 = tk.Frame(self.janela, bd=4, bg='#BEBEBE',
                            highlightbackground='white', highlightthickness=3)  # borda do frame
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)  # relwidth = largura/altura

        self.frame2 = tk.Frame(self.janela, bd=4, bg='#BEBEBE',
                            highlightbackground='black', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        #Label
        self.lb_nome = tk.Label(self.frame1, text=' Nome',bg='#BEBEBE',fg='black',
                                font=('verdana',8,'bold'))
        self.lb_nome.place(relx=0.01, rely=0.05)

        self.lb_cpf = tk.Label(self.frame1, text=' CPF',bg='#BEBEBE',fg='black',
                                font=('verdana',8,'bold'))
        self.lb_cpf.place(relx=0.01, rely=0.30)

        self.lb_telefone = tk.Label(self.frame1, text=' Telefone', bg='#BEBEBE', fg='black',
                                    font=('verdana', 8, 'bold'))
        self.lb_telefone.place(relx=0.31, rely=0.30)

        # Entry(input)
        self.nome_entry = tk.Entry(self.frame1)
        self.nome_entry.place(relx=0.02, rely=0.17, relwidth=0.6)

        self.cpf_entry = tk.Entry(self.frame1)
        self.cpf_entry.place(relx=0.02, rely=0.42, relwidth=0.2)

        self.telefone_entry = tk.Entry(self.frame1)
        self.telefone_entry.place(relx=0.32, rely=0.42, relwidth=0.3)

        #BOTÕES
        self.bt_adicionar = tk.Button(self.frame1,text='Adicionar',bd=2,bg='#c5cfd3',fg='black',
                                font=('verdana',8,'bold'), command=self.add_cliente)
        self.bt_adicionar.place(relx=0.25,rely=0.70,relwidth=0.1,relheight=0.15)

        self.bt_deletar = tk.Button(self.frame1, text='Deletar', bd=2, bg='#c5cfd3', fg='black',
                                      font=('verdana', 8, 'bold'), command=self.deletar)
        self.bt_deletar.place(relx=0.45, rely=0.70, relwidth=0.1, relheight=0.15)

        self.bt_obter = tk.Button(self.frame1, text='Cadastrados', bd=2, bg='#c5cfd3', fg='black',
                                      font=('verdana', 7, 'bold'),command= self.select_lista)
        self.bt_obter.place(relx=0.65, rely=0.70, relwidth=0.1, relheight=0.15)


    def widgets_frame2(self):
        self.listaEst = ttk.Treeview(self.frame2, height=3, column=("Col1", "col1", "col3"))
        self.listaEst.heading("#0", text="")
        self.listaEst.heading("#1", text="Nome")
        self.listaEst.heading("#2", text="Telefone")
        self.listaEst.heading("#3", text="CPF")

        self.listaEst.column("#0", width=1)
        self.listaEst.column("#1", width=280)
        self.listaEst.column("#2", width=140)
        self.listaEst.column("#3", width=110)

        self.listaEst.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)



    def add_cliente(self):
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cpf = self.cpf_entry.get()

        if self.nome.isalpha() == True:
            if self.nome == '' or self.telefone == '' or self.cpf_entry == '':
                messagebox.showinfo(title='ATENÇÃO', message='Todos os campos são obrigatórios')


            elif self.cpf != '' or self.nome != '' or self.telefone != '':
                bc.gravar_dados(self.cpf,self.nome,self.telefone)
                self.listaEst.insert('', 'end', values=( self.nome,self.telefone, self.cpf))
                self.cpf_entry.delete(0,'end')
                self.nome_entry.delete(0, 'end')
                self.telefone_entry.delete(0, 'end')
        else:
            messagebox.showinfo(title='ATENÇÃO', message='O Nome deve possuir apenas letras!')



    def deletar(self):
        try:
            self.listaEst.selection()
            for n in self.listaEst.selection():
                self.col =self.listaEst.item(n, 'values')

            x = self.col[2:]

            bc.delete(x)
            itemSelecionado = self.listaEst.selection()
            self.listaEst.delete(itemSelecionado)
        except:
            messagebox.showinfo(title='ERRO', message='Nenhum item selecionado')



    def select_lista(self):
        self.listaEst.delete(*self.listaEst.get_children())
        lista = bc.selecionar_tudo()
        for i in lista:
            self.listaEst.insert('', 'end', values=(i[1],i[2],i[0]))



Aplicacao()



