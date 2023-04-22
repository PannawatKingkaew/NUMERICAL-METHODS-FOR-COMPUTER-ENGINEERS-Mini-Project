using DifferentialEquations
using BenchmarkTools
using Plots

function dydt(u, p, t)
    p * exp(-t)
end

t_span = (0.0, 10.0)
p = 0.1
u0 = 0
localprob = ODEProblem(dydt, u0, t_span, p)

num_sol = @benchmark solve($localprob)

println("Minimum time: $(minimum(num_sol.times) / 1e9) seconds")
println("Maximum time: $(maximum(num_sol.times) / 1e9) seconds")
println("Average time: $(mean(num_sol.times) / 1e9) seconds")

num_sol = solve(localprob)
plot(num_sol, xlabel="t", ylabel="y", label=["y"])
