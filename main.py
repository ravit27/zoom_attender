import pyautogui
import schedule
import time
slashes = "/" * 50



print('\n\n', slashes)

print('ZOOM ATTENDER')
print('\n>>Enter the following details regarding the meeting to set it up...')
print('Use ( Ctrl+c ) to exit at any time')

print('\n', slashes)

meet_id = input('Enter Meeting ID: ')
password = input('Enter Meeting password: ')
meet_time = input(
    ('Enter everyday meeting time in 24hour format (eg: "15:30" for 3:30pm): '))
total_meet = input(
    'How long will the meeting last for ?(Answer in minutes eg:120 for 2 hours): ')
print(slashes)

# just for confirmation
total_meet = int(total_meet)
meet_time = str(meet_time)



def zoomClass():
    time.sleep(0.2)

    pyautogui.press('esc', interval=0.1)

    time.sleep(0.3)

    pyautogui.press('win', interval=0.5)
    pyautogui.write('zoom')
    time.sleep(2)
    pyautogui.press('enter', interval=0.5)

    time.sleep(10)

    x, y = pyautogui.locateCenterOnScreen('F:/Zoom-Automation/joinIMG.png')
   
    pyautogui.click(x, y)

    pyautogui.press('enter', interval=5)
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=5)

    pyautogui.write(password)
    pyautogui.press('enter', interval=10)

    print("Session has started and will continue for %s minutes" % total_meet)

    print('Hold (Ctrl+c) to exit the program ')

    # Total time of zoom session
    time.sleep(total_meet * 60)

    # closing Zoom
    os.system("TASKKILL /F /IM Zoom.exe")
    time.sleep(0.5)


schedule.every().day.at("%s" % meet_time).do(zoomClass)
print("Scheduling meeting at ", meet_time)

while True:
    schedule.run_pending()
    time.sleep(1)
