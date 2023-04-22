using Roots
using BenchmarkTools

f(x) = x^2 - 11

result = @benchmark Roots.find_zero(f , (-1,5) , Bisection(),xatol =0.0001)

println("Answer: ", Roots.find_zero(f , (-1,5) , Bisection(),xatol =0.0001))
println("Minimum time: $(minimum(result.times) / 1e9) seconds")
println("Maximum time: $(maximum(result.times) / 1e9) seconds")
println("Average time: $(mean(result.times) / 1e9) seconds")