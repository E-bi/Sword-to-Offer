class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,value):
        self._width = value

    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width*self._height
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000
s = Screen()
s.width = 1024
s.height = 768
print('resolution=',s.resolution)
    
