import numpy as np

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
    maxSubreddits = 0
    maxTimeSteps = 0
    subreddits = np.array([])
    connections = np.array([])

    for pickle in pickles:
        sim_tuple = simulator.simulate(pickle)
        connections = sim_tuple[0]
        subreddits = sim_tuple[1]
        if len(subreddits) > maxSubreddits:
            maxSubreddits = len(subreddits)
        if np.max(len(list(subreddits.values())) > maxTimeSteps):
            maxTimeSteps = len(subreddits.values())

    launch(subreddits, connections, maxSubreddits, maxTimeSteps)


def launch(allSubreddits, allConnections, maxSubreddits, maxTimeSteps):
    # Matrices containing constants for each pickles
    numPickles = len(pickles)

    # Store the position, number of subreddits, a
    X = np.zeros((numPickles, maxSubreddits))
    Y = np.zeros((numPickles, maxSubreddits))
    R = np.zeros((numPickles, maxSubreddits))
    N = np.zeros((numPickles, maxSubreddits))
    names = {}
    for i in range(numPickles):
        names = names.append('')

    infected = np.zeros((numPickles, maxSubreddits, maxTimeSteps))
    colors = np.zeros((numPickles, maxSubreddits, maxTimeSteps))

    ## Unload parameters #######################################################
    for l in range(len(allSubreddits)):
        subreddits = allsubReddits[l]
        connections = allConnections[l]
        total = len(connections) # Number of SubReddits Investigated
        timeSteps = len(subreddits.values(0)) # Length of the arrays (number of time steps)
        x = np.zeros(N) # x Position
        y = np.zeros(N) # y position
        r = np.zeros(N) # radius of node
        thisColors = np.zeros([]) # Color for each node at each time
        names = np.array([]) # SubReddit name
        thisInfected = np.array([])

        for name in subreddits: # Loop through dictionary and store keys and values in arrays
            names = np.append(names, name)
            infected = np.append(infected, subreddits[name])

            for i in range(N): # For each sub reddit
                x[i] = np.random.randint(N) # point's x value
                y[i] = np.random.randint(N) # point's y value
                r[i] = np.random.randint(40, 60) # radius
                subs[i] = np.random.randint(40, 60) # radius
                for j in range(10):
                    thisInfected[i][j] = 1
                    thisColors[i][j] = RGB(255*infected[i], 20, 180*(1-infected[i]))
        #Add the current subreddit data to the Matrices
        X[l] = x
        Y[l] = y
        R[l] = r
        N[l] = total
        infected[l] = thisInfected
        colors[l] = thisColors

        ## Plotting code ########################################################

    xdr = DataRange1d()
    ydr = DataRange1d()

    source = ColumnDataSource(dict(x=X[0], y=Y[0], r=R[0], infect = infected[0], subs = sub[0]))

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
            ('Subscriber Count', '@subs')
            ]
        ))

    # Add lines connecting each glyph
    for i in range(N):
        for j in range(N):
            if j <= i:
                rgbval = 255 - 255*connections[i][j] # Shade from white to black based on connection strength
                lineColor = RGB(rgbval, rgbval, rgbval)
                width = connections[i][j]
                plot.line([x[i], x[j]], [y[i], y[j]], line_width = np.random.randint(7), line_color = lineColor)

    curTimeIdx = 0

    # Add all the glyphs to the main plot
    glyph = Circle(x="x", y="y", size="r", fill_color="colors", line_width=1)
    plot.add_glyph(source, glyph)
    ## Bokeh Widget and JS Code ##############################################

    # JS code triggered whenever value slider is changed
    timeCallback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    curTimeIdx = radius.value;
    for (int i = 0; i < data.color.length; i++) {
        data.color[i] =
    }
    source.change.emit();
    """)

    pickleCallback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    curTimeIdx = radius.value;
    for (int i = 0; i < data.color.length; i++) {
        data.color[i] =
    }
    source.change.emit();
    """)

    ##################################################################################
    picleMenu = Select(title="Option:", value="foo", options=["#M", "bar", "baz", "quux"])

    timeSlider = Slider(start=0, end=N, value=1, step=1,
                title="Change Time", callback=timeCallback)
    timeCallback.args["time"] = timeSlider

    text = PreText(text = """
    This will be HTML-compatible text
    """, width = 200, height = 400)

    layout = row(
        widgetbox(timeSlider, text),
        plot)

    show(layout)


startup()
