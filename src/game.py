#import resources as color

class Game():

    def __init__(self, pygame, name="Game", size=(500, 500), fps=60):
        self.pygame = pygame
        self.pygame.init()
        self.isRunning = True
        self.fps = fps
        self.clock = self.pygame.time.Clock()
        self.surface = self.pygame.display.set_mode(size, self.pygame.RESIZABLE)
        self.pygame.display.set_caption(name)

    def render(self):
        self.clock.tick(self.fps)
        self.surface.fill((255, 255, 255))
        self.pygame.display.update()

    def keys(self):
        # Get pressed keys
        keys = self.pygame.key.get_pressed()
        
        if keys[self.pygame.K_a]:
            pass

    def events(self):

        # Event loop
        for event in self.pygame.event.get():

            # Closing window
            if event.type == self.pygame.QUIT:
                self.isRunning = False

            # Resizing window
            if event.type == self.pygame.VIDEORESIZE:
                self.surface = self.pygame.display.set_mode((event.w, event.h), self.pygame.RESIZABLE)
                self.render()

    def run(self):

        # Game loop
        while self.isRunning:
            self.events()
            self.render()
            self.clock.tick(self.fps)
        self.pygame.quit()



        
