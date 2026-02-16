#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double heavy_compute(py::array_t<double> input)
{
    auto buf = input.request();
    double* ptr = static_cast<double*>(buf.ptr);

    size_t size = 1;
    for(auto r : buf.shape) size *= r;

    double sum = 0.0;

    for(size_t i = 0; i < size; ++i)
    {
        sum += ptr[i] * ptr[i];
    }

    return sum;
}

PYBIND11_MODULE(cpp_inference, m)
{
    m.def("heavy_compute", &heavy_compute);
}
