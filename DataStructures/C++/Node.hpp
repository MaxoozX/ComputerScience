/**
 * The declaration and implementation of the Node class
 * @file Node.hpp
 * @author Maxence
 * @version 1.0
*/

#ifndef NODE_H
#define NODE_H

/** Building block of more advanced data structures such as Linked Lists and Stacks and */
template <class Type>
class Node {

    public:
        Node(Type _value, Node* _next): value(_value), next(_next) {}
        Type value;
        Node* next;

};

#endif // NODE_H
