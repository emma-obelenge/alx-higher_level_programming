#include "hash.h"

hash_item new_item(char *key, int value)
{
    /* Creates a pointer to a new hash table item*/
    hash_item item = (hash_item*) malloc(sizeof(hash_item));
    item->key = malloc(strlen(key) + 1);
    item->value = malloc(strlen(key) + 1);
    strcpy(item->key, key);
    strcpy(item->value, value);
    return (item);
}