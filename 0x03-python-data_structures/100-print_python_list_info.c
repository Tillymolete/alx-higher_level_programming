#define PY_SSIZE_T_CLEAN
#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p) {
Py_ssize_t size, alloc;
Py_ssize_t i;
PyObject *item;

if (!PyList_Check(p)) {
fprintf(stderr, "Invalid object passed!\n");
return;
}

size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", alloc);

for (i = 0; i < size; i++) {
item = PyList_GetItem(p, i);
printf("element %zd: %s\n", i Py_TYPE(iytem)->tp_name);
}
}
