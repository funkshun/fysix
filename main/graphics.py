import numpy as np


import codecs
import simulator
import holoviews as hv
from bokeh.layouts import row, widgetbox
from bokeh.models import CustomJS, Slider, DataRange1d, Plot, LinearAxis, Grid, HoverTool, Dropdown, Select, Button, Div
from bokeh.plotting import figure, output_file, show, ColumnDataSource, gridplot
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

    source0 = ColumnDataSource(dict(x=X[0], y=Y[0],
        r=R[0], colors=colors[0], name=sub_reference[0]))

    source1 = ColumnDataSource(dict(x=X[1], y=Y[1],
        r=R[1], colors=colors[1], name=sub_reference[1]))

    source2 = ColumnDataSource(dict(x=X[2], y=Y[2],
        r=R[2], colors=colors[2], name=sub_reference[2]))

#    source3= ColumnDataSource(dict(x=X[3], y=Y[3],
#        r=R[3], colors=colors[3], name=sub_reference[3]))


    plot0 = figure(
        title=None, x_range=xdr, y_range=ydr, plot_width=300, plot_height=250,
        h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location = None)
    plot0.axis.visible = None
    plot0.xgrid.visible = False
    plot0.ygrid.visible = False

    plot0.add_tools(HoverTool(
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
                plot0.line([x[i], x[j]], [y[i], y[j]],
                    line_width = np.random.randint(7), line_color = lineColor)


    # Add all the glyphs to the main plot
    glyph = Circle(x="x", y="y", size="r", fill_color="colors", line_width=1)
    plot0.add_glyph(source0, glyph)


    plot1 = figure(
        title=None, x_range=xdr, y_range=ydr, plot_width=300, plot_height=250,
        h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location = None)
    plot1.axis.visible = None
    plot1.xgrid.visible = False
    plot1.ygrid.visible = False

    plot1.add_tools(HoverTool(
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
                plot1.line([x[i], x[j]], [y[i], y[j]],
                    line_width = np.random.randint(7), line_color = lineColor)


    # Add all the glyphs to the main plot
    glyph = Circle(x="x", y="y", size="r", fill_color="colors", line_width=1)
    plot1.add_glyph(source1, glyph)


    plot2 = figure(
        title=None, x_range=xdr, y_range=ydr, plot_width=300, plot_height=250,
        h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location = None)
    plot2.axis.visible = None
    plot2.xgrid.visible = False
    plot2.ygrid.visible = False

    plot2.add_tools(HoverTool(
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
                plot2.line([x[i], x[j]], [y[i], y[j]],
                    line_width = np.random.randint(7), line_color = lineColor)


    # Add all the glyphs to the main plot
    glyph = Circle(x="x", y="y", size="r", fill_color="colors", line_width=1)
    plot2.add_glyph(source2, glyph)

    '''

    plot3 = figure(
        title=None, x_range=xdr, y_range=ydr, plot_width=1100, plot_height=700,
        h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location = None)
    plot3.axis.visible = None
    plot3.xgrid.visible = False
    plot3.ygrid.visible = False

    plot3.add_tools(HoverTool(
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
                plot3.line([x[i], x[j]], [y[i], y[j]],
                    line_width = np.random.randint(7), line_color = lineColor)


    # Add all the glyphs to the main plot
    glyph = Circle(x="x", y="y", size="r", fill_color="colors", line_width=1)
    plot3.add_glyph(source, glyph)
    '''


    ## Bokeh Widget and JS Code ##############################################
    '''
    callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var time = time.value;
        var A = amp.value;
        var k = freq.value;
        var phi = phase.value;
        var B = offset.value;
        var color = data['colors']
        var y = data['y']
        for (var i = 0; i < x.length; i++) {
            y[i] = B + A*Math.sin(k*x[i]+phi);
        }
        source.change.emit();
    """)




    ##################################################################################
    pickleMenu = Select(title="Option:", value="foo", options=pickles, callback=callback)
    callback.args["menu"] = pickleMenu
    pickleMenu.js_on_change("value", callback)

    timeSlider = Slider(start=0, end=N[curPickle], value=1, step=1,
                title="Change Time", callback=callback)
    callback.args["timeSlider"] = timeSlider
    timeSlider.js_on_change('time', callback)'''

    html_file = open('hacknc2018.html', 'r')
    text = Div(text = html_file.read(), width = 400, height = 400)

    layout = row(
        #widgetbox(timeSlider, pickleMenu),
        gridplot([plot0, plot1], [plot2]),
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
