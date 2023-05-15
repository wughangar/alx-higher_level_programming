#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * print_listint: function to print the list
 * @head: pointer to head
 *
 * Return: number of nodes
 */

size_t print_listint(const listint_t *head)
{
	int n;

	while(head != NULL)
	{
		fprintf(stderr, "%d\n", head->n);
		head = head->next;
		n++;
	}
	return (n);
}

/**
 * add_nodeint: adds new node at the beginning of the list
 * @head; pointer to head node 
 * @n; const in to be added
 *
 * Return: updatd listint_t
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t* new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * free_listint_t; frees the list
 * @head: pointer to head node
 *
 * Return: none
 */

void free_listint_t(listint_t *head)
{
	listint_t *current;

	while(head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * check_cycle - checks for cycles in linked lists
 * @list: pointer to the linked list
 *
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	while (fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;

		if (slw == fst)
		{
			return (1);
		}
	}

	return (0);
}
