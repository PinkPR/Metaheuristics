import pygame

class InfoPrinter:
	def __init__(self, w, h):
		self.surf = pygame.Surface((w, h))

	def PrintInfos(self, info_list, border_color, text_color):
		size = int(len(info_list) * 0.8)
		f = pygame.font.Font(None, size)
		i = 0

		for i in info_list:
			text = f.render(i[0] + ' : ' + str(i[1]), 1, text_color)
			self.surf.blit(text, (i * self.h / len(info_list)), self.w / 2 - text.get_width() / 2)

	def getSurface(self):
		return self.surf
