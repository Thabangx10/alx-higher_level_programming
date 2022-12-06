#include "lists.h"

/**
 * is_palidrome - checks if a  linked list is palidrome
 * @head: double pointer to the linked list
 *
 * Return: 1(if TRUE),0(if FALSE)
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++
	}
	return (0);
}
