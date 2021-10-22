import cv2
import numpy as np
import pyautogui
import time
import keyboard


def video_recording():
    
    print('asd')       
    # rezolutia ecranului pe care o iei din sistemul de operare
    SCREEN_SIZE = (1920, 1080)
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # crearea obiectului
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
        
    fps = 120
    # e o variabila care ma ajuta sa incetinesc inregistrarea video ca sa nu fie rapida
    prev = 0
        
    # am ales 14400 pentru ca FPS * 2 *60
    for i in range(14400):
        time_elapsed = time.time() - prev
        # face o captura a ecranului
        img = pyautogui.screenshot()
        if time_elapsed > 1.0/fps:
            prev = time.time()
            # converteste pixelii in numpy ca poate folosi opencv
            frame = np.array (img)
            # converteste paltea din BGR (Blue - Green - Red) in RGB (Red - Green - Blue) pentru pentru ca RGB e folosit default de opencv
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # inregistreazza cadrul
        out.write(frame)   
        # arata cadrul
        # cv2.imshow("screenshot", frame)
        # daca se apasa q se opreste inregistrarea
        if keyboard.is_pressed('q'):
            break
        
    # asigura ca se inchide totul si se elibereaza memoria
    cv2.destroyAllWindows()
    out.release()
            