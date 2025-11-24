class Paralelepiped:
    
    def __init__(self, length, width, height): 
        self.l = float(length) 
        self.w = float(width)  
        self.h = float(height) 

    def total_surface_area(self): 
        area = 2 * (self.l * self.w + self.l * self.h + self.w * self.h)
        return area

    def volume(self): 
        volume = self.l * self.w * self.h
        return volume