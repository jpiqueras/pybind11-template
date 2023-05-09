#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>

#include "my_lib/my_lib.hpp"

namespace py = pybind11;

PYBIND11_MODULE(my_lib, m) {
  py::class_<LinearSystemSolver>(m, "LinearSystemSolver")
      .def(py::init<Eigen::MatrixXd>())
      .def("solve", &LinearSystemSolver::solve);
  m.def("print_package_info", &print_package_info,
        "A function that print_package_info");
}
