/**
 * The declaration and implementation of the DoubleLinkedNode class
 * @file DoubleLinkedNode.hpp
 * @author Maxence
 * @version 1.0
*/

#ifndef DOUBLELINKEDNODE_H
#define DOUBLELINKEDNODE_H

/** Building block of more advanced data structures such as double linked lists and queues */
template <class Type>
class DoubleLinkedNode {

    public:
        DoubleLinkedNode(Type _value, DoubleLinkedNode* _next, DoubleLinkedNode* _previous): value(_value), next(_next), previous(_previous) {}
        Type value;
        DoubleLinkedNode* next;
        DoubleLinkedNode* previous;

};

#endif // DOUBLELINKEDNODE_H
