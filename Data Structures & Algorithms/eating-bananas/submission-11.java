class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int lowestRate = 1;
        int maxRate = piles[0];
        for (int p : piles) {
            maxRate = Math.max(maxRate, p);
        }

        int res = maxRate;
        while (lowestRate <= maxRate) {
            int rate = lowestRate + ((maxRate - lowestRate) / 2);
            // try this rate for eating bananas
            int time = 0;
            for (int p : piles) {
                time += (int) Math.ceil((double) p / rate);
                if (time > h) {
                    break;
                }
            }
            if (time > h) {
                // rate was too slow need to pick bigger rate
                lowestRate = rate + 1;
            } else {
                // rate is a potential solution try to find smaller one
                res = rate;
                maxRate = rate - 1;
            }
        }
        return res;
    }
}
