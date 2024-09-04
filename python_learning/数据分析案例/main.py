from data_define import Record
from file_define import TextFileReader, JsonFileReader, FileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader('D:/2011年1月销售数据.txt')
json_file_reader = JsonFileReader('D:/2011年2月销售数据JSON.txt')

text_data: list[Record] = text_file_reader.read_data()
json_data: list[Record] = json_file_reader.read_data()

all_data: list[Record] = text_data + json_data

data_dict = {}
for record in all_data:
    if record.data in data_dict:
        data_dict[record.data] += record.money
    else:
        data_dict[record.data] = record.money

bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('销售额', list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额'),
)
bar.render('每日销售额.html')