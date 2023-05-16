#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node: inserts number into sorted singly linked list
 * @head: pointer to head 
 * @number: number to be inserted
 *
 * Return: NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	int n;

	listint_t *new_node = (listint_t*)malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;
	listint_t *current;

	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next-n < new_node->n)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;

		if (new_node == NULL)
		{
			return (NULL);
		}
	}
		return (new_node);
}


