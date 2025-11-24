import geometry
import Plants 

box1 = geometry.Paralelepiped(10, 5, 2) 

area = box1.total_surface_area()
volume = box1.volume()

print(f"Повна площа поверхні: {area}")
print(f"Об'єм: {volume}")

oak = Plants.Tree(age=50)
oak.display_species()
oak.grow(10) 

cherry_baum = Plants.Cherry(age=5, variety="Drogana Yellow")
cherry_baum.grow(2)  
cherry_baum.set_harvest_status(True)
cherry_baum.display_info()