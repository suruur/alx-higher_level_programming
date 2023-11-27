#include "lists.h"
/**
 * check_cycle - check if there is a cycle or not
 * @list: list to be checked
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (list == NULL)
		return (0);

	while (f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
			return (1);
	}

	return (0);

}
