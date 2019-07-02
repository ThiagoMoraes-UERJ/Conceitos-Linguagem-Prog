
from tkinter import *
from urllib.request import * 

vet= []
vet2= []
def limpar(self):
    pass
    

        
def resultado():

    #resultado
    funcnome = nomef.get()  
    x = dadoX.get()
    y = dadoY.get()
    z = dadoZ.get()
    w = dadoW.get()
    

    soma =int(lb4["text"])
    soma = len(vet)
    
    #funcao
    envia = 0  

    soma =int(lb4["text"])
    soma = len(vet)

    if soma > 0 and funcnome != "":
        t = ""
        num_elementos_lista = len(vet)
        for s in range(num_elementos_lista):
            q = vet[s]
            nome = q.split("'")
            nome = nome[0]
            if funcnome == nome:
                q = vet[s]
                nome = q.split("'")
                func = nome[2]
                
                # vet argumentos
                arg = nome[1]
                argumentos = arg.split(",")
                
                while envia != 1:
                #faz requisição
                    req = Request('http://moraestec.com/uerj/transformaOperadores.php?funcao="' + func) #linkdaRespostaPHP
                    resposta = urlopen(req)
                #transforama em string e guarda na variavel res
                    res = str(resposta.read())
                #lê a resposta e separa em arrays separados por " ' " 
                    a = res.split("'")
                # pega o array a[1] que está contido a resposta e guarda na variavel enviar
                    recebe = str(a[1]);
                    recebe = recebe.replace('"' , '')
                    texto1["text"] = recebe
                    inp1 = texto1["text"]
                    inp1 = inp1.replace(" ", "")
                    inp3 = inp1
                    #substituir pelos dados
                    num_elementos_lista = len(argumentos)
                    for h in range(num_elementos_lista):
                        if h == 0:
                          inp3 = inp3.replace(argumentos[h],x)
                          print(inp3)
                        if h == 1:
                          inp3 = inp3.replace(argumentos[h],y)
                          print(inp3)
                        if h == 2:
                          inp3 = inp3.replace(argumentos[h],z)  
                        if h == 3:
                          inp3 = inp3.replace(argumentos[h],w)  
                    print(inp3);
                #faz requisição
                    req = Request('https://moraestec.com/uerj/interpretador.php?funcao="' + inp3); #linkdaRespostaPHP
                    resposta = urlopen(req)
                #transforama em string e guarda na variavel res
                    res = str(resposta.read())
                #lê a resposta e separa em arrays separados por " ' " 
                    a = res.split("'")
                # pega o array a[1] que está contido a resposta e guarda na variavel enviar
                    recebe = str(a[1]);
                    recebe = recebe.replace('"' , '')
                    texto1["text"] = recebe
                    inp2 = texto1["text"]
                    envia = 1
                

                out.delete(0.0,'end')
                tokexpr = "Função: "+ vet2[s] +"\n Parte 1 : "+ inp1 +"\n Parte 2 : "+ inp3 +"\n Parte 3 : "+ inp2 +"\n"
                out.insert(0.0,tokexpr)

                nomef.delete(first=0,last=100)
                dadoX.delete(first=0,last=100)
                dadoY.delete(first=0,last=100)
                dadoZ.delete(first=0,last=100)
                dadoW.delete(first=0,last=100)
               
    else:
        out.delete(0.0,'end')

    

def botao_click1():

    #TOKEN

    #funcao
    envia = 0
    funcnome = nomef.get()  
    x = dadoX.get()
    y = dadoY.get()
    z = dadoZ.get()
    w = dadoW.get()
    

    soma =int(lb4["text"])
    soma = len(vet)

    if soma > 0 and funcnome != "" and  x == "" and y == "" and z == "" and w == "":
        t = ""
        num_elementos_lista = len(vet)
        for s in range(num_elementos_lista):
            q = vet[s]
            nome = q.split("'")
            nome = nome[0]
            if funcnome == nome:
                q = vet[s]
                nome = q.split("'")
                func = nome[2] 
                while envia != 1:
                #faz requisição
                    req = Request('http://moraestec.com/uerj/transformaOperadores.php?funcao="' + func) #linkdaRespostaPHP
                    resposta = urlopen(req)
                #transforama em string e guarda na variavel res
                    res = str(resposta.read())
                #lê a resposta e separa em arrays separados por " ' " 
                    a = res.split("'")
                # pega o array a[1] que está contido a resposta e guarda na variavel enviar
                    recebe = str(a[1]);
                    recebe = recebe.replace('"' , '')
                    texto1["text"] = recebe
                    envia = 1

                out.delete(0.0,'end')
                inp = texto1["text"]
                tokexpr="Função: "+vet2[s]+"\n Parte 1 : "+inp+"\n"
                out.insert(0.0,tokexpr)

                nomef.delete(first=0,last=100)
                dadoX.delete(first=0,last=100)
                dadoY.delete(first=0,last=100)
                dadoZ.delete(first=0,last=100)
                dadoW.delete(first=0,last=100)
               
    else:
        out.delete(0.0,'end')
   

def botao_click2():

    #SALVAR NA MEMÓRIA
    funcnome = nomefunc.get()  
    x = dado1.get()
    y = dado2.get()
    z = dado3.get()
    w = dado4.get()
    funccorpo = dado9.get()
    
    #pega o indice guardado na label
    soma =int(lb4["text"])
    soma = len(vet)
    verifica = 0
    if soma >= 1:
        i = 0
        num_elementos_lista = len(vet)
        for t in range(num_elementos_lista):
            q = vet[t]
            nome = q.split("'")
            nome = nome[0]
            if funcnome == nome:
                verifica = 1
            i = i + 1
            
    if funcnome != "" and funccorpo != "" and ( x != "" or y != "" or z != "" or w != "") and (verifica == 0):

        a = ""
        inp = funcnome + "'"
        if x != "":
            a = x
            inp = inp + x
        if y != "":
            if x == "":
                a = y
                inp = inp + y
            else:
                a = a + "," + y
                inp = inp + "," + y
        if z != "":
            if y == "" and x == "" :
                a = z
                inp = inp + z
            else:
                a = a + "," + z
                inp = inp + "," + z
        if w != "":
            if z == "" and y == "" and x == "":
                a = w
                inp = inp + w
            else:
                a = a + "," + w
                inp = inp + "," + w
        inp = inp + "'" + funccorpo
        
          
        inp2 = nomefunc.get()+"("+ a +") ="+dado9.get()
        #guarda função na memória
        vet.append(inp)
        vet2.append(inp2)
        #atribui um novo valor ao campo texto com o indice +1 para saber o tamanho do vetor adquirido
        lb4["text"] = str(soma + 1)

        nomefunc.delete(first=0,last=100)
        dado1.delete(first=0,last=100)
        dado2.delete(first=0,last=100)
        dado3.delete(first=0,last=100)
        dado4.delete(first=0,last=100)
        dado9.delete(first=0,last=100)

    if soma > 0 or (funcnome != "" and funccorpo != "" and ( x != "" or y != "" or z != "" or w != "")) and (verifica == 0):
        t = ""
        num_elementos_lista = len(vet)
        for s in range(num_elementos_lista):
            t = t + "\n" + str(vet2[s])
            funCriadas["text"] = t
            
    
   


########## JANELA E SUAS CONFIGURAÇÕES ######################
        
janela = Tk()
janela.title("Interface")
janela.geometry("1000x400+100+100")
titulo = Label(janela , text = "I N T E R F A C E    P Y T H O N ")
titulo.place(x=5, y=2)

############### CRIAR FUNÇÃO ################################

texto0 = Label(janela , text = "Criar Func:")
texto0.place(x=5, y=30)
# Nome da função
nomefunc = Entry(janela)
nomefunc.place(x=70, y=30)

nomefu = Label(janela , text = "(")
nomefu.place(x=200, y=30)

nomefu = Label(janela , text = "1º")
nomefu.place(x=270, y=10)
dado1 = Entry(janela)
dado1.place(x=215 , y=30)

texto1 = Label(janela , text = ",")
texto1.place(x=345, y=30)

nomefu = Label(janela , text = "2º")
nomefu.place(x=410, y=10)
dado2 = Entry(janela)
dado2.place(x=355 , y=30)

texto2 = Label(janela , text = ",")
texto2.place(x=480, y=30)

nomefu = Label(janela , text = "3º")
nomefu.place(x=545, y=10)
dado3 = Entry(janela)
dado3.place(x=490 , y=30)

texto3 = Label(janela , text = ",")
texto3.place(x=610, y=30)

nomefu = Label(janela , text = "4º")
nomefu.place(x=675, y=10)
dado4 = Entry(janela)
dado4.place(x=620, y=30)

texto4 = Label(janela , text = ")")
texto4.place(x=740, y=30)

texto9 = Label(janela , text = "=")
texto9.place(x=750, y=30)

dado9 = Entry(janela)
dado9.place(x=765 , y=30)

####################### CALCULAR FUNÇÃO ###################################

texto0 = Label(janela , text = "Calc Func:")
texto0.place(x=5, y=60)

#nome da função
nomef = Entry(janela)
nomef.place(x=70, y=60)

t = Label(janela , text = "(")
t.place(x=200, y=60)

dadoX = Entry(janela)
dadoX.place(x=215 , y=60)

texto1 = Label(janela , text = ",")
texto1.place(x=345, y=60)

dadoY = Entry(janela)
dadoY.place(x=355 , y=60)

texto2 = Label(janela , text = ",")
texto2.place(x=480, y=60)

dadoZ = Entry(janela)
dadoZ.place(x=490 , y=60)

texto3 = Label(janela , text = ",")
texto3.place(x=610, y=60)

dadoW = Entry(janela)
dadoW.place(x=620, y=60)

texto4 = Label(janela , text = ")")
texto4.place(x=740, y=60)


##################### TOKEN ###################################

Tokenlabel=Label(janela,text='Tokens:')
Tokenlabel.place(x=25, y=100)
out=Text(janela,width=85,height=10,wrap='word')
out.place(x=75 , y=100)
##################### FUNÇOES CRIADAS #########################
funCriada = Label(janela , text = "Funções:")
funCriada.place(x=800, y=90)

funCriadas = Label(janela , text = "")
funCriadas.place(x=810, y=110)


# mostrando o resultado
texto11 = Label(janela , text = "Resultado")
texto11.place(x=340, y=350)
texto1 = Label(janela , text = "0")
texto1.place(x=400, y=350)

texto11 = Label(janela , text = "Numero de Funções Armazenadas")
texto11.place(x=600, y=300)
lb4 = Label(janela , text = "0")
lb4.place(x=800, y=300)

#criando o botão e chamando a função criada acima
botaosalv = Button(janela, width=20, text="Criar Função" , command = botao_click2)
botaosalv.place(x=105, y=300)
botaotoken = Button(janela, width=20, text="Tokenizar", command = botao_click1)
botaotoken.place(x=240, y=300)
botao = Button(janela, width=20, text="Calcular", command = resultado)
botao.place(x=380, y=300)

#fim
janela.mainloop()
