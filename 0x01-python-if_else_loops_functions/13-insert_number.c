#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert node - inserts a number into a sorted singly linked list
 * @head: the pointer of linked list
 * @number: number to be inserted
 * return: pointer otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
