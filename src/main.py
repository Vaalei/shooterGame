from pyexpat import model
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from attacks import *

app = Ursina()


player = PlatformerController2d(color=color.blue, scale=(.5,1,.5), position=(0,0,0), origin_z=1,max_jumps= 1, jump_height = 3)
gun = Entity(model="cube", parent=player, scale=(0.1,0.1,0.4), color=color.black, rotation=(0,90,0), position=(.5, .5, 0), collision = False)


platform = Entity(model="cube", scale=(10,1,1), position=(0,-3,0), collider= "box", color = color.black)

testplatform = Entity(model="cube", scale=(1,1,1), position=(1,0,0), collider= "box", color = color.black)

# Camera
camera.fov = 60


def update():
    camera.position = (player.x, player.y+2)
    gun.look_at_2d(testplatform, axis="z")



def input(key):
    if key == "left mouse down":
        attack.shoot(gun)
    if key == "j":
        attack.light(player)
    if key == "k":
        attack.heavy(player)

app.run()