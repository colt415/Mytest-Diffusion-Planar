// Diffusion in 2D planar geometry with adiabatic boundary condition.

#include <bout.hxx>
#include <boutmain.hxx>

Field3D T;
BoutReal k_coff;

int physics_init(bool restarting)
{
  Field2D T0;
  k_coff=1.0;

  mesh->get(T0,"temperature");
//  mesh->get(g,"g");
//  Options *options = Options::getRoot();
//  options = options->getSection("gas");
//  options->get("k_coff", k_coff, 1.0);

  bout_solve(T,"temperature");

  if(!restarting){
    T+=T0;
  }
  
  return 0;
}


int physics_run(BoutReal t){
  
  mesh->communicate(T);

  ddt(T)=k_coff*Laplacian(T);

  return 0;
}  
