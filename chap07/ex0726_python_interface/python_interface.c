// python_interface.c
// - cpython module interface for diffusion.c

#define NPY_NO_DEPRECATED_API   NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include "cdiffusion.h"

/* Docstrings */
static char module_docstring[] = "Provides optimized method to solve the diffusion equation";
static char cdiffusion_evolve_doctring[] = "Evolve a 2D grid using the diffusion equation";

PyArrayObject *py_evolve(PyObject *, PyObject *);

/* Module spectification */
static PyMethodDef module_methods[] = 
{
    /* {method name, C function, argement types, docstring} */
    { "evolve", (PyCFunction)py_evolve, METH_VARARGS, cdiffusion_evolve_doctring},
    { NULL,     NULL,                   0,            NULL}
};

static struct PyModuleDef cdiffusionmodule  = 
{
    PyModuleDef_HEAD_INIT,
    "cdiffusion",           /* name of module */
    module_docstring,       /* module documentation, may be NULL */
    -1,                     /* size 0f per-interpreter state of the module,
                             * or -1 if the module state in global variables. 
                             */
    module_methods
};

PyArrayObject *py_evolve(PyObject *self, PyObject *args)
{
    PyArrayObject *data;
    PyArrayObject *next_grid;
    double        dt, D = 1.0;

    /* The "evolve" function will have the signature:
     *      evolve(data, next_grid, dt, D=1)
     */
    if(!PyArg_ParseTuple(args, "OOd|d", &data, &next_grid, &dt, &D))
    {
        PyErr_SetString(PyExc_RuntimeError, "Invalid arguments");
        return(NULL);
    }
    
    /* Make sure that the numpy arrays are contiguous in memory */
    if(!PyArray_Check(data) || !PyArray_ISCONTIGUOUS(data))
    {
        PyErr_SetString(PyExc_RuntimeError, "data is no contiguous array.");
        return(NULL);
    }

    if(!PyArray_Check(next_grid) || !PyArray_ISCONTIGUOUS(next_grid))
    {
        PyErr_SetString(PyExc_RuntimeError, "next_grid is no a contiguous array.");
        return(NULL);
    }

    /* Make sure that grid and next_grid are of the same type and have the same dimensions */
    if(PyArray_TYPE(data) != PyArray_TYPE(next_grid))
    {
        PyErr_SetString(PyExc_RuntimeError, "next_grid and data should have same type.");
        return(NULL);
    }

    if(PyArray_NDIM(data) != 2)
    {
        PyErr_SetString(PyExc_RuntimeError, "data should be two dimensional.");
        return(NULL);
    }

    if(PyArray_NDIM(next_grid) != 2)
    {
        PyErr_SetString(PyExc_RuntimeError, "next_grid should be two dimensional.");
        return(NULL);
    }

    if((PyArray_DIM(data, 0) != PyArray_DIM(next_grid, 0) || (PyArray_DIM(data, 1) != PyArray_DIM(next_grid, 1))))
    {
        PyErr_SetString(PyExc_RuntimeError, "data and next_grid must have the same dimensions.");
        return (NULL);
    }

    // evolve
    evolve(PyArray_DATA(data), PyArray_DATA(next_grid), D, dt);

    Py_XINCREF(next_grid);
    return(next_grid);
}

/* Initialize the module */
PyMODINIT_FUNC
PyInit_cdiffusion(void)
{
    PyObject *m;

    m = PyModule_Create(&cdiffusionmodule);
    if(m == NULL)
    {
        return(NULL);
    }

    /* Load 'numpy' functionality. */
    import_array();

    return(m);
}