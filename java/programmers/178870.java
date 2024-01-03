class 178870 {
    public int[] solution(int[] sequence, int k) {
        int cur_index = 0;
        int cur_end_index = 0;
        int shortest_length = Integer.MAX_VALUE;
        int[] shortest_indexes = {0,0};
        int total = sequence[0];
        while(cur_index < sequence.length) {
            //비내림차순으로 정렬
            if (total < k) {
                if (cur_end_index == sequence.length - 1) {
                    return shortest_indexes;
                }
                cur_end_index++;
                total += sequence[cur_end_index];
            }
            else if (total == k) {
                int length = cur_end_index - cur_index;
                if (length < shortest_length) {
                    shortest_length = length;
                    shortest_indexes[0] = cur_index;
                    shortest_indexes[1] = cur_end_index;
                }
                total -= sequence[cur_index];
                cur_index++;
                if (cur_end_index < cur_index) {
                    cur_end_index = cur_index;
                }
            }
            else if (total > k) {
                if (cur_end_index == cur_index) {
                    return shortest_indexes;
                }
                total -= sequence[cur_index];
                cur_index++;
            }
        }
        return shortest_indexes;
    }
}