class Solution {
    public int subarraySum(int[] nums, int k) {
        Set <Integer> s = new HashSet<Integer>();
        int sum = 0;
        int[] prefix_sum = new int[nums.length];
        int count = 0;
        // Set<Integer> prefixSumSet = new HashSet<Integer>();
        HashMap<Integer, Integer> prefixSumMap= new HashMap<Integer, Integer>();
        // prefixSumSet.add(0);
        prefixSumMap.put(0,1);
        // int i = 0;
        for(int num:nums){
            sum = sum+num;
            // prefixSumSet.add(sum);
            if (prefixSumMap.containsKey(sum-k)){
                count = count + prefixSumMap.get(sum-k);
            }
            if(prefixSumMap.containsKey(sum)){
                int val = prefixSumMap.get(sum);
                prefixSumMap.put(sum, ++val);
            }
            else{
                prefixSumMap.put(sum, 1);
            }
            
        }
        
        return count;
    }
}