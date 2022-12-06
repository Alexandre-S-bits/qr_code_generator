from tkinter import *
from tkinter import messagebox as mb
import pyqrcode
import os

app = Tk()
app.title('Gerador de Qrcode')
app.geometry('600x420+400+150')
app.resizable(0, 0)
app.configure(bg='#0d587b')


def bt_gerar():
    """ Gera um Qrcode com as informações da caixa de texto "ct_dados_qrcode" e mostra na tela """
    global ct_dados_qrcode, code_bmp

    if len(dados_qrcode.get()) > 0:  # Verifica se a caixa de texto está vazia
        # Obtem informações da caixa de texto e gera um Qrcode
        ct_dados_qrcode = pyqrcode.create(dados_qrcode.get())
        code_image = ct_dados_qrcode.xbm(scale=3)
        code_bmp = BitmapImage(data=code_image)
    else:
        mb.showinfo("Erro!", "Informe o conteúdo do qrcode")
            
    try:
        # Tenta exibir a imagem gerada na tela (formato Bitmap)
        lb_imagem = Label(app)
        lb_imagem.place(x=390, y=210)
        lb_imagem.config(image=code_bmp)
    except:
        mb.showinfo("Erro!", "Informe o conteúdo do qrcode")


def salvar_png():
    """Salva a imagem do Qrcode no formato PNG"""
    global code_image
    # Obtendo o diretorio atual onde o programa está sendo executado
    diretorio_atual = os.getcwd() + "\\qrcodes"
    # Verifica se existe a pasta "qrcodes" no diretório atual, caso não exista será criado a 
    # pasta, caso exista os novos arquivos serão adicionado nessa pasta
    if not os.path.exists(diretorio_atual):
        os.makedirs(diretorio_atual)

    try: 
        if len(nome_arquivo_png.get()) > 0:  # Verifica se a caixa de texto do nome do arquivo está vazia
            if os.path.isfile(f'{diretorio_atual}\\{nome_arquivo_png.get()}.png'):  # Verifica se o arquivo existe no diretorio atual
                mb.showinfo("Arquivo já existe!", "Informe outro nome de arquivo")
            else:
                code_image = ct_dados_qrcode.png(f'{diretorio_atual}\\{nome_arquivo_png.get()}.png', scale=6) # Salva o arquivo em formato PNG
        else:
            mb.showinfo("Erro!", "Informe o nome do arquivo")
    except:
        mb.showinfo("Erro!", "Deve se gerar o qrcode primeiro")


def sair():
    """Finaliza a execução do programa"""
    # Pergunta se o usuario deseja sair do programa
    sair_msg = mb.askyesno("Sair do Programa", "Deseja sair?")
    if sair_msg == 1:
        app.destroy()


##### INTERFACE GRAFICA #####
# Labels
lb_titulo = Label(app, text='GERADOR DE QRCODE', bg='#261C15', fg='#FBFBFB', font='Helvitica 15 bold')
lb_titulo.pack(side=TOP, fill=X)
lb_ctqrcode = Label(app, text='Texto para gerar Qrcode', bg='#261C15', fg='#FBFBFB', font='Helvitica 12').place(x=12, y=40)
lb_arquivo = Label(app, text='Nome do arquivo para salvar', bg='#261C15', fg='#FBFBFB', font='Helvitica 12').place(x=12, y=120)

# caixas de texto
dados_qrcode = StringVar()
ct_dados_qrcode = Entry(app, textvariable=dados_qrcode, bg='#96BBBB', font='Helvitica 12')
ct_dados_qrcode.place(x=12, y=75, width=380, height=25)

nome_arquivo_png = StringVar()
ct_nome_arquivo = Entry(app, textvariable=nome_arquivo_png, bg='#96BBBB', font='Helvitica 12')
ct_nome_arquivo.place(x=12, y=155, width=380, height=25)

# botoes
bt_sair = Button(app, text='SAIR', width=12, command=sair, bg='#261C15', fg='#FBFBFB', font='verdana 10 bold')
bt_sair.place(x=460, y=40)

bt_gerar_qrcode = Button(app, text='Gerar Qrcode', command=bt_gerar, bg='#261C15', fg='#FBFBFB',
       font='verdana 10').place(x=12, y=220)

bt_salvar_png = Button(app, text='Salvar Qrcode', command=salvar_png, bg='#261C15', fg='#FBFBFB',
       font='verdana 10').place(x=180, y=220)

# Iniciar e manter execução
while True:
    app.mainloop()
