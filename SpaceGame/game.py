import turtle
import winsound
import math
import random


# SCREEN
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

sc = turtle.Screen()
sc.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
sc.title("Space Arena Online")
winsound.PlaySound('loading.wav', winsound.SND_ASYNC)
sc.bgpic("bg_nebula_2.gif")
Player_Name = sc.textinput("Jogador", "Seu Nick: ")
sc.tracer(0)

turtle.register_shape("asteroid_2.gif")
turtle.register_shape("Eye_Hunter.gif")
turtle.register_shape("Mine_Explosive.gif")
turtle.register_shape("Speeder.gif")

# PEN FOR DRAW THE SPRITES
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('green')
pen.penup()
pen.hideturtle()


class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.alive_enemies = self.level + 2
        self.asteroids = self.level + 2

    def Start_level(self):
        winsound.PlaySound("start-level.wav", winsound.SND_ASYNC)
        sprites.clear()

        sprites.append(player)
        for laser in lasers:
            sprites.append(laser)
        for enemy_laser in enemy_lasers:
            sprites.append(enemy_laser)

        for _ in range(self.level + 2):
            x = random.randint(-self.width / 2, self.width / 2)
            y = random.randint(-self.height / 2, self.height / 2)
            dx = -1.0
            dy = -1.0
            sprites.append(Enemy(x, y, "red", "square"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy
            sprites[-1].health = 100 * self.level / 2
            sprites[-1].max_health = 100 * self.level / 2

        for _ in range(self.level + 2):
            x = random.randint(-self.width / 2, self.width / 2)
            y = random.randint(-self.height / 2, self.height / 2)
            dx = 1.0
            dy = 0.7
            sprites.append(Asteroides(x, y, "brown", "asteroid_2.gif"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

    def draw_border(self, pen, x_fora, y_fora):
        pen.color('green')
        pen.width(3)
        pen.penup()

        left = -self.width / 2.0 - x_fora
        right = self.width / 2.0 - x_fora
        top = self.height / 2.0 - y_fora
        bottom = -self.height / 2.0 - y_fora

        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

    def render_info(self, pen, score, alive_enemies=0):
        pen.color("#222255")
        pen.penup()
        pen.goto(750, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(18, 48, None)
        pen.stamp()

        pen.color("green")
        pen.width(3)
        pen.goto(570, 480)
        pen.pendown()
        pen.goto(570, -480)
        pen.goto(930, -480)
        pen.goto(930, 480)
        pen.goto(570, 480)
        pen.penup()

        character_pen.scale = 1.0
        pen.color("white")
        character_pen.draw_string(pen, "ALIEN RAMPAGE", 750, 450)
        character_pen.draw_string(pen, "LEVEL: {}".format(game.level), 750, 410)
        character_pen.draw_string(pen, "SCORE: {}".format(player.score), 750, 370)
        character_pen.draw_string(pen, "ENEMIES: {}".format(game.alive_enemies), 750, 330)
        character_pen.draw_string(pen, "ASTEROIDS: {}".format(game.asteroids), 750, 290)
        character_pen.draw_string(pen, "RESOURCES: {}".format(player.resources), 750, 250)
        character_pen.draw_string(pen, "{}'S LIVES: {}".format(Player_Name, player.lives), 750, 210)
        character_pen.draw_string(pen, "{}'S DAMAGE: {}".format(Player_Name, player.damage), 750, 170)
        character_pen.draw_string(pen, "RADAR", 750, -100)


class CharacterPen():
    def __init__(self, color="white", scale=1.0):
        self.color = color
        self.scale = scale

        self.characters = dict()
        self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["2"] = ((-5, 10), (5, 10), (5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10), (5, 10), (5, 0), (0, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2, 0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10))
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10))
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10))
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0, 0), (0, -10))
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))
        self.characters["-"] = ((-3, 0), (3, 0))
        self.characters["."] = ((-1, -10), (1, -10))
        self.characters["'"] = ((0, 10), (0, 8))

    def draw_string(self, pen, str, x, y):
        pen.width(2)
        pen.color(self.color)

        x -= 15 * self.scale * ((len(str) - 1) / 2)
        for character in str:
            self.draw_character(pen, character, x, y)
            x += 15 * self.scale

    def draw_character(self, pen, character, x, y):
        scale = self.scale

        character = character.upper()

        if character in self.characters:
            pen.penup()
            xy = self.characters[character][0]
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()

            for i in range(1, len(self.characters[character])):
                xy = self.characters[character][i]
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)

            pen.penup()


character_pen = CharacterPen("red", 3.0)


# SPRITE CLASS
class Sprite():
    def __init__(self, x, y, color, shape):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.dx = 0
        self.dy = 0
        self.heading = 90
        self.da = 0
        self.thrust = 0.0
        self.accelerate = 0.03
        self.health = 100
        self.max_health = 100
        self.width = 20
        self.height = 20
        self.state = "alive"
        self.radar = 1000
        self.max_thrust = 0.05

    def is_colision(self, other):
        if self.x < other.x + other.width and \
                self.x + self.width > other.x and \
                self.y < other.y + other.height and \
                self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy

        self.dx = other.dx
        self.dy = other.dy

        other.dx = temp_dx
        other.dy = temp_dy

    def update(self):
        self.heading += self.da
        self.heading %= 360

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

        self.border_check()

    def border_check(self):
        if self.x > game.width / 2.0 - 10:
            self.x = game.width / 2.0 - 10
            self.dx *= -1
        elif self.x < -game.width / 2.0 + 10:
            self.x = -game.width / 2.0 + 10
            self.dx *= -1
        if self.y > game.height / 2.0 - 10:
            self.y = game.height / 2.0 - 10
            self.dy *= -1
        elif self.y < -game.height / 2.0 + 10:
            self.y = -game.height / 2.0 + 10
            self.dy *= -1

    def render(self, pen, x_fora, y_fora):
        if self.state == "alive":
            pen.goto(self.x - x_fora, self.y - y_fora)
            pen.setheading(self.heading)
            pen.color(self.color)
            pen.shape(self.shape)
            pen.stamp()
            self.render_health(pen, x_fora, y_fora)

    def render_health(self, pen, x_fora, y_fora):
        pen.goto(self.x - x_fora - 10, self.y - y_fora + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)
        if self.health / self.max_health < 0.3:
            pen.color('red')
        elif self.health / self.max_health < 0.7:
            pen.color('yellow')
        else:
            pen.color('green')

        pen.fd(20 * (self.health / self.max_health))
        if self.health != self.max_health:
            pen.color('grey')
            pen.fd(20 * ((self.max_health - self.health) / self.max_health))

        pen.penup()


#SEN FUNCTION FOR FIND THE ANGLE BETWEN PLAYER AND ENEMY
def seno(x, y, x1, y1, x2, y2):

    d_enemy_player = ((x - x1) ** 2) + ((y - y1) ** 2)
    d_enemy_player = math.sqrt(d_enemy_player)

    d_player_x = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    d_player_x = math.sqrt(d_player_x)

    Seno = float(d_player_x / d_enemy_player)
    angulo = int(((Seno / 0.017452) * 1.1))

    if x1 < x and y1 > y:
        angulo += 90
    else:
        angulo = angulo
    if x1 < x and y1 < y:
        angulo += 180
    else:
        angulo = angulo
    if x1 > x and y1 < y:
        angulo += 270
    else:
        angulo = angulo


    return angulo


class Player(Sprite):
    def __init__(self, x, y, color, shape):
        Sprite.__init__(self, 0, 0, color, shape)
        self.heading = 90
        self.lives = 5
        self.resources = 0
        self.damage = 10
        self.score = 0
        self.da = 0

    def booster(self):
        self.thrust += self.accelerate
        if self.thrust > self.max_thrust:
            self.thrust = self.max_thrust

    def stop_booster(self):
        self.thrust = 0.0

    def stop_rotate(self):
        self.da = 0

    def rotate_left(self):
        self.da = 4

    def rotate_right(self):
        self.da = -4

    def fire(self):
        energy = 0
        for laser in lasers:
            if laser.state == "ready":
                energy += 1
        if energy == 1:
            for laser in lasers:
                if laser.state == "ready":
                    laser.fire(self.x, self.y, self.heading, self.dx, self.dy)
        if energy == 2:
            directions = [-10, 10]
            for laser in lasers:
                if laser.state == "ready":
                    laser.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy)
        if energy == 3:
            directions = [0, -10, 10]
            for laser in lasers:
                if laser.state == "ready":
                    laser.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy)

    def update(self):
        if self.state == "alive":
            self.heading += self.da
            self.heading %= 360

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

            self.x += self.dx
            self.y += self.dy

            self.border_check()

            # health check
            if self.health <= 0:
                self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.health = self.max_health
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1

    def render(self, pen, x_fora, y_fora):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x - x_fora, self.y - y_fora)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

        pen.shapesize(1.0, 1.0, None)
        self.render_health(pen, x_fora, y_fora)

class Enemy_Laser(Sprite):
    def __init__(self, x, y, color, shape):
        Sprite.__init__(self, x, y, color, shape)
        self.state = "ready"
        self.thrust = 5.0
        self.max_fuel = 300
        self.fuel = self.max_fuel
        self.width = 4
        self.height = 4

    def Enemy_fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()
            self.heading += self.da
            self.heading %= 360

            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    def render(self, pen, x_fora, y_fora):
        if self.state == "active":
            pen.shapesize(0.2, 0.4, None)
            pen.goto(self.x - x_fora, self.y - y_fora)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

            pen.shapesize(1.0, 1.0, None)


class Lasers(Sprite):
    def __init__(self, x, y, color, shape):
        Sprite.__init__(self, x, y, color, shape)
        self.state = "ready"
        self.thrust = 5.0
        self.max_fuel = 300
        self.fuel = self.max_fuel
        self.width = 4
        self.height = 4

    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            winsound.PlaySound("laser_bean.wav", winsound.SND_ASYNC)

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()
            self.heading += self.da
            self.heading %= 360

            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    def render(self, pen, x_fora, y_fora):
        if self.state == "active":
            pen.shapesize(0.2, 0.4, None)
            pen.goto(self.x - x_fora, self.y - y_fora)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

            pen.shapesize(1.0, 1.0, None)


class Enemy(Sprite):
    def __init__(self, x, y, color, shape):
        Sprite.__init__(self, x, y, color, shape)
        self.type = random.choice(["hunter", "speeder", "mine"])
        self.max_speed = 2

        if self.type == "hunter":
            self.color = "red"
            self.shape = "Eye_Hunter.gif"

        if self.type == "speeder":
            self.color = "pink"
            self.shape = "Speeder.gif"

        if self.type == "mine":
            self.color = "grey"
            self.shape = "Mine_Explosive.gif"

    def update(self):
        if self.state == "alive":
            self.heading = self.da
            self.heading %= 360

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

            self.x += self.dx
            self.y += self.dy

            self.border_check()

            # health check
            if self.health <= 0:
                self.reset()

            if self.type == "hunter":
                if self.x < player.x:
                    self.dx += 0.05
                elif self.x > player.x:
                    self.dx -= 0.05
                if self.y < player.y:
                    self.dy += 0.05
                elif self.y > player.y:
                    self.dy -= 0.05
                    for enemy_laser in enemy_lasers:
                        if enemy_laser.state == "ready":
                            shot_heading = seno(int(self.x), int(self.y), int(player.y), int(player.y),
                                                     int(player.x), int(self.y))
                            enemy_laser.Enemy_fire(self.x, self.y, shot_heading, self.dx, self.dy)


            if self.type == "speeder":
                if self.x < player.x:
                    self.dx -= 0.05
                elif self.x > player.x:
                    self.dx += 0.05
                if self.y < player.y:
                    self.dy -= 0.05
                elif self.y > player.y:
                    self.dy += 0.05

            if self.type == "mine":
                self.dx = 0
                self.dy = 0

            if self.dx > self.max_speed:
                self.dx = self.max_speed

            elif self.dx < -self.max_speed:
                self.dx = -self.max_speed

            elif self.dy > self.max_speed:
                self.dy = self.max_speed

            elif self.dy < -self.max_speed:
                self.dy = -self.max_speed

    def reset(self):
        self.state = "dead"
        player.score += 100
        player.resources += 25
        game.alive_enemies -= 1
        winsound.PlaySound("scream.wav", winsound.SND_ASYNC)


class Asteroides(Sprite):
    def __init__(self, x, y, color, shape):
        Sprite.__init__(self, x, y, color, shape)

    def update(self):
        if self.state == "alive":
            self.heading += self.da
            self.heading %= 360

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

            self.x += self.dx
            self.y += self.dy

            self.border_check()

            # health check
            if self.health <= 0:
                self.reset()

    def reset(self):
        self.state = "dead"
        player.resources += 50
        player.damage += 10 * (game.level / 2)
        player.score += 50
        game.asteroids -= 1
        winsound.PlaySound("Explosion+7.wav", winsound.SND_ASYNC)


class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y


class Radar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, pen, sprites):

        # draw radar
        pen.setheading(90)
        pen.color("green")
        pen.goto(self.x + self.width / 2.0, self.y)
        pen.pendown()
        pen.circle(self.width / 2.0)
        pen.penup()

        # draw sprites
        for sprite in sprites:
            if sprite.state == "alive":
                radar_x = self.x + (sprite.x - player.x) * (self.width / game.width)
                radar_y = self.y + (sprite.y - player.y) * (self.height / game.height)
                pen.goto(radar_x, radar_y)
                pen.color(sprite.color)
                pen.shape(sprite.shape)
                pen.setheading(sprite.heading)
                pen.shapesize(0.1)
                distancia = ((player.x - sprite.x) ** 2 + (player.y - sprite.y) ** 2) ** 0.5
                if distancia < player.radar:
                    pen.stamp()


# game objects
game = Game(3000, 2000)

# creating radar
radar = Radar(750, -300, 300, 300)

# CREATING OBJECTS
player = Player(0, 0, "white", "triangle")

# CREATING CAMERA
camera = Camera(player.x, player.y)

# LASERS
enemy_lasers = []
for _ in range(1):
    enemy_lasers.append(Enemy_Laser(0, 100, 'green', 'circle'))
lasers = []
for _ in range(3):
    lasers.append(Lasers(0, 100, 'yellow', 'triangle'))

sprites = []

game.Start_level()

sc.listen()
sc.onkeypress(player.rotate_left, 'Left')
sc.onkeypress(player.rotate_right, 'Right')

sc.onkeyrelease(player.stop_rotate, 'Left')
sc.onkeyrelease(player.stop_rotate, 'Right')

sc.onkeypress(player.booster, 'Up')
sc.onkeyrelease(player.stop_booster, 'Up')

sc.onkeypress(player.fire, 'space')

# LOOPING PRINCIPAL
while True:
    # limpar a tela
    pen.clear()

    # UPDATE SPRITES
    for sprite in sprites:
        sprite.update()

    # checar colisoes
    for sprite in sprites:
        if isinstance(sprite, Enemy):
            if player.is_colision(sprite):
                player.health -= 33
                sprite.health -= 33
                player.bounce(sprite)
            for laser in lasers:
                if laser.state == 'active' and laser.is_colision(sprite):
                    sprite.health -= player.damage
                    laser.reset()
        if isinstance(sprite, Asteroides):
            for laser in lasers:
                if laser.state == 'active' and laser.is_colision(sprite):
                    sprite.health -= player.damage
                    laser.reset()

    # renderizar sprites
    for sprite in sprites:
        sprite.render(pen, camera.x + 100, camera.y)

    # desenhar tela
    game.draw_border(pen, camera.x + 100, camera.y)

    # checar fim do level
    level_finish = True
    for sprite in sprites:
        if isinstance(sprite, Enemy) and sprite.state == "alive":
            level_finish = False
    if level_finish:
        game.level += 1
        game.asteroids = game.level + 2
        game.alive_enemies = game.level + 2
        game.Start_level()

    # update camera
    camera.update(player.x, player.y)

    # draw info
    game.render_info(pen, 0, 0)

    # render rada
    radar.render(pen, sprites)
    if player.lives == 0:
        quit()
    # atualizar tela
    sc.update()
