import PySimpleGUI as sg
import mysql.connector

def cadastrado (dados):

    cursor.execute("SELECT * FROM cadastro WHERE username = %s AND password = %s", dados)
    
    if cursor.fetchone():
        return True

    else:
        return False

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "login")

cursor = db.cursor()

sg.theme('Dark Grey 13')

layout = [
    [sg.Text('Usuário:')],
    [sg.Input(key='username')],
    [sg.Text('Senha:')],
    [sg.Input(key='password')],
    [sg.Button('Register'), sg.Button('Login')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Realize seu login', layout)
event, values = window.read()
dados = (values['username'], values['password'])
window.close()

if event == 'Login':
    
    if cadastrado(dados): 
        sg.popup('Login realizado com sucesso.', title='Sucesso')

    else: 
        sg.popup('Credenciais Invalidas.', title='Erro')

elif event == 'Register':

    if not cadastrado(dados): 
        
        sql = "INSERT INTO cadastro (username, password) VALUES (%s, %s)"
        cursor.execute(sql, dados)
        db.commit()
        sg.popup(f'{dados[0]}, sua conta foi registrada com sucesso.', title='Sucesso')

    else:
        sg.popup(f'O usuário {dados[0]} já está cadastrado em nosso sistema.', title='Erro')

