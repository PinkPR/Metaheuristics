import pygame

class InfoPrinter:
	def __init__(self, w, h):
		self.surf = pygame.Surface((w, h))
		self.w = w
		self.h = h

	def PrintInfos(self, info_list, text_color):
		self.surf.fill((0, 0, 0))
		size = 50
		f = pygame.font.Font(None, size)
		cnt = 0

		for i in info_list:
			text = f.render(i[0] + ' : ' + str(i[1]), 1, text_color)
			self.surf.blit(text, (0, 50 + cnt * size))
			cnt += 1

	def getSurface(self):
		return self.surf
