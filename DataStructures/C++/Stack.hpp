/**
 * The declaration and implementation of the Stack class
 * @file Stack.hpp
 * @author Maxence
 * @version 1.0
*/

#ifndef STACK_H
#define STACK_H

#include "Node.hpp"

/** A classic Stack class, you can push, pull and know is the stack is empty */
template <class StackType>
class Stack {

    public:
        Stack(): firstElement(0) {}

        bool isEmpty() {
            return (firstElement == 0);
        }

        void push(StackType value) {
            Node<StackType>* newNode = new Node<StackType>(value, firstElement);
            firstElement = newNode;
        }
        
        StackType pull() {
            if(isEmpty()) {
                return StackType();
            }
            StackType value = firstElement->value;
            Node<StackType>* next = firstElement->next;
            delete firstElement;
            firstElement = next;
            return value;
        }

    private:
        Node<StackType>* firstElement;

};

#endif // STACK_H
