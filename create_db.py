from connect1 import engine
from creatingtable import *

print(">>>creating the object")
meta_obj.create_all(bind=engine)