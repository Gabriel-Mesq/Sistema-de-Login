from tkinter import INSERT
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

if event == 'Login':
    
    sql = ("SELECT * FROM cadastro WHERE username = %s AND password = %s")
    cursor.execute(sql, dados)
    
    if cursor.fetchone():

        print("Successfully")

    else:

        print("Invalid Credentials")

elif event == 'Register':
    
    sql = "INSERT INTO cadastro (username, password) VALUES (%s, %s)"
    cursor.execute(sql, dados)
    db.commit()

window.close()

