using DifferentialEquations
using BenchmarkTools
using Plots

function ode_func(du, u, p, t)
    - p[1] * du[1] - p[2] * u[1] + cos(2.0*t)
end

t_span = (0.0, 10.0)
p = [0.1,0.1]

prob = SecondOrderODEProblem(ode_func, 0,0, t_span, p)

# Measure the execution time of the `solve` function
num_sol = @benchmark solve($prob)

# minimum, maximum and average execution times in seconds
println("Minimum time: $(minimum(num_sol.times) / 1e9) seconds")
println("Maximum time: $(maximum(num_sol.times) / 1e9) seconds")
println("Average time: $(mean(num_sol.times) / 1e9) seconds")

# Plot the solution
num_sol = solve(prob)
plot(num_sol, xlabel="t", ylabel="y", label=["y"])
