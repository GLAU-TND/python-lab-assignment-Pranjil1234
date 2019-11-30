class MyException(Exception):
    def __init__(self,v=''):
        self.v = v
    def __str__(self):
        return str(self.v)
def xyz(a,b):
    c=a+b
    if c<=150:
        raise MyException('custom Exception occured")
    else:
        return c
print(xyz(30,40))
