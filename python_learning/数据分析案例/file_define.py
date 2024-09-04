
from data_define import Record
import json


class FileReader:

    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        file = open(self.path, 'r', encoding='UTF-8')
        record_list = []
        for line in file.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        file.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        file = open(self.path, 'r', encoding='UTF-8')
        record_list = []
        for line in file.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)
        file.close()
        return record_list


if __name__ == '__main__':

    text_file = TextFileReader('D:/2011年1月销售数据.txt')
    text_data = text_file.read_data()
    json_file = JsonFileReader('D:/2011年2月销售数据JSON.txt')
    json_file.read_data()
    text_list = text_file.read_data()
    json_list = json_file.read_data()

    for line in text_list:
        print(line)

    for line in json_list:
        print(line)





