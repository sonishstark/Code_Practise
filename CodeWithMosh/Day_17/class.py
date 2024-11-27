class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        

object1 = Point()
object1.x = 10
object1.y = 20
print(object1.x)
object1.draw()

object2 = Point()
object2.x = 30
print(object2.x)