class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        hashmap = {}

        # loop through the elements of the list
        for index in range(len(nums)):
            # save the compliment of the target with the current element
            compliment = target - nums[index]

            # if the compliment is in the hashmap return its index, otherwise add it to the map
            if compliment in hashmap:
                return [hashmap[compliment], index]
            else:
                hashmap[nums[index]] = index
        
        # found no solution
        return []