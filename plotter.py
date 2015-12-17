import pygame

class Plotter:
	def __init__(self, w, h, max_y):
		self.w = w
		self.h = h
		self.max_y = 0
		self.border = 50
		self.surf = pygame.Surface((w, h))
		self.datas = []

	def getSubset(self, l, vals):
		if len(l) <= vals:
			return l

		dat = []

		for i in range(vals):
			dat.append(l[int(i * len(l) / float(vals))])

		return dat

	def DrawText(self, color, x_val, x_text, y_val, y_text):
		size = int(self.border * 3.0 / 5)
		f = pygame.font.Font(None, size)

		text = f.render(str(x_val), 1, color)
		self.surf.blit(text, (self.w - self.border - text.get_width(), self.h - self.border))
		text = f.render(str(0), 1, color)
		self.surf.blit(text, (self.border, self.h - self.border))
		text = f.render(x_text, 1, color)
		self.surf.blit(text, (self.w / 2 - text.get_width() / 2, self.h - self.border))

		text = f.render(str(y_val), 1, color)
		self.surf.blit(text, (self.border - text.get_width(), self.border - size))
		text = f.render(str(0), 1, color)
		self.surf.blit(text, (self.border - text.get_width(), self.h - self.border - size))
		text = f.render(y_text, 1, color)
		text = pygame.transform.rotate(text, 90)
		self.surf.blit(text, (self.border - text.get_width(), self.h / 2 - text.get_height() / 2))

	def Draw(self, palette, background_color, frame_color):
		self.surf.fill(background_color)
		pygame.draw.rect(self.surf,
						 frame_color,
						 pygame.Rect(0, 0, self.w - 1, self.h - 1),
						 1)
		pygame.draw.rect(self.surf,
						 frame_color,
						 pygame.Rect(self.border,
									 self.border,
									 self.w - 1 - self.border * 2,
									 self.h - 1 - self.border * 2),
						 1)

		dat = self.getSubset(self.datas, 500)
		#dat = self.datas

		if len(dat) >= 2:
			x_factor = float(len(dat)) / float(self.w - self.border * 2)
			y_factor = float(self.max_y) / float(self.h - self.border * 2)

			for i in range(len(dat) - 1):
				pygame.draw.aaline(self.surf,
								  palette[i % len(palette)],
								  (self.border + int(i / x_factor),
								   self.h - self.border - int(dat[i] / y_factor)),
								  (self.border + int((i + 1) / x_factor),
								   self.h - self.border - int(dat[i + 1] / y_factor)))

		self.DrawText((255, 255, 255), len(self.datas), 'Iterations', self.max_y, 'Manhattan distance')

	def getSurface(self):
		return self.surf

	def pushData(self, data):
		self.datas.append(data)
		if (data > self.max_y):
			self.max_y = data
