from tkinter import *
from tkinter import ttk


# definição da Calculadora de serie D
def csd_open():
    #setup da janela
    csd_window = Toplevel()
    csd_window.title('Calculadora de Serie D')
    csd_window.geometry('400x200')

    valor = StringVar()
    num_nota = IntVar()
    valor_final = StringVar()
    num_final = IntVar()
    notas_somadas = StringVar()

    #definição da função Submit para realizar os calculos ao pressionar o botao
    def submit():
        numero_atual = IntVar()
        #auto incrementação do numero da nota
        if int(num_final.get()) == 0:
            numero_atual = int(num_nota.get()) + 1
            num_final.set(int(numero_atual))
        else:
            numero_atual = int(numero_atual.get()) +1
            num_final.set(int(numero_atual))
        
        #realização da soma dos valores
        valor_soma = float(valor_final.get())+float(valor.get())
        valor_final.set(valor_soma)

        
        
        #retorno dos valores somados concatenados
        lista_somadas = notas_somadas.get()+' + '+valor.get()
        notas_somadas.set(lista_somadas)
        

        
    #inputs e suas GUI
    csd_title_lbl = Label(csd_window,text='Calculadora de Serie D').grid(column=0,row=0)
    num_lbl = Label(csd_window,text='Número da primeira nota: ').grid(column=0,row=1)
    num_entry = Entry(csd_window,textvariable=num_nota).grid(column=1,row=1)
    valor_lbl = Label(csd_window,text='Valor: ').grid(column=0,row=2)
    valor_entry = Entry(csd_window,textvariable=valor).grid(column=1,row=2)
    submit_btn = Button(csd_window,text='Submeter',command=lambda:submit()).grid(column=2,row=2)

    #output
    notas_lbl0 = Label(csd_window,text='Somatório das notas:').grid(column=0,row=4)
    notas_lbl1 = Label(csd_window,textvariable=num_nota).grid(column=1,row=4)
    notas_lbl2 = Label(csd_window,text=' a ').grid(column=2,row=4)
    notas_lbl3 = Label(csd_window,textvariable=num_final).grid(column=3,row=4)
    vfinal_lbl0 = Label(csd_window,text='Valor final: ').grid(column=0,row=5)
    vfinal_lbl = Label(csd_window,textvariable=valor_final).grid(column=2,row=5)
    nsomadas_lbl0 = Label(csd_window,text='Notas somadas: []').grid(column=0,row=6)
    nsomadas_lbl = Label(csd_window,textvariable=notas_somadas).grid(column=0,columnspan=12,row=6)

    csd_window.mainloop()

#definição da Calculadora de Imposto Retido na Nota
def ret():
    #setup da janela
    ret_window = Toplevel()
    ret_window.title('Calculadora de Imposto Retido na Nota')
    ret_window.geometry('400x200')

    #GUI
    ret_title_lbl = Label(ret_window,text='Calculadora de Imposto Retido na Nota').grid(column=0,row=0)
    serv_lbl = Label(ret_window,text='Valor do Serviço: ').grid(column=0,row=1)
    serv_entry = Entry(ret_window).grid(column=1,row=1)

    imp_lbl = Label(ret_window, text='Imposto').grid(column=0,row=2)
    ali_lbl = Label(ret_window, text='Alíquota').grid(column=1,row=2)
    ret_lbl = Label(ret_window, text='Retenção').grid(column=2,row=2)

    pis_lbl = Label(ret_window,text='PISS').grid(column=0,row=3)
    pis_ali = Entry(ret_window).grid(column=1,row=3)
    
    cssl_lbl = Label(ret_window,text='CSSL').grid(column=0,row=4)
    cssl_ali = Entry(ret_window).grid(column=1,row=4)

    inss_lbl = Label(ret_window,text='INSS').grid(column=0,row=5)
    inss_ali = Entry(ret_window).grid(column=1,row=5)

    irrf_lbl = Label(ret_window,text='IRRF').grid(column=0,row=6)
    irrf_ali = Entry(ret_window).grid(column=1,row=6)

    cofins_lbl = Label(ret_window,text='COFINS').grid(column=0,row=7)
    cofins_ali = Entry(ret_window).grid(column=1,row=7)

    vfinal = Label(ret_window,text='Valor final da Nota: ').grid(column=0,row=8)

    ret_window.mainloop()

# Main window definition
window = Tk()
window.title('teste')
window.geometry('400x400')
mainframe = Frame(window,padx=10,pady=5).pack()

lbl1 = Label(mainframe,text='Olá, selecione uma ferramenta: ',justify='center').pack()
sdc_btn = Button(mainframe,text='Calculadora de Série D',command=csd_open).pack()
ret_btn = Button(mainframe,text='Calculadora de Imposto Retido na Nota',command=ret).pack()


window.mainloop()
