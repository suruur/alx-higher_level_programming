#include <stdio.h>
#include "lists.h"

/**
 * print_listint - check if there is a cycle or not
 * @h: list to be checked
 * Return: int
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *cur;
	unsigned int n;

	cur = h;
	n = 0;

	while (cur != NULL)
	{
		printf("%i\n", cur->n);
		cur = cur->next;
		n++;
	}

	return (n);

}
/**
 * add_nodeint - adds
 * @head: pointer
 * @n: int
 * Return: address
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;

	return (new);
}

/**
 * free_listint - frees
 * @head: pointer
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *cur;

	while (head != NULL)
	{
		cur = head;
		head = head->next;
		free(cur);
	}
}
