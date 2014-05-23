from util import Util

class World(object):

    def __init__(self, name, size):
        self.name = name
        self.size = self.width, self.height = size
        self.layers = [WorldLayer((self.width, self.height))]*5

    def setBlockAt(self, x, y, layer, blockType):
        self.layers[layer].setBlockAt(x, y, blockType)

    def generate(self):
        w = self.width
        h = self.height

        for y in xrange(h):
            for x in xrange(w):
                self.setBlockAt(x, y, 1, "air")

        for y in xrange(h / 2):
            for x in xrange(w):
                self.setBlockAt(x, y, 1, "dirt")

class WorldLayer(object):

    def __init__(self, size):
        self.size = self.width, self.height = size
        self.blockModels = [[None for x in xrange(self.width)] for y in xrange(self.height)]

    def getBlockAt(self, x, y):
        return self.blockModels[x][y]

    def setBlockAt(self, x, y, blockType):
        self.blockModels[x][y] = Util.get().blockModels[blockType]
        return True
