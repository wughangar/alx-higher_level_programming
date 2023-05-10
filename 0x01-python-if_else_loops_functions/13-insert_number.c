#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * Cnode: creates a node 
 * @number: integer
 *
 * Return: list 
 */
listint_s Cnode(int number)
{
	listint_s* newNode = (listint_s*)malloc(sizeof(listint_t));
	if (newNode == NULL)
	{
		printf("Memory alloaction failed.\n");
		return (listint_s);
	}
	newNode->date = number;
	newNode->next = NULL;
	return (newNode);
}

/**
 * insert_node: inserts node
 * @head: pointer to head
 * @number: int
 *
 * Return: tthe list
 */

listint_t* insert_node(listint_t** head, int number)
{
	listint_t* newNode = createNode(number);

	if (newNode == NULL)
	{
		return (Null);
	}

	if (*head == NULL || number < (*head)->data)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		listint_t* current = *head;
		while (current->next != NULL && number > current->next->data)
		{
			current = current->next;
		}
		newNode->next = current->next;
		current->next = newNode;
	}
	return (newNode);
}

/**
 * printList - prints the list
 * @head: pointer to head
 *
 * Return: void
 */
void printlist(listint_t* head)
{
	listint_t* current = head;

	while (current != NULL)
	{
		printf("%d ", current->data);
		current = current-.next;
	}
	printf("\n");
}

