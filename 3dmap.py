'''
Descripttion: 
version: 
Author: LiQiang
Date: 2022-12-31 21:42:09
LastEditTime: 2022-12-31 21:56:54
'''
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

c = (
    Map3D(init_opts=opts.InitOpts(width='1000px', 
                                height='600px', 
                                theme=ThemeType.VINTAGE))
    # 地图类型
    .add_schema(
        itemstyle_opts=opts.ItemStyleOpts( # 图形的颜色
            color="#00BFFF", # 或 'rgb(128, 128, 128)'
            opacity=1, # 图形透明度
            border_width=0.8, # 描边宽度
            border_color="#708090", # 描边颜色
        ),
        # Map3D 的 Label 设置
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + " " + data.value;}"),
        ),
        
        # 高亮标签配置项
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,
            color="#fff",
            font_size=10,
            background_color="rgba(0,23,11,0)",
        ),
        
        # 光照相关的设置。
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            main_shadow_quality="high",
            is_main_shadow=False,
            main_beta=10,
            ambient_intensity=0.3,
        ),
    )
    .add(
        series_name="",
        data_pair=[["北京市",7],["重庆市",3],["上海市",3],["天津市",4],["内蒙古自治区",5],["广西壮族自治区",3],["西藏自治区",3],["新疆维吾尔自治区",4],["宁夏回族自治区",3],
        ["安徽省",4],["贵州省",3],["陕西省",3],["四川省",4],["山西省",4],["海南省",3],
        ["福建省",3],["云南省",5],["广东省",15],["江西省",3],["浙江省",4],
        ["湖南省",5],["湖北省",4],["江苏省",6],["河南省",4],["青海省",4],
        ["吉林省",5],["甘肃省",5],["黑龙江省",4],["辽宁省",4],["山东省",4],["河北省",5]],
        # 叠加图的类型
        type_=ChartType.BAR3D,
        bar_size=1,
        
        # 三维地图中三维图形的着色效果。
        shading="lambert",
        label_opts=opts.LabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + ' ' + data.value;}"),
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="请输入标题"))
    .render("map3d_with_bar3d.html")
)