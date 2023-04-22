using DifferentialEquations
using BenchmarkTools
using Plots

function ode_func(du, u, p, t)
    du[1] = u[2]
    du[2] = -p[2]/p[1] * u[2] + cos(2.0*t)/p[1]
end

t_span = (0.0, 10.0)
p = [0.1,0.1]
u0 = [0.0,0.0]
prob = ODEProblem(ode_func, u0, t_span, p)

num_sol = @benchmark solve($prob)

println("Minimum time: $(minimum(num_sol.times) / 1e9) seconds")
println("Maximum time: $(maximum(num_sol.times) / 1e9) seconds")
println("Average time: $(mean(num_sol.times) / 1e9) seconds")

num_sol = solve(prob)
plot(num_sol, xlabel="t", ylabel="y", label=["y"])
