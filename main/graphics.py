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
from PIL import Image


## Bokeh initialization code
hv.extension('bokeh')
output_file('Reddit Data Modelling.html')

def main():
    summary = open('hacknc2018.html', 'r')

    gifs = """
    <!DOCTYPE html>
    <html>
    <body>
    <p style = "position:absolute; TOP:50px; LEFT: 500px; WIDTH:600px">Our model predicts how interconnected subreddits might share ideas.
    In the example below, the subreddit "The_Mueller" starts with an idea. Each subreddit has a chance of "conracting" the idea based on the strengths
    of its conncetions and the concentration of the idea in the surrounding populations.
    </p>

    <img src = 'network.gif', width = 600px, height = 600px,
    IMG STYLE="position:absolute; TOP:100px; LEFT:500px; WIDTH:600px; HEIGHT:600px">

    <img src = 'legend.png', width = 400px, height = 75px,
    IMG STYLE="position:absolute; TOP:720px; LEFT:500px; HEIGHT:75px">

    <img src = 'smallpolitical_plotloop.gif', width = 600px, height = 400px,
    IMG STYLE="position:absolute; TOP:900px; LEFT:500px; WIDTH:600px; HEIGHT:600px">

    <img src = 'gaming_plotloop.gif', width = 600px, height = 400px,
    IMG STYLE="position:absolute; TOP:1500px; LEFT:500px; WIDTH:600px; HEIGHT:600px">

    <img src = 'enter.gif', width = 600px, height = 400px,
    IMG STYLE="position:absolute; TOP:2100px; LEFT:500px; WIDTH:600px; HEIGHT:600px">

    <img src = 'political_plotloop.gif', width = 600px, height = 400px,
    IMG STYLE="position:absolute; TOP:2700px; LEFT:500px; WIDTH:600px; HEIGHT:600px">

    </body>
    </html>
    """

    memeimages = """
    <!DOCTYPE html>
    <html>
    <body>

    <p style = "position:absolute; TOP:50px; LEFT: 1200px; WIDTH:400px"> We gathered some Reddit
    user data to show how viral trends looks in the real world.   The below plots show that phenomena
    such as memes experience massive surges at different times in different communities, giving
    some credence to our model.
    </p>

    <img src = 'dankmemes.png', width = 200, height = 200, align = "right",
    IMG STYLE="position:absolute; TOP:150px; LEFT:1200px; WIDTH:400px; HEIGHT:200px" >

    <img src = 'MemeEconomy.png', width = 200, height = 200, align = "right",
    IMG STYLE="position:absolute; TOP:400px; LEFT:1200px; WIDTH:400px; HEIGHT:200px">

    <img src = 'mothmemes.png', width = 200, height = 200, align = "right",
    IMG STYLE="position:absolute; TOP:650   px; LEFT:1200px; WIDTH:400px; HEIGHT:200px">

    </body>
    </html>
    """

    description = Div(text = summary.read())

    gifs = Div(text = gifs)

    memeimages = Div(text = memeimages)

    layout = row(
        description,
        gifs,
        memeimages
        )
    show(layout)


main()
