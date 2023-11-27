#ifndef LIST_H
#define LIST_H
#include<stdlib>

/**
 * struct listint_s - singly list
 * @n: integer
 * @next: points to the next node
 *
 * description: singly linked list
 *
 */
typedef struct listint_s
{
	int n;
	listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
