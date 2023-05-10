#ifndef LISTS_H
#define LISTS_H
/**
 * struct listint_t - sorted singly linked list
 * @value: integer
 * @next: pointes to next node 
 * Description: singly linked list node structure
 *
 */

typedef struct listint_t
{
	int value;
	struct listint_s* next;
} listint_s;

size_t displayList(listint_t *h);
void free_Listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS-H */
