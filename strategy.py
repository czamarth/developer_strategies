import random

class Strategy():
    def __init__(self, filename):
        # type: (object) -> object
        """

        :rtype: object
        """
        try:
            f = open(filename, 'r')
            self.contents = f.readlines()
            f.close()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            raise

    def get_strategy(self):
        return random.choice(self.contents)