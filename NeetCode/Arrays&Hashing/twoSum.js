const twoSum = (nums, target) => {
  const seens = {};
  for (let i = 0; i < nums.length; i++) {
    const difference = target - nums[i];
    if (seens.hasOwnProperty(difference)) {
      return [seens[difference], i];
    }

    seens[nums[i]] = i;
  }

  return [];
};

const nums = [3, 4, 5, 7];
const target = 7;

console.log(twoSum(nums, target));
