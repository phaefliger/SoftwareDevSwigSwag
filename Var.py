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
            fp, pathname, description = imp.find_module('_Var', [dirname(__file__)])
        except ImportError:
            import _Var
            return _Var
        if fp is not None:
            try:
                _mod = imp.load_module('_Var', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Var = swig_import_helper()
    del swig_import_helper
else:
    import _Var
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


HGRAD = _Var.HGRAD
HCURL = _Var.HCURL
HDIV = _Var.HDIV
HGRAD_DISC = _Var.HGRAD_DISC
HCURL_DISC = _Var.HCURL_DISC
HDIV_DISC = _Var.HDIV_DISC
HDIV_FREE = _Var.HDIV_FREE
L2 = _Var.L2
CONSTANT_SCALAR = _Var.CONSTANT_SCALAR
VECTOR_HGRAD = _Var.VECTOR_HGRAD
VECTOR_HGRAD_DISC = _Var.VECTOR_HGRAD_DISC
VECTOR_L2 = _Var.VECTOR_L2
UNKNOWN_FS = _Var.UNKNOWN_FS
class Var(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Var, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Var, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _Var.delete_Var
    __del__ = lambda self : None;
Var_swigregister = _Var.Var_swigregister
Var_swigregister(Var)

class VarPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VarPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VarPtr, name)
    __repr__ = _swig_repr
    def __deref__(self): return _Var.VarPtr___deref__(self)
    def __init__(self): 
        this = _Var.new_VarPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Var.delete_VarPtr
    __del__ = lambda self : None;
VarPtr_swigregister = _Var.VarPtr_swigregister
VarPtr_swigregister(VarPtr)

# This file is compatible with both classic and new-style classes.

