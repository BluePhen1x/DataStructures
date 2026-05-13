class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        
        // Step 1: Calculate Prefix products
        // result[i] will store the product of all elements to the left of i
        result[0] = 1; // Nothing to the left of the first element
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        
        // Step 2: Calculate Suffix products on the fly
        // We use a single variable 'suffix' to keep track of products from the right
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            // Multiply the current prefix (already in result) by the suffix
            result[i] = result[i] * suffix;
            // Update the suffix for the next element to the left
            suffix = suffix * nums[i];
        }
        
        return result;
    }
}