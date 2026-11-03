# layer 0: 배경
# layer 1: 소년, 공
world = [[], []]


def add_object(o, depth=0):
    world[depth].append(o)


def add_objects(objects, depth=0):
    world[depth].extend(objects)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return


def update():
    for layer in world:
        for o in layer[:]:
            o.update()


def render():
    for layer in world:
        for o in layer[:]:
            o.draw()