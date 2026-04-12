# Doubly Linked List Implementation

## Problem Description

This document outlines the implementation of a doubly linked list, including basic node creation, and operations such as inserting a node into a sorted list and reversing the list.

## C++ Solution

This C++ solution provides a basic structure for a doubly linked list node and examples of operations.

**`Node` Structure:**

```cpp
struct Node
{
    int data;
    Node *next;
    Node *prev;
};
```

**`main()` function (Basic Example):**

*   Demonstrates creating three nodes and linking them to form a simple doubly linked list: `head_address <-> second_address <-> third_address`.

**`sortedInsert(Node *head_address, int data)` function:**

*   Inserts a new node with `data` into a sorted doubly linked list while maintaining its sorted order.
*   Handles various cases: insertion at the beginning, in the middle, and at the end of the list.
*   If the list is empty, the new node becomes the head.

**`Reverse(Node* head)` function:**

*   Reverses a given doubly linked list.
*   It iterates through the list, swapping the `prev` and `next` pointers for each node.
*   The `head` of the list is updated to the new first node (original last node).

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
#define ld long double 
#define vll vector<long long>
#define vi vector<int>
#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define sort(a) sort(a.begin(),a.end());
#define rsort(a) sort(a.rbegin(),a.rend());
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}

struct Node
{
    int data;
    Node *next;
    Node *prev;
};

int main()
{
    Node *head_address=NULL, *second_address=NULL, *third_address=NULL;
    
    head_address=new Node();
    second_address=new Node();
    third_address=new Node();
    
    head_address->data=5;
    head_address->prev=NULL;
    head_address->next=second_address;
    
    second_address->data=13;
    second_address->prev=head_address;
    second_address->next=third_address;
    
    third_address->data=-11;
    third_address->prev=second_address;
    third_address->next=NULL;
    
    return 0;
}

//Insert node at correct position in a sorted Doubly Linked List

Node* sortedInsert(Node *head_address, int data) 
{
    Node *address=NULL,*next_address=NULL,*prev_address=NULL;
    address=head_address;
    while(address!=NULL)
    {
        if((address->next)!=NULL && data>=(address->data) && data<=((address->next)->data))
        {
            Node *generate_address=NULL;
            generate_address=new Node();
            generate_address->data = data;
            
            next_address=address->next;
            
            address->next=generate_address;
            generate_address->next=next_address;
            
            next_address->prev=generate_address;
            generate_address->prev=address;
            
            break;
        }
        else if((address->prev)!=NULL && data<(address->data))
        {
            Node *generate_address=NULL;
            generate_address=new Node();
            generate_address->data = data;
            
            prev_address=address->prev;
            
            address->prev=generate_address;
            
            generate_address->next=address;
            generate_address->prev=prev_address;
            
            prev_address->next=generate_address;
        
            break;
        }
        else if((address->prev)==NULL && data<(address->data))
        {
            Node *generate_address=NULL;
            generate_address=new Node();
            generate_address->data = data;
            
            prev_address=address->prev;
            
            address->prev=generate_address;
            
            generate_address->next=address;
            generate_address->prev=prev_address;
            
            head_address=generate_address;
        
            break;
        }
        else if((address->next)==NULL && data>=(address->data))
        {
            Node *generate_address=NULL;
            generate_address=new Node();
            generate_address->data = data;
            
            next_address=address->next;
            
            address->next=generate_address;
            generate_address->next=next_address;
            
            generate_address->prev=address;
            
            break;
        }
    }
    
    if(head_address==NULL)
    {
        Node *generate_address=NULL;
        generate_address=new Node();
        generate_address->data = data;
        
        head_address=generate_address;
        head_address->prev=NULL;
        head_address->next=NULL;
    }
    
    return head_address;
}


//Reverse the linked List
Node* Reverse(Node* head)
{
     Node *temp = NULL;  
     Node *current = head;


     while (current !=  NULL)
     {
       temp = current->prev;
       current->prev = current->next;
       current->next = temp;              
       current = current->prev;
     }      
    if(temp != NULL )
        head = temp->prev;

    return head;

}
```