#!/usr/bin/env python

# filename: hardWay_3.py
# description: learning python for <<Learn Python the hard way>>:exercise 42
# author: Demon.Lee
# date: 2016.10.30

import random
import sys


class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        sys.exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print("\n")
            print("---"*20)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips=[
        "You died...",
        "Your mom would be proud of you...",
        "Such a luser...",
        "I have a small puppy that's better at this..."
    ]

    def enter(self):
        print(Death.quips[random.randint(0, len(self.quips)-1)])
        sys.exit(2)


class CentralCorridor(Scene):
    def enter(self):
        print("You enter CentralCorridor Scene now...")
        action = input("> ")
        if 'shoot' == action:
            print("you are dead. Then he eats you!")
            return 'death'
        elif 'dodge' == action:
            print("You wake up shortly after only to die...")
            return 'death'
        elif 'tell a joke' == action:
            print("Lucky for you they made you learn Gthon insults...")
            return 'laser_weapon_armory'
        else:
            print("Does not compute!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print("If you get the code wrong 10 times then the lock closes forever!")
        code="%d%d%d"%(random.randint(1,9),random.randint(1,9),random.randint(1,9))
        print("code==%s"%code)
        guess=str(input('keypad> '))
        guessTimes = 1
        while guess != code and guessTimes < 10:
            print("You are wrong!")
            guessTimes += 1
            guess = input("keypad> ")

        if guess == code:
            print("you get the code...")
            return 'the_bridge'
        else:
            print("sorry, you don't get the code...")
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print("you burst onto the Bridge with the neron...")
        action = input("> ")
        if 'throw the bomb' == action:
            print('you throw the bomb and die...')
            return 'death'
        elif 'slowly place the bomb' == action:
            print('you slowly place the bomb and escape...')
            return 'escape_pod'
        else:
            print("Does not compute...")
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print("you enter EscapePos Scene...")
        good_pod = random.randint(1,5)
        print('good_pod==%d'%good_pod)
        guess = input("[pod #]> ")
        if good_pod != int(guess):
            print("you guess error...")
            return 'death'
        else:
            print("you guess right...")
            return 'finished'


class Finished(Scene):
    def enter(self):
        print("winner...")
        sys.exit(0)


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


def testEx43():
    mp = Map('central_corridor')
    eg = Engine(mp)
    eg.play()


if '__main__' == __name__:
    testEx43()
else:
    print('being imported by another module!')

