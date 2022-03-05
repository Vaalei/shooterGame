from html import entities
from ursina import *
from random import random

class attack:
    def light(user):
        swing = Entity(parent=user, model='cube', scale=(.25,1,1), position=(0,.5, 0), color=color.black, collider='box', collision = False)
        swing.world_parent = scene
        swing.animate_position(swing.position+(swing.right*10), curve=curve.linear, duration=.1)
        destroy(swing, delay=.1)
        

    def heavy(user):
        swing = Entity(parent=user, model='cube', scale=(.3, 2, 1), origin=(0,1,0), color=color.black, collider='box', collision = False)
        swing.world_parent = scene
        swing.animate_rotation((0,0,10), curve=curve.linear, duration=.2)
        destroy(swing, delay=.2)

    def shoot(user, spread=0):
        global bullet
        bullet = Entity(parent=user, model='cube', scale=1, color=color.black, collider='box', collision = False)
        bullet.world_parent = scene
        bullet.animate_position(bullet.up+(bullet.forward*500), curve=curve.linear, duration=2)
        destroy(bullet, delay=2)
