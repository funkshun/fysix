import numpy as np

from bokeh.layouts import row, widgetbox
from bokeh.models import CustomJS, Slider, DataRange1d, Plot, LinearAxis, Grid, HoverTool
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.glyphs import MultiLine
from bokeh.models.markers import Circle
from bokeh.colors import RGB

N = 10 # Number of SubReddits Investigated
MAX_CONNECTION_STRENGTH = 10 # How connection strength is normalized

# Calculate connection strengths to determine initial positions
connections = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if j < i:
            connections[i][j] = np.random.randint(1, MAX_CONNECTION_STRENGTH) # This will be really function later

x = np.zeros(N) # x Position
y = np.zeros(N) # y position
r = np.zeros(N) # radius of node
s = np.zeros(N) # infected value (0-1)
subs = np.zeros(N) # subscriber counter
color = np.array([]) # Color for each node
URL = np.array([]) # URL
name = np.array([]) # SubReddit name

for i in range(N):
    x[i] = np.random.randint(N) # point's x value
    y[i] = np.random.randint(N) # point's y value
    r[i] = np.random.randint(40, 60) # radius
    s[i] = np.random.rand()
    subs[i] = np.random.randint(40, 60) # radius
    URL = np.append(URL, 'Hello.com')
    name = np.append(name, 'This is my sub reddit')
    color = np.append(color, RGB(255*s[i], 20, 180*(1-s[i])))

#hover_tool = HoverTool(tooltips=my_custom_tooltips, line_policy='nearest')
#pan_tool = PanTool(dimension="x")
#plot.add_tools(hover_tool, pan_tool)

xdr = DataRange1d()
ydr = DataRange1d()

source = ColumnDataSource(dict(x=x, y=y, r=r, name=name, color=color, infect=s, URL=URL))

plot = figure(
    title=None, x_range=xdr, y_range=ydr, plot_width=1100, plot_height=700,
    h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location = None)
plot.axis.visible = None
plot.xgrid.visible = False
plot.ygrid.visible = False

plot.add_tools(HoverTool(
    tooltips = [
        ( 'Sub-Reddit Name', '@name'),
        ('URL' , '@URL'),
        ( 'Subscriber Count', '@subs')

    ]
))

# Add lines connecting each glyph
for i in range(N):
    for j in range(N):
        if j <= i:
            rgbval = 255 - 255*connections[i][j]/MAX_CONNECTION_STRENGTH # Shade from white to black based on connection strength
            lineColor = RGB(rgbval, rgbval, rgbval)
            width = connections[i][j]
            plot.line([x[i], x[j]], [y[i], y[j]], line_width = np.random.randint(7), line_color = lineColor)
for i in range(N):
    glyph = Circle(x="x", y="y", size="r", fill_color="color", line_width=1)
    plot.add_glyph(source, glyph)

# JS code triggered whenever value slider is changed
callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var size = data['r']
    size[0] = radius.value

    source.change.emit();
""")

rSlider = Slider(start=0, end=5, value=1, step=.1,
                    title="Time", callback=callback)
callback.args["radius"] = rSlider

layout = row(
    widgetbox(rSlider),
    plot
)


show(layout)
