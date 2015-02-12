# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Mesh', [dirname(__file__)])
        except ImportError:
            import _Mesh
            return _Mesh
        if fp is not None:
            try:
                _mod = imp.load_module('_Mesh', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Mesh = swig_import_helper()
    del swig_import_helper
else:
    import _Mesh
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Mesh.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _Mesh.SwigPyIterator_value(self)
    def incr(self, n=1): return _Mesh.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _Mesh.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _Mesh.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _Mesh.SwigPyIterator_equal(self, *args)
    def copy(self): return _Mesh.SwigPyIterator_copy(self)
    def next(self): return _Mesh.SwigPyIterator_next(self)
    def __next__(self): return _Mesh.SwigPyIterator___next__(self)
    def previous(self): return _Mesh.SwigPyIterator_previous(self)
    def advance(self, *args): return _Mesh.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _Mesh.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _Mesh.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _Mesh.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _Mesh.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _Mesh.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _Mesh.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _Mesh.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Mesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Mesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Mesh, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def saveToHDF5(self, *args): return _Mesh.Mesh_saveToHDF5(self, *args)
    def cellPolyOrder(self, *args): return _Mesh.Mesh_cellPolyOrder(self, *args)
    def getActiveCellIDs(self): return _Mesh.Mesh_getActiveCellIDs(self)
    def hRefine(self, *args): return _Mesh.Mesh_hRefine(self, *args)
    def numActiveElements(self): return _Mesh.Mesh_numActiveElements(self)
    def numFluxDofs(self): return _Mesh.Mesh_numFluxDofs(self)
    def numFieldDofs(self): return _Mesh.Mesh_numFieldDofs(self)
    def numGlobalDofs(self): return _Mesh.Mesh_numGlobalDofs(self)
    def numElements(self): return _Mesh.Mesh_numElements(self)
    def pRefine(self, *args): return _Mesh.Mesh_pRefine(self, *args)
    def registerSolution(self, *args): return _Mesh.Mesh_registerSolution(self, *args)
    def vertexIndicesForCell(self, *args): return _Mesh.Mesh_vertexIndicesForCell(self, *args)
    def verticesForCell(self, *args): return _Mesh.Mesh_verticesForCell(self, *args)
    __swig_destroy__ = _Mesh.delete_Mesh
    __del__ = lambda self : None;
Mesh_swigregister = _Mesh.Mesh_swigregister
Mesh_swigregister(Mesh)

class MeshPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MeshPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MeshPtr, name)
    __repr__ = _swig_repr
    def __deref__(self): return _Mesh.MeshPtr___deref__(self)
    def __init__(self): 
        this = _Mesh.new_MeshPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Mesh.delete_MeshPtr
    __del__ = lambda self : None;
    def saveToHDF5(self, *args): return _Mesh.MeshPtr_saveToHDF5(self, *args)
    def cellPolyOrder(self, *args): return _Mesh.MeshPtr_cellPolyOrder(self, *args)
    def getActiveCellIDs(self): return _Mesh.MeshPtr_getActiveCellIDs(self)
    def hRefine(self, *args): return _Mesh.MeshPtr_hRefine(self, *args)
    def numActiveElements(self): return _Mesh.MeshPtr_numActiveElements(self)
    def numFluxDofs(self): return _Mesh.MeshPtr_numFluxDofs(self)
    def numFieldDofs(self): return _Mesh.MeshPtr_numFieldDofs(self)
    def numGlobalDofs(self): return _Mesh.MeshPtr_numGlobalDofs(self)
    def numElements(self): return _Mesh.MeshPtr_numElements(self)
    def pRefine(self, *args): return _Mesh.MeshPtr_pRefine(self, *args)
    def registerSolution(self, *args): return _Mesh.MeshPtr_registerSolution(self, *args)
    def vertexIndicesForCell(self, *args): return _Mesh.MeshPtr_vertexIndicesForCell(self, *args)
    def verticesForCell(self, *args): return _Mesh.MeshPtr_verticesForCell(self, *args)
MeshPtr_swigregister = _Mesh.MeshPtr_swigregister
MeshPtr_swigregister(MeshPtr)

# This file is compatible with both classic and new-style classes.

