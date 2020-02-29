# -*- coding: UTF-8 -*-

# pip install AipOcr 
from aip import AipOcr
APP_ID = '00000000'
API_KEY = '00000000000000000000'
SECRET_KEY = '00000000000000000000'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
def image2text(fileName):
    image = get_file_content(fileName)
    dic_result = client.basicGeneral(image)
    res = dic_result['words_result']
    result = ''
    for m in res:
        result = result + str(m['words'])
    return result
 
getresult = image2text('./test01.jpg')
print(getresult)