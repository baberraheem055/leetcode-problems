#include <iostream>
#include <list>
#include <vector>
using namespace std;
class Hashtable
{
private:
    vector<list<int>> table;
    int size;

    int Hash_function(int key)
    {
        return key % size;
    }

public:
    // constructor
    Hashtable(int table_size)
    {
        size = table_size;
        table.resize(size); // Resize the table vector to accommodate the specified number of buckets
    }

    // we can declare the constructor through Member initilizer list
    //  HashTable(int tableSize) : size(tableSize) {
    //      table.resize(size);
    //  }

    // NOW LETS DEFINTE FUNCTION FOR "INSERT","SEARCH" AND "DELETE"

    // INSERT

    void INSERT(int key)
    {
        int index;
        index = Hash_function(key);
        table[index].push_back(key);
    }

    bool SEARCH(int key)
    {
        int index = Hash_function(key);
        for (int value : table[index])
        {
            if (value == key)
            {
                return true;
            }
        }
        return false;
    }
    // remove an element from hashtable

    void remove(int key)
    {
        int index = Hash_function(key);
        auto &list = table[index];
        for (auto it = list.begin(); it != list.end(); ++it)
        {
            if (*it == key)
            {
                list.erase(it);
                return;
            }
        }
    }
};
int main()
{
    int arr[] = {4, 5, 3, 7, 8, 5, 2};
    int size = sizeof(arr) / sizeof(arr[0]);
    int element;
    char ch;

    // object of class
    Hashtable ht(10); // where 10 is the size of the table

    // to insert map element into hashtable

    for (int i = 0; i < size; i++)
    {
        ht.INSERT(arr[i]);
    }
    while (true)
    {
        cout << "enter a number to find " << endl;
        cin >> element;
        cout << element << " is " << (ht.SEARCH(element) ? "found" : "not found") << endl;
        cout << "do you want to find anther number(y/n)" << endl;
        cin >> ch;
        if (ch == 'n')
        {
            break;
        }
        
    }
}