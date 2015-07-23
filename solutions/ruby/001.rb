def solution
    sum = 0
    1000.times do |n|
        if n % 3 == 0 || n % 5 == 0
            sum += n
        end
    end
    return sum
end

puts solution()
