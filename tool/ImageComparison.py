'''
Created on 2018年7月18日

@author: Administrator
'''
# import PIL
# import math
# import operator
# from functools import reduce
#
#
# def image_contrast(img1, img2):
#
#     image1 = Image.open(img1)
#     image2 = Image.open(img2)
#
#     h1 = image1.histogram()
#     h2 = image2.histogram()
#
#     result = math.sqrt(reduce(operator.add,  list(
#         map(lambda a, b: (a - b)**2, h1, h2))) / len(h1))
#     return result
#
#
# if __name__ == '__main__':
#     img1 = "G:/Python3/layout/tool/res/1.png"  # 指定图片路径
#     img2 = "G:/Python3/layout/tool/res/2.png"
#     result = image_contrast(img1, img2)
#     print(result)
