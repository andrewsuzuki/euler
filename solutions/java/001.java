class Problem001 {
    public int solution() {
        int sum = 0;

        for (int n = 0; n < 1000; n++) {
            if (n % 3 == 0 || n % 5 == 0) {
                sum += n;
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        Problem001 problem = new Problem001();
        System.out.println(problem.solution());
    }
}
