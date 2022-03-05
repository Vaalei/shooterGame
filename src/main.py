from pyexpat import model
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from math import atan2, degrees
app = Ursina()


player = PlatformerController2d(color=color.blue, scale=(1,1,1), position=(0,0,0), origin_z=1,max_jumps= 1, jump_height = 3)
gun = Entity(model="cube", scale=(0.3,0.1,0.1), color=color.black, position=(0, 2, 0), origin=(-2, 0, 0), collision = False)

platform = Entity(model="cube", scale=(10,1,1), position=(0,-3,0), collider= "box", color = color.black)
testingText = Text(text=f"{mouse.x}, {mouse.y}")
testingText2 = Text(text=f"{player.x}, {player.y}", origin=(0,-1,0))

# Camera
camera.fov = 60
camera.position.z=0
print(camera.position)



def update():
    camera.position = (player.x, player.y+2)
    gun.position = player.position+(0,.5)
    gun.rotation_z = -degrees(atan2(mouse.y,mouse.x)) if mouse.x !=0 else [90 if mouse.y < 0 else -90]

    testingText.text=f"{mouse.x}, {mouse.y}"
    testingText2.text=f"{gun.rotation_z, camera.y-player.y}"
def input(key):
    global bullet
    if key == "left mouse down":
        bullet = Entity(parent=gun, model='cube', scale=1, color=color.black, collider='box', collision = False)
        bullet.world_parent = scene
        bullet.animate_position(bullet.position+(bullet.right*500), curve=curve.linear, duration=2)
        destroy(bullet, delay=2)


app.run()