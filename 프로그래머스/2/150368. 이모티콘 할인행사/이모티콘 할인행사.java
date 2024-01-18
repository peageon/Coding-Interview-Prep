import java.util.*;
class Solution {
    public static final List<Double> myList = List.of(0.6, 0.7, 0.8, 0.9);
    private int plus = 0;
    private int sale = 0;
    private int[][] users;
    private int[] emoticons;

    public int[] solution(int[][] users, int[] emoticons) {
        this.users = users;
        this.emoticons = emoticons;
        List<Double> sales = new ArrayList<>();
        for (int i = 0; i < emoticons.length; i++) {
            sales.add(1.0);
        }
        this.recurse(0, emoticons.length, sales);
        int[] sol = {plus, sale};
        return sol;
    }
    
    public void recurse(int index, int lastIndex, List<Double> sales) {
        for (int i=0; i < 4; i++) {
            sales.set(index, myList.get(i));
            if(index < lastIndex - 1) {
                recurse(index+1, lastIndex, sales);
            } else {
                this.compare(sales);
            }
        }
        return;
    }
    
    public void compare(List<Double> sales) {
        int plus = 0;
        int totalSale = 0;
        int maxIndex = sales.size();
        
        for(int[] user: this.users) {
            double bargain = (100 - user[0]) * 0.01;
            int maxPrice = user[1];
            int curPrice = 0;
            for(int i=0; i < maxIndex; i++) {
                double sale = sales.get(i);
                if(sale <= bargain) {
                    curPrice += (this.emoticons[i] * sale);
                }
            }
            if (curPrice >= maxPrice) {
                plus++;
            } else {
                totalSale += curPrice;
            }
        }
        
        if(this.plus < plus) {
            this.plus = plus;
            this.sale = totalSale;
        }
        else if(this.plus == plus) {
            if(totalSale > this.sale) {
                this.sale = totalSale;
            }
        }
    }
}