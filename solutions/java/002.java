class Problem002 {
    public int solution() {
        int nl, n, new_n;
        int sum = 0;

        for (nl = 1, n = 2; n < 4e6; nl = n, n = new_n) {
            if (n % 2 == 0) {
                sum += n;
            }
            new_n = nl + n;
        }

        return sum;
    }

    public static void main(String[] args) {
        Problem002 problem = new Problem002();
        System.out.println(problem.solution());
    }
}
