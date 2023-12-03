#include <Python.h>
/**
 * print_python_list_info - print
 * @p: pointer
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;

	printf("[*] Size of Python List = %ld\n", PyList_Size(p));

	list = (*PyListObject *)p;
	size = list->allocated;

	printf("[*] Allocated = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		if (i < PyList_Size(p))
		{
			printf("Element %ld: %s\n", i, PyTYPE(list->ob_item[i]->tp_name));
		}
	}
}
