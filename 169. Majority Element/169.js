/**
 
@param {number[]} nums
@return {number}*/
var majorityElement = function(nums) {
    const hash = {};
    const length = nums.length / 2
    for (let i = 0; i < nums.length; i++) {
        if (hash[nums[i]] === undefined) {
            hash[nums[i]] = 1;
        } else {
            hash[nums[i]]++;
        }

        if (hash[nums[i]] > length) {
            return nums[i]
        } 
    }
};