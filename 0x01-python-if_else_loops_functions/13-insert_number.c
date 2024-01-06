#include "main.h"
/**
 * insert_node - Function to insert new node to linked list
 * @head: pointer to the linked list
 * @number: the value to be added into the predefined linked list
 * Return: Returns the address of the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *ptr = *head
    listint_t *temp = NULL;
    int i;

    if (ptr == NULL)
        return (NULL);
    temp = malloc(sizeof(listint_t));
    if (temp == NULL)
        return (NULL);
    for (i = 1; i < 5; i++)
    {
        ptr = ptr->next;
    }
    temp->next = ptr->next;
    temp->n = number;
    ptr->next = temp;
    return (&temp);
}