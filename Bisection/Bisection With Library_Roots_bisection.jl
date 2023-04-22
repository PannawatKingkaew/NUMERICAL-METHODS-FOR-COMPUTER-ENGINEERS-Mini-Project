using Roots
using BenchmarkTools

f(x) = x^2 - 11

result = @benchmark Roots.bisection(f,-1, 5; xatol = 0.0001)

println("Answer: ", Roots.bisection(f,-1, 5; xatol = 0.0001))
println("Minimum time: $(minimum(result.times) / 1e9) seconds")
println("Maximum time: $(maximum(result.times) / 1e9) seconds")
println("Average time: $(mean(result.times) / 1e9) seconds")