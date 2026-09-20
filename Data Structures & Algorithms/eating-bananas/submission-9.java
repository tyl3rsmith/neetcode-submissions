class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int lowestRate = 1, maxRate = piles[0];
        for (int p : piles) {
            maxRate = Math.max(maxRate, p);
        }

        int res = maxRate;
        while (lowestRate <= maxRate) {
            int rate = lowestRate + ((maxRate - lowestRate) / 2);
            int time = 0;
            for (int p : piles) {
                time += (int) Math.ceil((double) p / rate);
            }

            if (time <= h) {
                res = rate; // this is a valid result try to find a smaller one
                maxRate = rate - 1;
            } else { // this is too slow
                lowestRate = rate + 1;
            }
        }

        return res;
    }
}
