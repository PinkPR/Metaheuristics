import sys
import graph
import StatisticalCooling
import pygame
import time
import plotter
import colors
import numpy
import math
import infoprinter

RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)

window_size = (1024, 1024)
pygame.font.init()
screen = pygame.display.set_mode(window_size)
graph_surf = pygame.Surface((512, 512))
plt = plotter.Plotter(1024, 512, 0)
ip = infoprinter.InfoPrinter(512, 512)
g = graph.Graph(sys.argv[2])
sc = StatisticalCooling.Algo(int(sys.argv[3]), float(sys.argv[4]), g, 200, 20000)

init_t = time.clock()

if sys.argv[1] == 'draw':
	g.Draw((512, 512), graph_surf, colors.PASTEL_PLT)
	screen.blit(graph_surf, (0, 0))

elif sys.argv[1] == 'run':
	while True:
		g2, m2 = sc.Run()

		if not g2:
			break
		g = g2
		g.Draw((512, 512), graph_surf, colors.PASTEL_PLT)
		plt.pushData(m2)
		plt.Draw(colors.PASTEL_PLT, BLACK, GREEN)
		screen.blit(graph_surf, (0, 0))
		screen.blit(plt.getSurface(), (0, 512))
		ip.PrintInfos([('Temperature', round(sc.t, 3)), ('Iterations', sc.iter_cnt), ('Elapsed seconds', time.clock() - init_t)], (255, 255, 255))
		screen.blit(ip.getSurface(), (512, 0))
		pygame.display.flip()

pygame.image.save(screen, 'image.jpg')
