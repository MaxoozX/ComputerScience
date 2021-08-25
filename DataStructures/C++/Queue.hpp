/**
 * The declaration and implementation of the Queue class
 * @file Queue.hpp
 * @author Maxence
 * @version 1.0
*/

#ifndef QUEUE_H
#define QUEUE_H

#include "DoubleLinkedNode.hpp"

/** A classic Stack class, you can push, pull and know is the stack is empty */
template <class QueueType>
class Queue {

    public:
        Queue(): firstElement(0), lastElement(0) {}

        bool isEmpty() {
            return (firstElement == 0);
        }

        void push(QueueType value) {
            DoubleLinkedNode<QueueType>* newNode = new DoubleLinkedNode<QueueType>(value, lastElement, 0);
            if(lastElement != 0) {
                lastElement->previous = newNode;
            }
            lastElement = newNode;
            if(firstElement == 0) {
                firstElement = newNode;
            }
        }
        
        QueueType pull() {
            if(isEmpty()) {
                return QueueType();
            }
            QueueType value = firstElement->value;
            DoubleLinkedNode<QueueType>* previous = firstElement->previous;
            delete firstElement;
            firstElement = previous;
            return value;
        }

    private:
        DoubleLinkedNode<QueueType>* firstElement;
        DoubleLinkedNode<QueueType>* lastElement;

};

#endif // QUEUE_H
