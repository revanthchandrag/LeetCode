class Solution {
    public int maxChunksToSorted(int[] arr) {
        int maxSoFar = arr[0];
        int n = arr.length;
        int count = 0;
        for (int i =0;i<n;i++){
            maxSoFar = Math.max(maxSoFar, arr[i]);
            if (maxSoFar == i){
                count++;
            }
            
        }
        
        return count;
        
    }
}