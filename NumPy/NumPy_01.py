from PIL import Image
import numpy as np

# исходные картинки
names = ["NumPy/lunar_images/lunar01_raw.jpg", "NumPy/lunar_images/lunar02_raw.jpg",
         "NumPy/lunar_images/lunar03_raw.jpg"]

# названия для новых картинок
new_names = ["NumPy/lunar_images/answers_lunar/lunar01_raw.jpg", "NumPy/lunar_images/answers_lunar/lunar02  _raw.jpg",
             "NumPy/lunar_images/answers_lunar/lunar03_raw.jpg"]

for i in range(len(names)):
    img = Image.open(names[i]) # открываем исходную картинку
    data = np.array(img) # записываем картинку в матричном виде
    new_data = ((data-data.min())/(data.max()-data.min())*255).astype(np.uint8) # растягиваем диапазон цветов
    result_img = Image.fromarray(new_data) # делаем новую картнику
    result_img.save(new_names[i]) # сохраняем новую картинку