#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    listint_t *fast = *head;
    listint_t *slow = *head;


    if (*head == NULL || (*head)->next == NULL)
    {
        return 1;
    }

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        slow = slow->next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    listint_t *current = slow;
    listint_t *next = NULL;
    listint_t *new_head = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = new_head;
        new_head = current;
        current = next;
    }

    listint_t *left = *head;
    listint_t *right = new_head;

    while (left != NULL && right != NULL)
    {
        if (left->n != right->n)
        {
            return 0;
        }
        left = left->next;
        right = right->next;
    }

    return 1;
}
