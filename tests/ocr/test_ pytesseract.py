# -*- coding: UTF-8 -*-

import pytesseract
from PIL import Image

image = Image.open('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/ocr/timg.jpeg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)


image = Image.open('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/ocr/lhx.jpeg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)