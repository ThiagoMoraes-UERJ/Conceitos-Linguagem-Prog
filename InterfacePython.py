
#biblioteca tk
from tkinter import *

#função 
def botao_click():

    #teste para o click na cmd
    #print("click")
    #botao
    #botao["text"] = "clicou"

    #funcao
    dado5["text"] = dado1.get()
    dado6["text"] = dado2.get()
    dado7["text"] = dado3.get()
    dado8["text"] = dado4.get()
    
    #somar os dados
    soma = float(dado1.get())+float(dado2.get())+float(dado3.get())+float(dado4.get())
    #resultado
    texto1["text"] = soma

    
def botao_click1():

    #gabriel
    #-------------------------------------------------------------------------------------
    out.delete(0.0,'end')
    inp="função("+dado1.get()+","+dado2.get()+","+dado3.get()+","+dado4.get()+")"+"="+dado9.get()
    tokexpr=inp+"\n"
    out.insert(0.0,tokexpr)
    #-------------------------------------------------------------------------------------

def botao_click2():
    
    #pega os dados
    x = dado1.get()
    y = dado2.get()
    z = dado3.get()
    w = dado4.get()
    func = dado9.get()

    #criar func que salva argumento na memória

    vet= []
    inp="função("+dado1.get()+","+dado2.get()+","+dado3.get()+","+dado4.get()+")"+"="+dado9.get()
    #pega o indice guardado na label
    soma =int(lb4["text"])
    #guarda função na memória 
    vet.append(inp)
    #atribui um novo valor ao campo texto com o indice +1 para saber o tamanho do vetor adquirido 
    lb4["text"] = str(soma + 1)
    
    
    
    

#cria o objeto janela e suas configurações
janela = Tk()
janela.title("Interface")
 
janela.geometry("800x400+100+100")
                  #L X A + E + T

#cria uma label de titulo
titulo = Label(janela , text = "projeto interface").pack()


#criando os espaçamentos para a colocação dos dados acima 
texto0 = Label(janela , text = "função (")
texto0.place(x=25, y=50)

dado1 = Entry(janela)
dado1.place(x=78 , y=50)

texto1 = Label(janela , text = ",")
texto1.place(x=205, y=50)

dado2 = Entry(janela)
dado2.place(x=218 , y=50)

texto2 = Label(janela , text = ",")
texto2.place(x=345, y=50)

dado3 = Entry(janela)
dado3.place(x=358 , y=50)

texto3 = Label(janela , text = ",")
texto3.place(x=485, y=50)

dado4 = Entry(janela)
dado4.place(x=500 , y=50)

texto4 = Label(janela , text = ")")
texto4.place(x=627, y=50)

texto9 = Label(janela , text = "=")
texto9.place(x=635, y=50)

dado9 = Entry(janela)
dado9.place(x=653 , y=50)

#gabriel
#------------------------------------------------------
Tokenlabel=Label(janela,text='Tokens:')
Tokenlabel.place(x=25, y=100)
out=Text(janela,width=25,height=10,wrap='word')
out.place(x=75 , y=100)
#------------------------------------------------------


#criando os espaçamentos para a alocação dos dados abaixo 
texto0 = Label(janela , text = "função (")
texto0.place(x=25, y=350)

dado5 = Label(janela , text = "0")
dado5.place(x=80 , y=350)

texto5 = Label(janela , text = ",")
texto5.place(x=110, y=350)

dado6 = Label(janela , text = "0")
dado6.place(x=120 , y=350)

texto6 = Label(janela , text = ",")
texto6.place(x=150, y=350)

dado7 = Label(janela , text = "0")
dado7.place(x=160 , y=350)

texto7 = Label(janela , text = ",")
texto7.place(x=190, y=350)

dado8 = Label(janela , text = "0")
dado8.place(x=200 , y=350)

texto8 = Label(janela , text = ")")
texto8.place(x=230, y=350)

# mostrando o resultado
texto11 = Label(janela , text = "Resultado")
texto11.place(x=340, y=350)
texto1 = Label(janela , text = "0")
texto1.place(x=400, y=350)

lb4 = Label(janela , text = "0")
lb4.place(x=420, y=350)

#criando o botão e chamando a função criada acima
botaosalv = Button(janela, width=20, text="Salvar" , command = botao_click2)
botaosalv.place(x=105, y=300)
botaotoken = Button(janela, width=20, text="Tokenizar", command = botao_click1)
botaotoken.place(x=240, y=300)
botao = Button(janela, width=20, text="Calcular", command = botao_click)
botao.place(x=380, y=300)

#fim
janela.mainloop()
