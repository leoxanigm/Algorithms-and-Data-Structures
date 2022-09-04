# Queues

A sequential data collection where we only have access to the head and tail elements.
First in first out (FIFO).

| Operation   | Pseudocode   |
|-------------|--------------|
| head        | HEAD[Q]      |
| dequeue!    | DEQUEUE[Q]   |
| enqueue!    | ENQUEUE[p, Q]|
| empty?      | EMPTY[Q]     |

Construct new empty queue

`new Queue Q`