from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_WIDTH, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_dir = - 2

        if self.name == 'Enemy3':
            self.vertical_dir = 1

    def move(self):
        if self.name == 'Enemy3':
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.rect.centery += ENTITY_SPEED[self.name] * self.vertical_dir

            if self.rect.top <= 0:
                self.vertical_dir = 2
            elif self.rect.bottom >= WIN_HEIGHT:
                self.vertical_dir = -1
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
