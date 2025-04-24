import cv2 # импорт библиотеки
def read_ip_write_to_file(): # создаем функцию
    video=cv2.VideoCapture(0) # инициализация захвата камеры 0-камера. Если камер несколько, то др индексы
    ok,img=video.read() # чтение первого кадра
    if not ok: # проверка первого кадра
        print("ошибка") # если кадр не получен, то выдается сообщение об ошибке
        video.release() # освобождение ресурсов камеры
        return # выход из функции
    w=int(video.get(cv2.CAP_PROP_FRAME_WIDTH)) # ширина кадра
    h=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)) # высота кадра
    fourcc = cv2.VideoWriter.fourcc(*'XVID') # настройка кодека для записи видео
    # Создание объекта для записи видео: имя файла, кодек, FPS, размер кадра
    video_writer=cv2.VideoWriter("output.avi",fourcc,25,(w,h))
    while True: # цикл, который записывает видео
        ok,img=video.read() 
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# первый кадр серого цвета
        cv2.imshow('gray',gray) # отображение серого кадра в окне
        video_writer.write(img) # запись кадра в файл
        # при нажатии кнопки ESC закрывается окно
        if cv2.waitKey(1) & 0xFF==27:
            break
    video.release() # Закрытие подключения к камере
    video_writer.release() #Завершение записи видео
    cv2.destroyAllWindows() #Закрытие всех окон OpenCV
read_ip_write_to_file() # вызов функции