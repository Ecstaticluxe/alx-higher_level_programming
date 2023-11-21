#include <Python.h>
#include <stdout.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes ? bytes : "(error)");

    printf("  first %ld bytes:", size > 10 ? 10 : size);
    for (i = 0; i < size && i < 10; ++i) {
        printf(" %02hhx", bytes[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    printf("[.] float object info\n");
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
