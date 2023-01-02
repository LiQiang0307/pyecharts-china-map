'''
Descripttion: 
version: 
Author: LiQiang
Date: 2022-12-31 19:50:57
LastEditTime: 2023-01-01 09:11:06
'''
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.charts import Bar,Grid

c = (
    Map(init_opts=opts.InitOpts(height="800px", width="1200px"))

    .add(
        "",
        [["北京市",7],["重庆市",3],["上海市",10],["天津市",4],["内蒙古自治区",5],["广西壮族自治区",3],["西藏自治区",3],["新疆维吾尔自治区",6],["宁夏回族自治区",3],
        ["安徽省",4],["贵州省",3],["陕西省",3],["四川省",6],["山西省",4],["海南省",3],
        ["福建省",3],["云南省",5],["广东省",15],["江西省",3],["浙江省",6],
        ["湖南省",5],["湖北省",4],["江苏省",6],["河南省",4],["青海省",4],
        ["吉林省",5],["甘肃省",5],["黑龙江省",4],["辽宁省",4],["山东省",4],["河北省",5]],
        "china",
        
        label_opts=opts.LabelOpts(is_show=True),
        is_map_symbol_show=False,
        zoom=1.2
        # tooltip_opts=opts.TooltipOpts(formatter="<span style='color:yellow;font-size:20px'>节点<span> <span style='color:red;font-size:30px'>{c}<br>------<span>")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="",subtitle="",pos_right='center'),
        visualmap_opts=opts.VisualMapOpts(max_=20,is_piecewise=True,split_number=5,pos_top="30%",pos_left="12%",
        pieces=[
            {"min":0,"max":2,"lable":"0-2个"},
            {"min":3,"max":4,"lable":"3-4个"},
            {"min":5,"max":5,"lable":"5个"},
            {"min":6,"max":10,"lable":"6-10个"},
            {"min":10,"lable":"10个以上"}
        ]),
        legend_opts=opts.LegendOpts(type_="scroll", orient="vertical"),
        toolbox_opts=opts.ToolboxOpts(
            # 是否显示该工具
            is_show=True,
            ),

    )
    .render("map_china_cities.html")
)
# grid=Grid(init_opts=opts.InitOpts(height="1000px", width="1500px"))
#  # 仅使用pos_top修改相对顶部的位置
# grid.add(c,grid_opts=opts.GridOpts(pos_top="20%"))
# grid.render("map_china_cities.html")
