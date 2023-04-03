import json
from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.sampledata.iris import flowers
from bokeh.themes import Theme

colormap = {"setosa": "red", "versicolor": "green", "virginica": "blue"}
colors = [colormap[x] for x in flowers["species"]]

gray_theme = Theme(json={"attrs": {"Plot": {"background_fill_color": "#eeeeee"}}})


def make_plot(x, y):
    p = figure(title="Iris Morphology", sizing_mode="fixed", width=400, height=400)
    p.xaxis.axis_label = x
    p.yaxis.axis_label = y
    p.circle(flowers[x], flowers[y], color=colors, fill_alpha=0.2, size=10)
    return p
