%module RHS
%{
#include "RHS.h"
 %}

%include "std_strings.i"

%nodefaultctor RHS; // Disables the default constructor for class RHS

class RHS {
 public:
  RHS(bool legacySubclass); // may need to overload and always pass false to it?

  bool nonZeroRHS(int testVarID);
  
  void addTerm(LinearTermPtr rhsTerm);
  void addTerm(VarPtr v);
  
  LinearTermPtr linearTerm();
  LinearTermPtr linearTermCopy();
};
