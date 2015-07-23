function solution() {
    var sum = 0;

    for (var i = 0; i < 1000; i++) {
        if (i % 5 === 0 || i % 3 === 0) {
            sum += i;
        }
    }

    return sum;
}

if (require.main === module) {
    console.log(solution());
}
