#calling the method from another file
import converters
#we can also call specific methods in the file 
from converters import lbs_to_kg
print(lbs_to_kg(100))

print(converters.kg_to_lbs(70))