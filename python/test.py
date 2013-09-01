###############################################################################
# Sample: New and Init.
# Classes: BaseNI.
# Description: Test the relationship between __new__() and __init__()
################################################################################
class BaseNI(float):
  #__new__ method remains classmethod dispite of overriding
  #explicit or not
  #@staticmethod
  def __new__(cls, val):
    print 'in BaseNI.__new__(): val =', val, 'cls = ', cls
    return super(cls, cls).__new__(cls, round(val, 2))
  #__init__ method could be overrided
  #@classmethod
  #@staticmethod
  def __init__(self, val):
    print 'in BaseNI.__self__(): val =', val, 'self =', self

def NI():
  print 'b = BaseNI(1.213)'
  b = BaseNI(1.213)
  print 'b =', b
  print BaseNI.__new__
  print b.__new__


################################################################################
# Sample: Classmethod Override.
# Classes: BaseCO, ChildCO
# Description: Test that if overriding parent's classmethod would reserve its
#              class method property.
################################################################################
class BaseCO(object):
  @classmethod
  def foo(cls):
    print 'in BaseCO.foo(), cls :', cls

class ChildCO(BaseCO):
  def foo(cls):
    print 'in ChildCO.foo(), cls :', cls

def CO():
  print 'BaseCO.foo:\n ', BaseCO.foo
  print 'BaseCO.foo():\n ',
  BaseCO.foo()
  print 'ChildCO.foo:\n ', ChildCO.foo
  try:
    print 'ChildCO.foo():\n ', ChildCO.foo()
  except TypeError, e:
    print 'TypeError catched:', e
  child = ChildCO()
  print 'child = ChildCO()'
  print 'child.foo:\n ', child.foo
  print 'child.foo():\n ',
  child.foo()
  print 'del ChildCO.foo'
  del ChildCO.foo
  print 'child.foo:\n ', child.foo
  print 'child.foo():\n ',
  child.foo()
  try:
    print 'ChildCO.foo():\n ',
    ChildCO.foo()
  except TypeError, e:
    print 'TypeError catched:', e

################################################################################
# Sample: Super Builtin method.
# Classes: BaseSBM, ChildSBM
# Description: Test effection of the super builtin method.
################################################################################
class BaseSBM(object):
  def objmethod(self):
    print 'in BaseSBM.objectmethod() of object:', self
  @classmethod
  def clsmethod(cls):
    print 'in BaseSBM.classmethod() of class:', cls
  @staticmethod
  def stmethod():
    print 'in BaseSBM.stmethod()'

class ChildSBM(BaseSBM):
  pass

def SBM():
  try:
    print 'BaseSBM.objmethod():'
    BaseSBM.objmethod()
  except Exception, e:
    print e
  try:
    print 'BaseSBM.clsmethod():'
    BaseSBM.clsmethod()
  except Exception, e:
    print e
  try:
    print 'BaseSBM.stmethod():'
    BaseSBM.stmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM).objmethod():'
    super(ChildSBM).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM).clsmethod():'
    super(ChildSBM).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM).stmethod():'
    super(ChildSBM).stmethod()
  except Exception, e:
    print e
  print 'b = BaseSBM()'
  b = BaseSBM()
  try:
    print 'b.objmethod():'
    b.objmethod()
  except Exception, e:
    print e
  try:
    print 'b.clsmethod():'
    b.clsmethod()
  except Exception, e:
    print e
  try:
    print 'b.stmethod():'
    b.stmethod()
  except Exception, e:
    print e
  print 'c = ChildSBM()'
  c = ChildSBM()
  try:
    print 'c.objmethod():'
    c.objmethod()
  except Exception, e:
    print e
  try:
    print 'c.clsmethod():'
    c.clsmethod()
  except Exception, e:
    print e
  try:
    print 'c.stmethod():'
    c.stmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, ChildSBM).objmethod():'
    super(ChildSBM, ChildSBM).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, ChildSBM).clsmethod():'
    super(ChildSBM, ChildSBM).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, ChildSBM).stmethod():'
    super(ChildSBM, ChildSBM).stmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, BaseSBM).objmethod():'
    super(ChildSBM, BaseSBM).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, BaseSBM).clsmethod():'
    super(ChildSBM, BaseSBM).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, BaseSBM).stmethod():'
    super(ChildSBM, BaseSBM).stmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, BaseSBM).objmethod():'
    super(BaseSBM, BaseSBM).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, BaseSBM).clsmethod():'
    super(BaseSBM, BaseSBM).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, BaseSBM).stmethod():'
    super(BaseSBM, BaseSBM).stmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, ChildSBM).objmethod():'
    super(BaseSBM, ChildSBM).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, ChildSBM).clsmethod():'
    super(BaseSBM, ChildSBM).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, ChildSBM).stmethod():'
    super(BaseSBM, ChildSBM).stmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, b).objmethod():'
    super(BaseSBM, b).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, b).clsmethod():'
    super(BaseSBM, b).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, b).stmethod():'
    super(BaseSBM, b).stmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, c).objmethod():'
    super(BaseSBM, c).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, c).clsmethod():'
    super(BaseSBM, c).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(BaseSBM, c).stmethod():'
    super(BaseSBM, c).stmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, b).objmethod():'
    super(ChildSBM, b).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, b).clsmethod():'
    super(ChildSBM, b).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, b).stmethod():'
    super(ChildSBM, b).stmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, c).objmethod():'
    super(ChildSBM, c).objmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, c).clsmethod():'
    super(ChildSBM, c).clsmethod()
  except Exception, e:
    print e
  try:
    print 'super(ChildSBM, c).stmethod():'
    super(ChildSBM, c).stmethod()
  except Exception, e:
    print e
  
  
