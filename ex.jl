using BenchmarkTools

function test(n)
    return sum(0:n-1)
end

n = 10000

execution_time = @benchmark test(n)
println("Average time: $(mean(execution_time.times) / 1e9) seconds")