from pickle import NONE
import PySimpleGUI as sg    


# find a way to always give him permission
# Show the user, the options for him to log into Google
# close the screen and show a screen for him to wait til the login is over
# if an error occurs, show him another screen to log in google again

google_drive_login_layout = [[sg.Text('Escolha por onde você quer entrar')],
                            [sg.Button('Google-Drive')]
                            ]

input_screen_layout = [
                [sg.Text('Digite o link da pasta do google drive: ')],
                [sg.Input(key='-GOOGLE-DRIVE-LINK-')],
                [sg.Text('Selecione o local de save do jogo: ')],
                #verify if the folder exist
                [sg.Input(key = '-FOLDER-LOCATION-'), sg.FolderBrowse()],     
                [sg.Button("Submit"), sg.Button("Cancel")]]      

google_drive_login_window = sg.Window('Google Drive', google_drive_login_layout) 

while True:
    event, values = google_drive_login_window.read()
    if event == "Google-Drive":
        print('a')

    break

input_screen_window = sg.Window('Log_in', input_screen_layout) 
while True:
    event, values = input_screen_window.read()
    if event == "Cancel":
        sg.Window.close(self=input_screen_window)
        break
    if event == sg.WIN_CLOSED or event=="Cancel":
        break
    elif event == "Submit":
        if(values['-GOOGLE-DRIVE-LINK-'] == ""):
            sg.popup('there is no google drive link, try again')
        if(values['-FOLDER-LOCATION-'] == ""):
            sg.popup('you did not typed a valid folder, try again')
        #RODAR A APLICAÇÃO
        # verificiar se a pasta existe
        
# Change the screen design
   

event, values = window.read()    
window.close()

# text_input = values['-IN-']    
# sg.popup('You entered', text_input)