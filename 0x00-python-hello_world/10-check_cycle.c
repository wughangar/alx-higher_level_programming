#include "lists.h"
#include <stdio.h>

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
