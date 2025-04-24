import cv2 #подключаем библиотеку cv
img=cv2.imread(r'C:\Users\Honor\Downloads\1664208668_new.jpg')  #считываем путь файла и присваимваем переменной
cv2.namedWindow('Display window',cv2.WINDOW_NORMAL)     #создает окно с указанным именем и различ флагами
cv2.imshow('Display window',img)                        #отображаем окно с введеным именем
cv2.waitKey(0)                                                   #позволяют ожидать нажатия кнопки и закрыть окно
cv2.destroyAllWindows()
