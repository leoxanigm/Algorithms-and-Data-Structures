#include "HashTable.hpp"

// #include <iostream>

HashTable::HashTable(long _a, long _c, long _m)
{
  this->a = _a;
  this->c = _c;
  this->m = _m;

  buckets = new int[_m];

  for (int i = 0; i < this->m; ++i)
  {
    buckets[i] = -1;
  }
}

HashTable::~HashTable()
{
  this->buckets = nullptr;
}

int HashTable::getLength()
{
  return this->m;
}

int HashTable::hashFunction(int key, long m)
{
  return ((this->a * key) + this->c) % m;
}

void HashTable::insert(int key)
{
  if (key < 0)
    return;

  double loadFactor = this->loadFactor();

  if (loadFactor >= 1)
    this->extend();

  int hashValue = this->hashFunction(key, this->m);

  while (this->buckets[hashValue] != -1)
  {
    if (hashValue + 1 >= this->m)
    {
      hashValue = -1;
    }
    ++hashValue;
  }

  this->buckets[hashValue] = key;
}

void HashTable::extend()
{
  long newM = this->m * 2;
  int *newBuckets = new int[newM];
  int *oldBuckets = this->buckets;

  for (int i = 0; i < newM; ++i)
  {
    newBuckets[i] = -1;
  }

  this->buckets = newBuckets;

  for (int i = 0; i < this->m; ++i)
  {
    this->insert(oldBuckets[i]);
  }

  this->m = newM;
}

bool HashTable::find(int key)
{

  if (key < 0)
    return false;

  int hashValue = this->hashFunction(key, this->m);
  int count = this->m;

  while (this->buckets[hashValue] != key && count > 0)
  {
    if (hashValue + 1 >= this->m)
    {
      hashValue = -1;
    }
    ++hashValue;

    --count;
  }

  if (this->buckets[hashValue] == key)
  {
    return true;
  }

  return false;
}

void HashTable::remove(int key)
{
  if (key < 0)
    return;

  int hashValue = this->hashFunction(key, this->m);
  int count = this->m;

  while (this->buckets[hashValue] != key && count > 0)
  {
    if (hashValue + 1 >= this->m)
    {
      hashValue = -1;
    }
    ++hashValue;

    --count;
  }

  if (this->buckets[hashValue] == key)
  {
    this->buckets[hashValue] = -1;
  }
}

double HashTable::loadFactor()
{
  double filledBuckets = 0;
  // Count the number of values in the bucket
  for (int i = 0; i < this->m; ++i)
  {
    if (this->buckets[i] != -1)
    {
      filledBuckets += 1;
    }
  }

  return filledBuckets / this->m;
}
