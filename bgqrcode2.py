import os
import pandas as pd
from PIL import Image   #image connector library
import qrcode   #qr-code library
import random

tickets_num = 450   # указываем количество билетов
city = 'istanbul'   #указываем город
ticket_name = 'Bilet.png' #имя шаблона билета в пнг формате
#создаем папки для билетов, qr, списка билетов
os.mkdir(city+ '_tickets')
os.mkdir(city+ '_qr')
os.mkdir(city+ '_ticket_list')

#создаем список рандомных пятизначных кодов без повторений
l=[]
for i in range(tickets_num):
    a = random.randint(10000, 99999)
    if a in l:
        while a in l:
            a = random.randint(10000, 99999)
    l.append(a)

#создаем класс для qr кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
# создаем qr коды
for i in range(tickets_num):
    data = str(l[i]) # информация которая записывается в код
    filename = './' + city + '_qr/' + data + '.png'     # прописываем путь, название файла + расширение пнг
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")
    img.save(filename)

    # накладываем код на шаблон билета
    img = Image.open(ticket_name)       # указали название файла на который накладываем
    watermark = Image.open(filename)    # название того, который накладываем
    img.paste(watermark, (417, 895))    # параметры вставки: 1 параметр - путь к изображению, 2й параметр - точка вставки, 3й параметр - альфаканал (используется для наложения)
    img.save('./' + city + '_tickets/' + data + '_ticket.png')    # прописываем путь, название файла + расширение пнг
    l[i] = str(l[i])

# создаем таблицу
df_tic = pd.DataFrame({'Ticket_number': l,
                   'Купил': l,
                   'Пришел': l,
                   'email' : '',})
writer = pd.ExcelWriter('tickets_' + city + '.xlsx')   # записываем в файл, указываем путь, имя
df_tic.to_excel(writer)
writer.save()

'''
img = Image.open('1920x1080_october.png')
    # указали название файла на который накладываем
    watermark = Image.open('tproger.png')

# название того, который накладываем
img.paste(watermark, (450, 550),  watermark)
# параметры вставки: 1 параметр - путь к изображению, 2й параметр - точка вставки, 3й параметр - альфаканал (используется для наложения)
img.save("img_with_watermark.png")

#Для того чтобы наложить водяной знак или какой то другой рисунок на больше количество изображений слегка изменим код:

from PIL import Image

img_list = ['image1.png', image2.png, image3.png, image4.png]
for image in img_list:
    img = Image.open(image)
    watermark = Image.open('watermark.png')

    img.paste(watermark, (450, 230),  watermark)
    img.save(image)
'''