import requests
from bs4 import BeautifulSoup
import openpyxl

# 发送HTTP请求
url = 'https://hutool.cn/docs/index.html#'
response = requests.get(url)

# 使用Beautiful Soup解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 创建Excel工作簿和工作表
workbook = openpyxl.Workbook()
sheet = workbook.active

# 提取所需信息，这里假设你想要提取所有段落的文本内容
paragraphs = soup.find_all('p')

# 将提取的内容写入Excel
for index, paragraph in enumerate(paragraphs, start=1):
    sheet.cell(row=index, column=1, value=paragraph.text)

# 保存Excel文件
workbook.save('hutool_content.xlsx')
