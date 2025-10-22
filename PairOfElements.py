class elements:
    def two_sums(self,nums,target):
        lookup = {
        }
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target-num], i)
            lookup[num] = i

val = int(input("Input number:"))
print("index%d, index2%d", elements().two_sums((10,20,30,40,50,60,70), val))