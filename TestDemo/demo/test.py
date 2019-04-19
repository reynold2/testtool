# -*- coding: UTF-8 -*-
from PIL import Image
import pytesseract


text=pytesseract.image_to_string(Image.open('QQ截图20190418152850.png'),lang='chi_sim')
print(text)
