import sys
import graph
import StatisticalCooling

window_size = [512, 512]

g = graph.Graph('result')
size(*window_size)
background('lightgray')

def Draw(gr):
    clear()
    pen(7)
    stroke('orchid')
    gr.DrawLines(window_size, line)
    reset()

    fill('pink')
    stroke('salmon')
    strokewidth(6)
    gr.DrawSquares(window_size, rect)
    reset()

Draw(g)
