#ifndef PYTHON_H
#define PYTHON_H

#include <Python.h>

typedef struct
{
	PyObject_HEAD
} PyListObject;

typedef struct
{
	PyObject_HEAD
} PyBytesObject;

typedef struct
{
	PyObject_HEAD
} PyObject;

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
PyObject *PyList_New(Py_ssize_t size);
int PyList_Append(PyObject *list, PyObject *item);
PyObject *PyBytes_FromStringAndSize(const char *str, Py_ssize_t size);
char *PyBytes_AsString(PyObject *bytes);
Py_ssize_t PyBytes_Size(PyObject *bytes);

#endif /* PYTHON_H */
