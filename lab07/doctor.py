class Doctor(object):
    def __init__(self, dname, title):
        self.__dname = dname
        self.__title = title

    def getDname(self):
        return self.__dname

    def setDname(self, name):
        self.__dname = name

    def getTitle(self):
        return self.__title

    def setTitle(self, t):
        self.__title = t

    def __eq__(self, other):
        if self.__dname == other.getDname() and self.__title == other.getTitle():
            return True
        else:
            return False

    def __repr__(self):
        return self.__title + " - " + self.__dname

    def __lt__(self, other):
        if self.__title != other.getTitle():
            return self.__title < other.getTitle()
        else:
            return self.__dname < other.getDname()






