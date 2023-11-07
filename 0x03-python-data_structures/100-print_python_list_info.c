#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#!/usr/bin/python3

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: PyObject pointer to the Python list
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(int argc, char *argv[])
{
    Py_Initialize();
    if (argc == 2)
    {
        PyObject *pName, *pModule, *pDict, *pFunc, *pArgs, *pValue;
        if (PyList_Check(pValue))
        {
            pValue = Py_BuildValue("i", atoi(argv[1]));
            print_python_list_info(pValue);
        }
        else
            fprintf(stderr, "First argument is not a list\n");
    }
    else
        fprintf(stderr, "Usage: %s number\n", argv[0]);

    Py_Finalize();
    return (0);
}
