#ifndef LISTS_H
#define LISTS_H
/**
 * struct listint_t - sorted singly linked list
 * @value: integer
 * @next: pointes to next node 
 * Description: singly linked list node structure
 *
 */

typedef struct Node
{
	int data;
	struct Node* next;
} listint_s;

listint_t Cnode(int number);
void printList(listint_t* head);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS-H */
