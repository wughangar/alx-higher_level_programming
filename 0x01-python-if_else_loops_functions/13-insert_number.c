#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * displyList - lists the list of nodes in list
 * @h: pointer ot header of the list
 * Return: number of nodes
 */
size_t displayList(listint_t *h)
{
	listint_t *current = h;
	size_t count = 0;

	while (current != NULL)
	{
		printf("%d", current->count);
		current = currect->next;
		count++;
	}
	return (count);
}

/**
 * free_Listint - frees the list
 * @head: pointer to head node
 *
 * Return: void
 */

void free_Listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * insert_node - inserts node in list
 * @number; value to be inserted
 *
 * Return: the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t new = (listint_t*)malloc(sizeof(listint_t));
	new->value = number;
	new->next = NULL;
	listint_t *current;

	if (*head == NULL || number < (*head)->value)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		current = *head;
		while(current->next != NULL && current->next->value < number)
		{
			current = current->next;
		}

		new-> = current->next;
		current->next = new;
	}
}
