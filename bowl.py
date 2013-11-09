from thinkbayes import Pmf

class Bowl(object):
    """
    Holds the numbers and types cookies in a bowl
    """

    def __init__(self, cookies):
        self.cookies = cookies


    def Remove(self, cookie):
        # remove a cookie
        try:
            if self.cookies[cookie] == 0:
                raise IndexError
            self.cookies[cookie] -= 1
        except IndexError:
            raise

    def total(self):
        return 1.0 * sum(self.cookies.values())


    def __repr__(self):
        return '\n'.join(['%s: %s' % (k, v, )for k, v in self.cookies.items()])


    def __getitem__(self, item):
        return self.cookies[item]
