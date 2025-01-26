const twoSum = function (nums, target) {
  let seens = [];
  for (let i = 0; i < nums.length; i++) {
    console.log(`iteration? ${i}`);
    let difference = target - nums[i];
    console.log(`diff ${difference}`, difference);
    if (seens[difference]) {
      return [seens[difference], i];
    } else {
      seens.push(i);
    }
  }
  return [];
};

const numbers = [2, 7, 11, 15];
const target = 9;

const numbers2 = [8, 4, 1, 19];
const target2 = 10;
console.log(twoSum(numbers, target));
console.log(twoSum(numbers2, target2));
