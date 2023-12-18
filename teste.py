import time
import threading
import PySimpleGUI as sg

def convert_func(window):
    for i in range(10):    # Simuate the conversion
        window.write_event_value('Conversion Step', i)
        time.sleep(1)
    window.write_event_value('Conversion Done', None)

layout = [
    [sg.Button('Convert'), sg.Text('', expand_x=True, key='Step')],
    [sg.StatusBar('', size=20, key='Status')],
]
window = sg.Window('Title', layout, finalize=True)
status, step = window['Status'], window['Step']
running, index, m = False, 0, 10

msg = ['Conversion'+'.'*i for i in range(m)]

while True:

    event, values = window.read(timeout=200)

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Convert':
        threading.Thread(target=convert_func, args=(window,), daemon=True).start()
        running = True

    elif event == sg.TIMEOUT_EVENT and running:
        status.update(msg[index])
        index = (index + 1) % m

    elif event == 'Conversion Step':
        i = values[event]
        step.update(f'Step {i}')
        

    elif event == 'Conversion Done':
        running = False
        step.update('')
        status.update(event)

window.close()