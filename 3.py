#Отобразить видео в окне. Рассмотреть методы класса VideoCapture и попробовать отображать
# видео в разных форматах, в частности размеры и цветовая гамма.
import cv2
cap=cv2.VideoCapture(r'C:\Users\Honor\Downloads\IMG_9465.MP4',cv2.CAP_ANY) # прочитали кадр из видео
while True:
    ret, frame=cap.read() # ret - булевское значение, обозначающее, удалось ли выполнить чтение кадра
    if not ret:            # сам кадр - frame
        break
    #res_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # задаем серый цвет для видео
    #res_frame=cv2.bitwise_not(frame) # задаем инверсию цветов
   # res_frame=cv2.resize(res_frame,(500,600)) # меняем размер окна и видео
    res_frame = cv2.resize(frame, (500, 600))
    cv2.imshow('frame',res_frame)       # отображаем наше видео
    if cv2.waitKey(5) & 0xFF==27:         # скорость между кадрами в миллисекундах
        break                             # и если нажата клавиша Escape, то завершить
cap.release() # закрывает видеофайл и освобождает ресурсы
cv2.destroyAllWindows() # закрывает все окна с изображениями, созданные в текущей сессии