function solution() {
    var nl;
    var n;
    var sum = 0;

    for (nl = 1, n = 2; n < 4e6; nl = n, n = new_n) {
        if (n % 2 === 0) {
            sum += n;
        }

        new_n = n + nl;
    }

    return sum;
}

if (require.main === module) {
    console.log(solution());
}
