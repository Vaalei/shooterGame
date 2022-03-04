from pyexpat import model
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
app = Ursina()


player = PlatformerController2d(color=color.blue, scale=(1,1,1), position=(0,0,0), origin=(0,-.5    25,0), max_jumps= 1, jump_height = 3)
gun = Entity(model="cube", scale=(0.3,0.1,0.1), color=color.black, parent=player, position=(.5, .5, .0525), collision = False)

platform = Entity(model="cube", scale=(10,1,1), position=(0,-3,0), collider= "box", color = color.black)


# Camera
camera.fov = 60

def update():
    camera.position = (player.x, camera.y)

def input(key):
    global bullet
    if key == "k":
        bullet = Entity(parent=gun, model='cube', scale=1, color=color.black, collider='box', collision = False)
        bullet.world_parent = scene
        bullet.animate_position(bullet.position+(bullet.right*500), curve=curve.linear, duration=2)
        destroy(bullet, delay=2)


app.run()