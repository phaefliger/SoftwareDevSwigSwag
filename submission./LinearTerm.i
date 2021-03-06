%module LinearTerm
%{
#include "LinearTerm.h"
%}

%include "std_string.i"
%include "Var.i"
%include "std_set.i"
%include "std_map.i"

namespace std {
    %template(IntSet) set<int>;
    %template(MapIntToFunction) map<int,FunctionPtr>;
}
using namespace std;

%nodefaultctor LinearTerm;  // Disable the default constructor for class LinearTerm        

%extend {
  FunctionPtr evaluate(const map<int, FunctionPtr> &varFunctions) {
    map<int, FunctionPtr> varFunctionsCopy = varFunctions; 
    return evaluate(varFunctionsCopy); 
  }
}

class LinearTerm {
public:                                                                                                                                                       
  const set<int> & varIDs();

  VarType termType();

  FunctionPtr evaluate(map< int, FunctionPtr> &varFunctions);

  int rank();

  string displayString();
  
  
  
  

};
//FunctionPtr operator*(double weight, FunctionPtr f);                                                                                                                               

class LinearTermPtr {
public:
  LinearTerm* operator->();

  %extend {
    LinearTermPtr __add__(LinearTermPtr t2) {
      return *self + t2;
    }
    LinearTermPtr __add__(VarPtr v) {
      return *self + v;
    }
    LinearTermPtr __radd__(VarPtr v) {
      return *self + v;
    }
    LinearTermPtr __mul__(FunctionPtr f, VarPtr v) {
      return f*v;
    }
    LinearTermPtr __mul__(VarPtr v, FunctionPtr f) {
      return f*v;
    }
    LinearTermPtr __mul__(double weight, VarPtr v){
      return weight * v;
    }
    LinearTermPtr __mul__(VarPtr v, double weight){
      return weight * v;
    }
    LinearTermPtr __mul__(vector<double> weight, VarPtr v){
      return weight * v;
    }
    LinearTermPtr __mul__(VarPtr v, vector<double> weight){
      return weight * v;
    }
    /* LinearTermPtr __rmul__(FunctionPtr f){ */
    /*   return *self * f; */
    /* } */
    LinearTermPtr __add__(VarPtr v1, VarPtr v2){
      return v1 + v2;
    }
    LinearTermPtr __div__(VarPtr v, double weight){
      return v / weight;
    }
    LinearTermPtr __div__(VarPtr v, FunctionPtr f){
      return v / f;
    }
    LinearTermPtr __sub__(VarPtr v1, VarPtr v2){
      return v1 -v2;
    }
    LinearTermPtr __neg__(VarPtr v){
      return -v;
    }
    LinearTermPtr __neg__(LinearTermPtr a){
      return -a;
    }
    LinearTermPtr __sub__(VarPtr v){
      return *self - v;
    }
    LinearTermPtr __rsub__(VarPtr v){
      return v - *self;
    }
    LinearTermPtr __sub__(LinearTermPtr a2){
      return *self - a2;
    }
  }
};
