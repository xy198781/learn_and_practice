################################################################################
# Sample: New and Init.
# Classes: BaseNI.
# Description: Test the relationship between __new__() and __init__()
################################################################################
class BaseNI(float):
  def __new__(cls, val):
    print 'in BaseNI.__new__(): val =', val
    #return super(A, cls).__new__(cls, round(val, 2))a
    return 1
  def __init__(self, val):
    print 'in BaseNI.__self__(): val =', val


################################################################################
# Sample: Classmethod Override.
# Classes: BaseCO, ChildCO
# Description: Test that if overriding parent's classmethod would reserved its
#              class method property.
################################################################################
class BaseCO(object):
  @classmethod
  def foo(cls):
    print 'in BaseCO.foo(), cls :', cls

class ChildCO(B):
  def foo(cls):
    print 'in ChildCO.foo(), cls :', cls

