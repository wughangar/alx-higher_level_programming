#include "lists.h"

int check_cycle(listint_t *list)
{
	// Start with the first number
	int num = list->n;
	list = list->next;

	while(list != NULL)
	{
		if(list->n < num)
		{
			return 1;
		}

		num = list->n;
		list = list->next;
	}
	
	return 0;
}

