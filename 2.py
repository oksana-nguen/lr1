#Протестировать три возможных расширения, три различных флага для создания окна и три
# различных флага для чтения изображения.
import cv2 # подключаем библиотеку cv
img=cv2.imread(r'C:\Users\Honor\Downloads\1664208668_new.jpg') # считываем путь файла и присваиваем переменной
#img=cv2.imread(	r'C:\Users\Honor\Downloads\1664208668_new.jpg',cv2.IMREAD_GRAYSCALE) # загрузить фото серого цвета
#img=cv2.imread(	r'C:\Users\Honor\Downloads\1664208668_new.jpg',cv2.IMREAD_COLOR_RGB)
#cv2.namedWindow('Display window',cv2.WINDOW_NORMAL)     # создает окно с указанным именем и различными флагами
#cv2.namedWindow('Display window',cv2.WINDOW_KEEPRATIO) # размер фото и окна соблюдается
#cv2.namedWindow('Display window',cv2.WINDOW_FULLSCREEN) # размер фото на полный экран
cv2.imshow('Display window',img)                        # отображаем окно с введенным именем
#cv2.waitKey(0)                                                   # позволяют ожидать нажатия кнопки и закрыть окно
cv2.destroyAllWindows()
