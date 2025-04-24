import cv2

# Настройки записи видео
#запись видео в данную папку
output_filename = r'C:\Users\Honor\Downloads\lr1\vid.avi'
codec = cv2.VideoWriter.fourcc(*'XVID')  # Кодек для AVI
fps = 25.0  # Кадров в секунду

# Инициализация видеозахвата
cap = cv2.VideoCapture(0)

# Проверка подключения камеры
if not cap.isOpened():
    print("Ошибка: камера не найдена!")
    exit()

# Получение разрешения кадра с камеры
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Инициализация объекта для записи видео
out = cv2.VideoWriter(output_filename, codec, fps, (frame_width, frame_height))

# Основной цикл обработки
while True:
    # Считывание кадра
    ret, frame = cap.read()

    if not ret:
        print("Ошибка захвата кадра!")
        break

    # Запись кадра в файл
    out.write(frame)

    # Отображение кадра
    cv2.imshow('Webcam Live', frame)

    # Прерывание по ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Освобождение ресурсов
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Видео сохранено как: {output_filename}")