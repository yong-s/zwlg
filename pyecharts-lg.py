from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.charts import Pie

city_names = ["北京", "上海", "深圳", "广州", "杭州", "成都", "武汉", "长沙", "南京", "天津",
              "苏州", "常州", "南宁", "青岛", "厦门", "沈阳", "无锡", "郑州", "重庆", "合肥", "淮北", "济南", "泉州", "芜湖", "珠海"]
city_nums = [122, 82, 71, 52, 45, 20, 12, 8, 7, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]

city_toal = []
for i in range(0, len(city_names)):
    # print(city_names[i])
    # print(city_nums[i])
    city_str = "(" + str(city_names[i]) + ", " + str(city_nums[i]) + ")"
    city_toal.append(city_str)
print(city_toal)
# V1 版本开始支持链式调用
# bar = (
#     Bar()
#     .add_xaxis(city_names)
#     .add_yaxis("各城市数量", city_nums)
#     .set_global_opts(title_opts=opts.TitleOpts(title="测试各城市招聘数量"))
# )
# bar.render("测试岗位各城市数量.html")

# geo = (
#         Geo()
#         .add_schema(maptype="china")
#         .add("数量", city_toal)
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#             visualmap_opts=opts.VisualMapOpts(),
#             title_opts=opts.TitleOpts(title="测试岗位城市分布地图"),
#         )
#     )
# geo.render("测试岗位城市分布地图_scatter.html")

# pie = (
#     Pie()
#         .add("", city_names)
#         .set_global_opts(title_opts=opts.TitleOpts(title="岗位各城市分布饼图"),
#                          legend_opts=opts.LegendOpts(pos_left="15%"), )
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# )
# pie.render("岗位各城市分布饼图.html")
