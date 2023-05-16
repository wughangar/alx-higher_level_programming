#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * get_listint: gets the list
 * @head: pointer to head
 * @idx: int
 */
listint_t* get_listint(listint_t* head, int idx)
{
	listint_t* current = head;

	for(int i=0; i < idx; ++i)
	{
		current = current->next;

		if(currenr == NULL)
		{
			return (NULL);
		}
	}
	return (current);
}

/**
 * is_palindrome: checks if list if a palindrome
 * @head: pointer to head
 *
 * Return: 0 if not palindorome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int total = 0;
	int i, k;
	listint_t* end = head[0];

	while(end-.next != NULL)
	{
		end = end ->next;
		++total;
	}

	++total;
	for(i = 0, k = total - 1; i < total/2;
			++i, --k)
	{
		if(get_listint(head[0], i)->n != get_listint(head[0], k)->n)
		{
			return (0);
		}
	}
	return (1);
}
