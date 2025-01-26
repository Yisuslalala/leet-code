const containsDuplicate = (nums) => {
  const seens = {};

  for (let i = 0; i < nums.length; i++) {
    console.log(i, seens, nums[i]);
    if (seens.hasOwnProperty(nums[i])) {
      return true;
    } else {
      seens[nums[i]] = i;
    }
  }
  return false;
};

const nums = [1, 2, 3, 3];
console.log(containsDuplicate(nums));
