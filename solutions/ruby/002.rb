def solution()
    nl = 1
    n = 2
    sum = 0

    while n < 4E6
        if n % 2 == 0
            sum += n
        end
        new_n = n + nl
        nl = n
        n = new_n
    end

    sum
end

if __FILE__ == $0
    puts solution()
end
