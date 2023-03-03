from tkinter import *
from tkinter import font
from tkinter import ttk

####cores##
co0 = '#f0f3f5' #Preta
co1 = '#feffff' #branca
co2 = '#4fa882' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra
co5 = '#e06636' # profit
co6 = '#038cfc' #azul
co7 = '#ef5350' #vermelha
co8 = '#263238' # + verde
co9 = '#e9edf5' #skyblue

#criando a interface com tamanho fixo
janela= Tk()
janela.title('Tabuada')
janela.geometry('400x400')
janela.configure(background=co8)
janela.resizable(width=FALSE, height=FALSE ) #Impede alterar o tamanho da janela


app_nome = Label(janela, text='Insira apenas números inteiros', anchor=NW, font=('Ivy 13 bold'), bg=co2,fg=co1, relief='flat')
app_nome.place(x=10, y=20)

x=0
y=0

def inserir():
    x =int(e_x.get())
    y =int (e_y.get())
    i = 1
    multiplica = 0
    while i <= x:
        multiplica += y
        i = i + 1
        l_produto['text']= multiplica


l_x = Label(janela, text='Valor 1', anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_x.place(x=10, y=60)
e_x = Entry(janela, width=20,justify='left', relief='solid')
e_x.place(x=80, y=60)

l_y = Label(janela, text='Valor 2', anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_y.place(x=10, y=80)
e_y = Entry(janela, width=20,justify='left', relief='solid')
e_y.place(x=80, y=80)

#Botão Atualizar
b_atualizar = Button(janela,command= inserir, text='Atualizar',width=10, font=('Ivy 9 bold'), bg=co2,fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=150, y=340)

#label_produto
l_produto = Label(janela, text='    ', anchor=NW, font=('Ivy 10 bold'), bg=co8,fg=co1, relief='flat')
l_produto.place(x=230, y=70)



janela.mainloop()