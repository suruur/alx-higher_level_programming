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
/**
 * add_nodeint_end - adds
 * @head: po
 * @n: int
 * Return: address
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *cu;

	cu = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (cu->next != NULL)
			cu = cu->next;
		cu->next = new;
	}

	return (new);
}
/**
 * insert_node - insert
 * @head: pointer
 * @number: ni
 * Return: address
 
listint_t *insert_node(listint_t head, int number)
{
	listint_t *cu;
	listint_t *nn = malloc(sizeof(listint_t));

	if (nn == NULL)
	{
		return (NULL);
	}

	nn->n = number;
	nn->next = NULL;

	if (*head == NULL || number < (*head->n))
	{
		nn->next = *head;
		*head = nn;
		return (nn);
	}
	cu = *head;

	while (cu->next != NULL && cu->next->n < number)
	{
		cu = cu->next;
	}
	nn->next = cu->next;
	cu->next = nn;

	return (nn);

}
*/
