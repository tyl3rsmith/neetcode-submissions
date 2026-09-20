class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int num_zeros = 0;
        int product = 1;

        for (int num : nums) {
            if (num == 0) {
                num_zeros++;
            } else {
                product *= num;
            }
        }

        if (num_zeros > 1) {
            return res;
        } else if (num_zeros == 1) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == 0) {
                    res[i] = product;
                    break;
                }
            }
        } else /* num_zeros == 0 */ {
            for (int i = 0; i < res.length; i++) {
                res[i] = product / nums[i];
            }
        }

        return res;
        
    }
}  
