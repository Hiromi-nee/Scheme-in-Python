class World:
    name = None
    
    def __init__(self, world_name):
        self.name = world_name

class Entity:
    unique_id = None

    def __init__(self):
        self.unique_id = 1337

class Room(Entity):
    title = None
    description = None
    objects = None
    adventurers = None
    denizens = None
    links = None
    
    def __init__(self, title):
        Entity.__init__(self)
        self.title = title

def test():
    pass

if __name__ == "__main__":
    test()
