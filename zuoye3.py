#!/usr/bin/python
# -- coding: utf-8 --
"""
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""
class Animal():
    name='panda'
    def __init__(self):
        self.name = 'dog'
        self.colour = 'black and white'
        self.age='22'
        self.Gender= 'female'
    def jump(self):
        pass
    def shout(self):
        print('会叫')
        pass
if __name__== '__main__':
    #类的实例化
    Panda1 = Animal()
    print(Panda1.name)



