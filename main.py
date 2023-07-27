import pygame as pg

resolution = width, height = (1600, 900)

class App:
    def __init__(self):
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            pg.display.flip()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {self.clock.get_fps() :.2f}')


if __name__ == '__main__':
    app = App()
    app.run()