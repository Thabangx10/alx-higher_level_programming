#!/bin/bash
#include "list.h"

/**
 * check_list - will check if the function rund=s a cycle
 *
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesnt
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = *list
	listint_t *fast = *list

	if(!list)
		return(0);

	while (slow && fast && fast ->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if(slow == fast)
			return (1);
	}

	return (0);
}