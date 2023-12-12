from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_and_save_text(url, text_file, encoding='utf-8'):
    # 配置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式，不弹出浏览器窗口

    # 创建 Chrome 浏览器实例
    driver = webdriver.Chrome(options=chrome_options)

    # 发送 HTTP 请求
    driver.get(url)

    # 获取动态加载后的页面内容
    page_source = driver.page_source

    # 关闭浏览器
    driver.quit()

    # 使用 Beautiful Soup 解析 HTML 内容
    soup = BeautifulSoup(page_source, 'html.parser')

    # 提取所需信息，这里假设你想要提取所有段落的文本内容
    paragraphs = soup.find_all('p')

    # 将提取的内容写入文本文件
    with open(text_file, 'w', encoding=encoding) as file:
        for paragraph in paragraphs:
            file.write(paragraph.text + '\n')

# 调用函数，分别爬取两个链接的内容并保存到不同的文本文件
scrape_and_save_text('https://wenku.baidu.com/view/1e03b71b32126edb6f1aff00bed5b9f3f90f7265?_wkts_=1699846108644', 'hutool_datetime_content.txt', encoding='gbk')
