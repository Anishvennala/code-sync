class Solution {
    public int maxProfit(int[] prices) {
        
        int min = 10000;
        int maxProf = 0;

        for(int i = 0; i < prices.length; i++){

            //if min value
            if(prices[i] < min) min = prices[i];

            //if max value
            int currProf = prices[i] - min;
            if(currProf > maxProf) maxProf = currProf;
            
        }
        return maxProf;
    }
}