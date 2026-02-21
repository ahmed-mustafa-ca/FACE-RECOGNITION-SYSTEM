import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

count = 0
faceMatch = False
threadRunning = False
lock = threading.Lock()

referenceImg = cv2.imread(r'C:\Users\Jamshaid Mustafa\OneDrive\ahmed mustafa 2.0\Deep Learning\DL Projects\Face recognition\reference.jpg')


if (referenceImg is None):
    raise FileNotFoundError("reference.jpg not found!")

def checkFace(frame):
    global faceMatch, threadRunning

    try:
        result = DeepFace.verify(frame, referenceImg.copy())
        with lock:
            faceMatch = result['verified']

    except ValueError:
        with lock:
            faceMatch = False
    
    finally:
        threadRunning = False

while True:
    ret, frame = cap.read()

    if (ret):
        if (count % 30 == 0 and not threadRunning):
            threadRunning = True
            threading.Thread(target=checkFace, args=(frame.copy(),), daemon=True).start()
        
        count += 1

        if (faceMatch == True):
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 2,  (0, 255, 0), 3)

        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 2,  (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)

    if (key == ord("q")):
        break
    
cap.release()
cv2.destroyAllWindows()