import cv2

# Подключение к камере
cap = cv2.VideoCapture(0)
# если кадр не считался, то выводит ошибку
while True:
    # Чтение кадра
    ret, frame = cap.read() # присваиваем кадр в переменную
    if not ret:
        print("Ошибка захвата кадра!")
        break

    # Получение размеров кадра
    height, width = frame.shape[:2]
    #shape функция возвращает разное количество переменных, в зависимости от изображения
    # если изображение чб, то вернет только высоту и ширину кадра
    # синтаксис (высота, ширина, количество каналов)
    center_x, center_y = width // 2, height // 2  # Центр экрана
    # Параметры креста
    #rectangle() # закрашивает прямоугольник
    cross_length = 40  # Длина "лучей" креста
    color = (0, 0, 255)  # Красный цвет в формате BGR
    thickness = 2       # Толщина линий

    # функция rectangle чертит прямоугольник(верхний левый угол, нижний правый угол, цвет в формате BGR, толщина линии)
    cv2.rectangle(frame, (center_x - 6, center_y - 40), (center_x + 6, center_y + 40), (0, 0, 255), 2)
    cv2.rectangle(frame, (center_x - 40, center_y - 6), (center_x + 40, center_y + 6), (0, 0, 255), 2)

    # Отображение кадра
    cv2.imshow('Camera with Cross', frame)

    # Выход по клавише ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()