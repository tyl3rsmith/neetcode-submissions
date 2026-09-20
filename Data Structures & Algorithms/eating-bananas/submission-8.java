class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int maxRate = piles[0], lowestRate = 1;
        for (int i = 0; i < piles.length; i++) {
            maxRate = Math.max(maxRate, piles[i]);
        }

        int res = maxRate;
        while (lowestRate <= maxRate) {
            int rate = lowestRate + ((maxRate - lowestRate) / 2);
            
            int time = 0;    
            for (int i = 0; i < piles.length; i++) {
                time += (int) Math.ceil((double) piles[i] / rate);
                if (time > h) {
                    break;
                }
            }

            if (time <= h) {
                res = rate;
                maxRate = rate - 1; // try to find smaller rate
            } else {
                lowestRate = rate + 1;
            }
        }
        return res;
    }
}
