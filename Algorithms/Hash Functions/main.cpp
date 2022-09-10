#include <iostream>
#include <iterator>

#include "HashTable.cpp"

int main()
{
  HashTable myHash(2, 1, 5);

  myHash.insert(3);
  myHash.insert(3);
  myHash.insert(3);
  myHash.insert(3);
  myHash.insert(3);
  myHash.insert(12);
  myHash.insert(2);

  // myHash.remove(3);

  for (int i = 0; i < myHash.getLength(); ++i)
  {
    std::cout << std::to_string(myHash.buckets[i]) + " ";
  }

  std::cout << std::endl;

  std::cout << std::to_string(myHash.loadFactor()) + " " << std::endl;

  return 0;
}