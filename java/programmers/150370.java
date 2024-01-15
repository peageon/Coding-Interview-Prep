import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.*;
//Date를 안써도 되는데 배우고 싶어서 써보기로 했다!

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        HashMap<String, Integer> termsMap = new HashMap<>();
        for (String term: terms) {
            String[] parts = term.split(" ");
            termsMap.put(parts[0], Integer.parseInt(parts[1]));
        }
        
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy.MM.dd");
        LocalDate twoday = LocalDate.parse(today, formatter);
        List<Integer> result = new ArrayList<>();
        for (int i=0; i < privacies.length; i++) {
            String[] parts = privacies[i].split(" ");
            String date = parts[0];
            String term = parts[1];
             
            LocalDate customerDate = LocalDate.parse(date, formatter).plusMonths(termsMap.get(term));
            if (!customerDate.isAfter(twoday)) {
                result.add(i+1);
            }
        }
        int[] answer = result.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}