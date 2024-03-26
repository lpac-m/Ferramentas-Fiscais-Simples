from tkinter import *
from tkinter import ttk


# definição da Calculadora de serie D
def csd_open():
    #setup da janela
    csd_window = Toplevel()
    csd_window.title('Calculadora de Serie D')
    csd_window.geometry('400x200')

    #declaração das variaveis
    nts_somadas = []
    valor = StringVar()
    num_nota = IntVar()
    notas_count=IntVar()
    valor_final = StringVar()
    num_final = IntVar()
    notas_somadas = StringVar()

    #definição da função Submit para realizar os calculos ao pressionar o botao
    def submit(event=None):
        
        #auto incrementação do numero da nota
        notas_count.set(notas_count.get()+1)
        num_final.set(num_nota.get()+notas_count.get())
            
        
        #realização da soma dos valores
        if valor_final.get() == '':
            valor_final.set(float(valor.get()))
            nts_somadas.append(valor.get())
        else:
            valor_soma = float(valor_final.get()) + float(valor.get())
            valor_final.set('{number:.{digits}f}'.format(number=valor_soma, digits=2))
            nts_somadas.append(valor.get())

        

        #retorno dos valores somados concatenados
        notas_somadas.set(nts_somadas)
        #limpar a caixa de Entry ao finalizar o cálculo
        valor_entry.delete(0,'end')

        
    #inputs e suas GUI
    csd_title_lbl = Label(csd_window,text='Calculadora de Serie D').grid(column=0,row=0)
    num_lbl = Label(csd_window,text='Número da primeira nota: ').grid(column=0,row=1)
    num_entry = Entry(csd_window,textvariable=num_nota).grid(column=1,row=1)
    valor_lbl = Label(csd_window,text='Valor: ').grid(column=0,row=2)
    valor_entry = Entry(csd_window,textvariable=valor)
    valor_entry.grid(column=1,row=2)
    valor_entry.focus_set()
    submit_btn = Button(csd_window,text='Submeter',command=lambda:submit()).grid(column=2,row=2)

    #output
    notas_lbl0 = Label(csd_window,text='Somatório das notas:').grid(column=0,row=4)
    notas_lbl1 = Label(csd_window,textvariable=num_nota).grid(column=1,row=4)
    notas_lbl2 = Label(csd_window,text=' a ').grid(column=2,row=4)
    notas_lbl3 = Label(csd_window,textvariable=num_final).grid(column=3,row=4)
    vfinal_lbl0 = Label(csd_window,text='Valor final: ').grid(column=0,row=5)
    vfinal_lbl = Label(csd_window,textvariable=valor_final).grid(column=2,row=5)
    nsomadas_lbl0 = Label(csd_window,text='Notas somadas: ').grid(column=0,row=6)
    nsomadas_lbl = Label(csd_window,textvariable=notas_somadas).grid(column=0,columnspan=12,row=6)

    valor_entry.bind('<Return>',submit)
    csd_window.mainloop()

#definição da Calculadora de Imposto Retido na Nota
def ret():
    #setup da janela
    ret_window = Toplevel()
    ret_window.title('Calculadora de Imposto Retido na Nota')
    ret_window.geometry('500x300')

    #declaração das variáveis
    serv_valor = DoubleVar()
    pis_ali = DoubleVar()
    pis_ret = DoubleVar()
    cssl_ali = DoubleVar()
    cssl_ret = DoubleVar()
    inss_ali = DoubleVar()
    inss_ret = DoubleVar()
    irrf_ali = DoubleVar()
    irrf_ret = DoubleVar()
    cofins_ali = DoubleVar()
    cofins_ret = DoubleVar()
    vfinal = DoubleVar()


    #GUI
    ret_title_lbl = Label(ret_window,text='Calculadora de Imposto Retido na Nota').grid(column=0,row=0)
    serv_lbl = Label(ret_window,text='Valor do Serviço: ').grid(column=0,row=1)
    serv_entry = Entry(ret_window,textvariable=serv_valor)
    serv_entry.grid(column=1,row=1)
    serv_entry.focus_set()

    imp_lbl = Label(ret_window, text='Imposto').grid(column=0,row=2)
    ali_lbl = Label(ret_window, text='Alíquota').grid(column=1,row=2)
    ret_lbl = Label(ret_window, text='Retenção').grid(column=2,row=2)

    pis_lbl = Label(ret_window,text='PISS').grid(column=0,row=3)
    pis_entry = Entry(ret_window,textvariable=pis_ali).grid(column=1,row=3)
    pis_show = Label(ret_window, textvariable=pis_ret).grid(column=2,row=3)
    
    cssl_lbl = Label(ret_window,text='CSSL').grid(column=0,row=4)
    cssl_entry = Entry(ret_window,textvariable=cssl_ali).grid(column=1,row=4)
    cssl_show = Label(ret_window, textvariable=cssl_ret).grid(column=2,row=4)

    inss_lbl = Label(ret_window,text='INSS').grid(column=0,row=5)
    inss_entry = Entry(ret_window,textvariable=inss_ali).grid(column=1,row=5)
    inss_show = Label(ret_window, textvariable=inss_ret).grid(column=2,row=5)

    irrf_lbl = Label(ret_window,text='IRRF').grid(column=0,row=6)
    irrf_entry = Entry(ret_window,textvariable=irrf_ali).grid(column=1,row=6)
    irrf_show = Label(ret_window, textvariable=irrf_ret).grid(column=2,row=6)

    cofins_lbl = Label(ret_window,text='COFINS').grid(column=0,row=7)
    cofins_entry = Entry(ret_window,textvariable=cofins_ali).grid(column=1,row=7)
    cofins_show = Label(ret_window, textvariable=cofins_ret).grid(column=2,row=7)

    vfinal_lbl0 = Label(ret_window,text='Valor final da Nota: ').grid(column=0,row=8)
    vfinal_lbl = Label(ret_window,textvariable=vfinal).grid(column=2,row=8)
    btn_calcular = Button(ret_window,text='Calcular',command=lambda:calcular()).grid(column=0,row=9)

    #Cálculos e output
    #'{number:.{digits}f}'.format(number=res, digits=N)
    def calcular(event=None):
        pis_ret.set('{number:.{digits}f}'.format(number=(serv_valor.get()*(pis_ali.get()/100)), digits=2))
        cssl_ret.set('{number:.{digits}f}'.format(number=(serv_valor.get()*(cssl_ali.get()/100)), digits=2))
        inss_ret.set('{number:.{digits}f}'.format(number=(serv_valor.get()*(inss_ali.get()/100)), digits=2))
        irrf_ret.set('{number:.{digits}f}'.format(number=(serv_valor.get()*(irrf_ali.get()/100)), digits=2))
        cofins_ret.set('{number:.{digits}f}'.format(number=(serv_valor.get()*(cofins_ali.get()/100)), digits=2))
       
        vret = pis_ret.get()+cssl_ret.get()+inss_ret.get()+irrf_ret.get()+cofins_ret.get()
        vfinal.set(serv_valor.get()-vret)

    ret_window.bind('<Return>',calcular)
    ret_window.mainloop()

# Main window definition
window = Tk()
window.title('teste')
window.geometry('400x200')
mainframe = Frame(window,padx=10,pady=5).pack()

lbl1 = Label(mainframe,text='Olá, selecione uma ferramenta: ',justify='center').pack()
sdc_btn = Button(mainframe,text='Calculadora de Série D',command=csd_open).pack()
ret_btn = Button(mainframe,text='Calculadora de Imposto Retido na Nota',command=ret).pack()


window.mainloop()
