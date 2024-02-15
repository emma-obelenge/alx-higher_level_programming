#ifndef HASH_H
#define HASH_H

#include <stdio.h>
#include <unistd.h>

#define CAPACITY 50000 /* Size of the HashTable.*/

typedef struct hash_item
{
    char *key;
    char *value;
}hash_item;

// Defines the HashTable.
typedef struct hash_table
{
    // Contains an array of pointers to items.
    hash_item **items;
    int size;
    int count;
} hash_table;

#endif