// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

const nums = [1, 2, 3, 1];
const nums2 = [1, 2, 3, 4];

duplicated = {};
const ContainDuplicates = (nums)  => {
    const seen = {};
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in seen){
            return true;    
        }
        else {
            seen[nums[i]] = i;
        }
    }
    return false;
};
    

console.log(ContainDuplicates(nums));
console.log(ContainDuplicates(nums2));


// console.log(nums[1] in duplicated);


