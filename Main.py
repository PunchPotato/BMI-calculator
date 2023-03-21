import PySimpleGUI as sg


layout = [[sg.Text('Enter your weight in kilograms:'), sg.Input(k='-W-', size=(15))],
          [sg.Text('Enter your height in metres:    '), sg.Input(k='-H-', size=(15))],
          [sg.Text('Your BMI is: ', size=(40,1), k='-OUT-')],
          [sg.Button('OK'), sg.Button('Exit')]]

window = sg.Window('BMI Calculator', layout)

while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    h = float(values['-H-'])**2
    w = float(values['-W-'])
    BMI = round(w/h, 2)

    if BMI <= 18.5:
        window['-OUT-'].update(f"Your BMI is: {BMI}. You are underweight.")
    elif BMI <= 24.9:
        window['-OUT-'].update(f"Your BMI is: {BMI}. You are normal.")
    elif BMI <= 29.9:
        window['-OUT-'].update(f"Your BMI is: {BMI}. You are overweight.")
    else:
        window['-OUT-'].update(f"Your BMI is: {BMI}. You are obese.")

window.close()

