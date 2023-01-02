'''
Descripttion: 
version: 
Author: LiQiang
Date: 2023-01-01 18:25:12
LastEditTime: 2023-01-02 16:35:30
'''
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType,ThemeType,GeoType
from pyecharts.commons.utils import JsCode

geo = (
    Geo(init_opts=opts.InitOpts(width='1500px', 
                                height='1000px',
                                # bg_color = "blue"
                                ),
        is_ignore_nonexistent_coord=True)
    .add_schema(maptype="china")                       #maptype选择地图种类
    .add(series_name="",      # 系列名称
         data_pair=[["北京市",10],["西藏",1],["四川省",10],["福州市",10],["黑龙江省",6],["宁夏回族自治区",6],["上海市",10],["云南省",6],["深圳市",11],
         ["桂林市",12],["合肥市",6],["长沙市",6],["台州市",6],["淄博市",6],["六安市",4],
         ["信阳市",5],["阳新县",6],["南宁市",5],["曲靖市",8],["珠江三角洲",9],
         ["泉州市",10],["内蒙古自治区",6],["保定市",4],["无锡市",4],["武汉市",4],
         ["长洲区",3],["定边县",3],["抚州市",5],["东营市",2],["疏勒县",1],
         ["湖北省",6],["乌鲁木齐县",1],["西平县",2],
         ["穆棱市",2],["青岛市",4],["保定市",3],["青海省",2],["辽宁省",1]
        ],
        #  blur_size=10,
         symbol_size= JsCode('function (data) {return data[2]*4;}'),
        #  type_=ChartType.HEATMAP,     #类型选为热力图
        type_=GeoType.EFFECT_SCATTER
        )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True,formatter='{b}'))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=15,is_piecewise=True,pos_top="30%",pos_left="12%",pieces=[
                       
                        {"min": 12, "max": 15,"color":"#79dd6b"},
                        {"min": 9, "max": 12,"color":"#72a93f"},
                        {"min": 6, "max": 9,"color":"#6bdd8a"},
                        {"min": 3, "max": 6,"color":"#6bdd7b"},
                        {"min": 0, "max": 3,"color":"#1be297"},
                        # {"min": 12, "max": 15,"color":"red"},
                        # {"min": 9, "max": 12,"color":"red"},
                        # {"min": 6, "max": 9,"color":"red"},
                        # {"min": 3, "max": 6,"color":"red"},
                        # {"min": 0, "max": 3,"color":"red"},
                    ]),
        title_opts=opts.TitleOpts(title=""))
)
geo.render('热力图.html')