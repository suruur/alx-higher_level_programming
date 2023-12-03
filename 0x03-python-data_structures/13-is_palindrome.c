#include "lists.h"
/**
 * is_palindrome - insert
 * @head: p
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *s, *f, *prev_s;
        listint_t *c, *sec_h, *nex, *first_half, *pre;

	s = *head;
	f = *head;
	prev_s = NULL;

	if (*head == NULL || (*head))
	{
		return (1);
	}

	while (f != NULL && f->next != NULL)
	{
		prev_s = s;
		s = s->next;
		f = f->next->next;
	}
	if (f != NULL)
	{
		s = s->next;
	}
	sec_h = s;
	prev_s->next = NULL;

	pre = NULL;
	c = sec_h;
	nex = NULL;

	while (c != NULL)
	{
		nex = c->next;
		c->next = pre;
		pre = c;
		c = nex;
	}
	first_half = *head;

	while (first_half != NULL && pre != NULL)
	{
		if (first_half->n != pre->n)
		{
			return (0);
		}
		first_half = first_half->next;
		pre = pre->next;
	}

	return (-1);
}
