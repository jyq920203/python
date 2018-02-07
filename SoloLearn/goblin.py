def get_input():
    com = input(':').split()
    ver = com[0]
    if ver in ver_dir:
        ver = ver_dir[ver]
        print('对的')
    else:
        print('no {} in the list'.format(ver))
        return

    if len(com) >= 2:
        noun = com[1]
        print(ver(noun))
    else:
        print(ver("nothing"))


class GameObject:
    classname=""
    desc=""
    objects = {}

    def __init__(self,name):
        self.name = name
        GameObject.objects[self.classname]= self

    def get_desc(self):
        return self.classname + "\n" +self.desc

class Goblin(GameObject):
    def __init__(self,name):
        self.classname="goblin"
        self.health =3
        self._desc = "a foul creature"
        super().__init__(name)

    @property
    def de(self):
        if self.health>=3:
            return self._desc
        elif self.health==2:
            healthline = "It has a wound on its knee."
        elif self.health==1:
            healthline = "Its left arm has been cut off!"
        elif self.health<=0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line


    @de.setter
    def de(self,value):
        self._desc = value

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing)==Goblin:
            thing.health =thing.health -1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.classname)
    else:
        msg='there is no {}'.format(noun)
    return msg

goblin = Goblin("yijing")


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)


def hello(noun):
    print('nihao {}'.format(noun))


ver_dir = {
    "hello": hello,
    "hit": hit,
    "examine": examine,
}

while True:
    get_input()
