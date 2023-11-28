#include "lists.h"
/**
 * insert_node - insert
 * @head: p
 * @number: int
 * Return: add
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c;
	listint_t *new_n = malloc(sizeof(listint_t));

	if (new_n == NULL)
		return (NULL);

	new_n->n = number;
	new_n->next = NULL;

	if (*head == NULL || number < (*head)->next->n)
	{
		new_n->next = *head;
		*head = new_n;
		return (new_n);
	}

	c = *head;
	while (c->next != NULL && c->next->n < number)
		c = c->next;
	new_n->next = c->next;
	c->next = new_n;

	return (new_n);
}
