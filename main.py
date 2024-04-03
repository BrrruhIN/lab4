import PySimpleGUI as sg


tab1_layout = [
    [sg.Text('Введите расстояние')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Рассчитать'), sg.Button('Очистить')]
]


tab2_layout = [
    [sg.Text('Выберите опцию подсчета:')],
    [sg.Combo(['Автобус', 'Троллейбус', 'Трамвай'], key='-TRANS-')],
    [sg.Button('Выбрать'), sg.Button('Сбросить')]
]


tab3_layout = [
    [sg.Text('Стоимость', size=(15, 1), justification='center')],
    [sg.Text(size=(40, 1), key='-RESULT-')]
]


tab_group_layout = [
    [sg.Tab('Расстояние', tab1_layout), sg.Tab('Транспорт', tab2_layout), sg.Tab('Стоимость', tab3_layout)]
]


layout = [[sg.TabGroup(tab_group_layout)]]
window = sg.Window('Калькулятор стоимости поездки', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Рассчитать':
        if values['-TRANS-'] == 'Автобус':
            result = float(values['-INPUT-']) * 2.9 
        elif values['-TRANS-'] == 'Троллейбус':
            result = float(values['-INPUT-']) * 2.5
        elif values['-TRANS-'] == 'Трамвай':
            result = float(values['-INPUT-']) * 2.2
        window['-RESULT-'].update(f'Результат: {result}')
    elif event == 'Очистить':
        window['-INPUT-'].update(f' ')
    elif event == 'Сбросить':
        window['-TRANS-'].update(f' ')
window.close()

