
from pyecharts.charts import Line
from pyecharts.options import TitleOpts

# 得到折线对象
line = Line()
# 添加x轴数据
line.add_xaxis(["北京","上海","深圳"])
# 添加y轴数据
line.add_yaxis("GDP",[100,90,80])

# 设置全局变量
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示")
)

# 生成图表
line.render()

