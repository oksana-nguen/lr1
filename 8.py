import cv2

# Подключение к камере
cap = cv2.VideoCapture(0)

while True:
    # Чтение кадра
    ret, frame = cap.read()
    if not ret:
        print("Ошибка захвата кадра!")
        break

    # Получение размеров кадра
    height, width = frame.shape[:2]
    center_x, center_y = width // 2, height // 2  # Центр экрана
    picsel=frame[center_y][center_x] # получение центрального пикселя
    # у пикселя три значения цвета
    b=picsel[0]
    g=picsel[1]
    r=picsel[2]
    # Параметры креста
    #rectangle() # закрашивает прямоугольник
    cross_length = 40  # Длина "лучей" креста
    color = (0, 0, 255)  # Красный цвет в формате BGR
    thickness = 2       # Толщина линий
    if(b>g and b>r):
        cv2.rectangle(frame, (center_x - 6, center_y - 40), (center_x + 6, center_y + 40), (0,0,255), -1)
        cv2.rectangle(frame, (center_x - 40, center_y - 6), (center_x + 40, center_y + 6), (0,0,255), -1)
    elif (g>b and g>r):
        cv2.rectangle(frame, (center_x - 6, center_y - 40), (center_x + 6, center_y + 40), (0,255,0), -1)
        cv2.rectangle(frame, (center_x - 40, center_y - 6), (center_x + 40, center_y + 6), (0,255,0), -1)
    else:
        cv2.rectangle(frame,(center_x-6,center_y-40),(center_x+6,center_y+40),(255,0,0),-1)
        cv2.rectangle(frame, (center_x - 40, center_y -6), (center_x + 40, center_y + 6), (255,0,0), -1)
    # Отображение кадра
    cv2.imshow('Camera with Cross', frame)

    # Выход по клавише ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()