
class AutoInit(type):
  def __new__(meta, classname, supers, classdict):
    return type.__new__(meta, classname, supers, classdict)