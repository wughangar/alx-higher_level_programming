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
	int n;
	struct Node* next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);
#endif /* LISTS-H */
