import numpy as np
from bs4 import BeautifulSoup
import codecs
import simulator
import holoviews as hv
from bokeh.layouts import row, widgetbox
from bokeh.models import CustomJS, Slider, DataRange1d, Plot, LinearAxis, Grid, HoverTool, Dropdown, Select, Button, PreText
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.glyphs import MultiLine
from bokeh.models.markers import Circle
from bokeh.colors import RGB

pickles = ["smallpolitical", "political", "entertainment"]

## Bokeh initialization code
hv.extension('bokeh')
output_file('DataVis.html')

# Code to launch on startup
def startup():
    infected = []
    sub_reference = []
    connections = []
    subreddits = []
    for pickle in pickles:
        sim_tuple = simulator.simulate(pickle)
        connections.append(sim_tuple[0])
        subreddits.append(sim_tuple[1])
        sub_reference.append(sim_tuple[2])

    launch(subreddits, connections, sub_reference)


def launch(all_subreddits, all_connections, sub_reference):
    # Matrices containing constants for each pickles

    numPickles = len(pickles)

    # Store the position, number of subreddits, a
    X = []
    Y = []
    R = []

    for i in range(numPickles):
        X.append([])
        Y.append([])
        R.append([])

    N = []

    infected = all_subreddits
    colors = []
    for i in range(numPickles):
        colors.append(make_color(infected[i]))

    ## Unload parameters #######################################################
    for l in range(len(all_subreddits)):
        subreddits = all_subreddits[l]
        connections = all_connections[l]
        total = len(connections) # Number of SubReddits Investigated
        timeSteps = len(subreddits[0]) # Length of the arrays (number of time steps)
        x = np.zeros(total) # x Position
        y = np.zeros(total) # y position
        r = np.zeros(total) # radius of node

        for i in range(total): # For each sub reddit
            x[i] = np.random.randint(10) # point's x value
            y[i] = np.random.randint(10) # point's y value
            r[i] = np.random.randint(40, 60) # radius
            #subs[i] = np.random.randint(40, 60) # radius

        #Add the current subreddit data to the Matrices
        X[l] = x
        Y[l] = y
        R[l] = r
        N.append(total)

        ## Plotting code ########################################################

    xdr = DataRange1d()
    ydr = DataRange1d()

    curPickle = 0

    source = ColumnDataSource(dict(time=[0, 0, 0], x=X[curPickle], y=Y[curPickle],
        r=R[curPickle], colors=colors[curPickle], name=sub_reference[curPickle]))

    plot = figure(
        title=None, x_range=xdr, y_range=ydr, plot_width=1100, plot_height=700,
        h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location = None)
    plot.axis.visible = None
    plot.xgrid.visible = False
    plot.ygrid.visible = False

    plot.add_tools(HoverTool(
    tooltips = [
            ('Sub-Reddit Name', '@name'),
            ('URL', '@URL'),
            ]
        ))


    # Add lines connecting each glyph
    for i in range(N[curPickle]):
        for j in range(N[curPickle]):
            if j <= i:
                rgbval = 255 - 255*connections[i][j] # Shade from white to black based on connection strength
                lineColor = RGB(rgbval, rgbval, rgbval)
                width = connections[i][j]
                x = X[curPickle]; y = Y[curPickle]
                plot.line([x[i], x[j]], [y[i], y[j]],
                    line_width = np.random.randint(7), line_color = lineColor)

    curTimeIdx = 0

    # Add all the glyphs to the main plot
    glyph = Circle(x="x", y="y", size="r", fill_color="colors", line_width=1)
    plot.add_glyph(source, glyph)
    ## Bokeh Widget and JS Code ##############################################

    # JS code triggered whenever value slider is changed
    '''timeCallback = CustomJS(args=dict(source=source), code="""
    document.write("Pickle Called");
    var data = source.data;
    curTimeIdx = radius.value;
    for (int i = 0; i < data.color.length; i++) {
        data.color[i] =
    }
    source.change.emit();
    """)'''

    callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var f = cb_obj.value
    var time = data['time']
    time = f
    source.change.emit();
""")

    pickleCallback = CustomJS(args=dict(source=source), code="""
    document.write("Pickle Called");
    var data = source.data;
    var idx = 0;
    var value = menu.value;
    for (int i = 0; i < )


    for (int i = 0; i < data.color.length; i++) {
        data.color[i] =
    }
    source.change.emit();
    """)

    ##################################################################################
    pickleMenu = Select(title="Option:", value="foo", options=pickles, callback=pickleCallback)
    pickleCallback.args["menu"] = pickleMenu
    pickleMenu.js_on_change("value", pickleCallback)

    timeSlider = Slider(start=0, end=N[curPickle], value=1, step=1,
                title="Change Time", callback=callback)
    callback.args["time"] = timeSlider
    timeSlider.js_on_change('time', callback)
    
    html_file = codecs.open("hacknc2018.html", 'r')
    text = PreText(text = html_file.read(), width = 200, height = 400)

    layout = row(
        widgetbox(timeSlider, pickleMenu),
        plot,
        text)
    show(layout)

def make_color(array2D):
    colors = []
    for i in range(len(array2D)):
        colors.append([])

    for i in range(len(array2D)):
        for j in range(len(array2D[0])):
            colors[i] = RGB(255*array2D[i][j], 20, 180*(1-array2D[i][j]))

    return colors

startup()
