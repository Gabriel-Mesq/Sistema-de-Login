import PySimpleGUI as sg
import mysql.connector

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
    
    sql = ("SELECT * FROM cadastro WHERE username = %s AND password = %s")
    cursor.execute(sql, dados)
    
    if cursor.fetchone():

        sg.popup('Login realizado com sucesso')

    else:

        sg.popup('Credenciais Invalidas')

elif event == 'Register':
    
    sql = "INSERT INTO cadastro (username, password) VALUES (%s, %s)"
    cursor.execute(sql, dados)
    db.commit()
    sg.popup('Registrado com sucesso')
