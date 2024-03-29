// Given an integer array nums of length n, you want to create an array
// ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
// for 0 <= i < n (0-indexed).

// Specifically, ans is the concatenation of two nums arrays.

// Return the array ans.

const sampleList = [1, 2, 1];

const ConcatenationOfArrays = (nums) => {
  let ans = [];
  for (let i = 0; i < nums.length; ++i) {
    ans.splice(i, 0, nums[i]);
    ans.splice(i + nums.length, 0, nums[i]);
  }
  return ans;
};

console.log(ConcatenationOfArrays(sampleList));
