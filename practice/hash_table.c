HashTable* create_table(int size)
{
    // Creates a new HashTable.
    hash_table* table = malloc(sizeof(hash_table));
    table->size = size;
    table->count = 0;
    table->items = calloc(table->size, sizeof(hash_item*));

    for (int i = 0; i < table->size; i++)
        table->items[i] = NULL;

    return table;
}