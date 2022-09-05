const arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7];

const len = arr.length;
let start = 0;
let end = len - 1;
let totalSum = 0;

for (let i = 0; i < len; ++i) {
  let sum = 0;
  for (let j = i; j < len; ++j) {
    sum += arr[j];
    if (sum > totalSum) {
      totalSum = sum;
      start = i;
      end = j;
    }
  }
}

// Should output 7, 10, 43
console.log(start, end, totalSum)
