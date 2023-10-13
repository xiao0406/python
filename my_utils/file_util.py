def print_file_info(file_name):
    '''
    print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    :param file_name:
    :return:
    '''
    result = None
    try:
        result = open(file_name,"r")
        print(result.read())
    except (Exception) as e :
        print("文件不存在")
    finally:
        if result:
            result.close()

def append_to_file(file_name,data):
    '''
    接收文件路径以及传入数据，将数据追加写入到文件中
    :param file_name:
    :param data:
    :return:
    '''
    result = open(file_name, 'a',encoding="UTF-8")
    result.write(data)
    result.write("\n")
    result.close()
