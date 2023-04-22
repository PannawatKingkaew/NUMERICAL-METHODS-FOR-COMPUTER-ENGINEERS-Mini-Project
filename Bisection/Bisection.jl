using BenchmarkTools

f(x) =  x^2 - 11
function bisection_method(f,a, b, tol)
    if f(a)*f(b) > 0
        println("No root found.")
    else
        while (b - a) >= tol
            midpoint = (a + b) / 2.0
            if f(midpoint) == 0
                return midpoint
            elseif f(a) * f(midpoint) < 0
                b = midpoint
            else
                a = midpoint
            end
        end       
        return (a + b) / 2.0
    end
end

result = @benchmark bisection_method(f,-1, 5, 0.0001)

println("Answer: ", bisection_method(f,-1, 5, 0.0001))
println("Minimum time: $(minimum(result.times) / 1e9) seconds")
println("Maximum time: $(maximum(result.times) / 1e9) seconds")
println("Average time: $(mean(result.times) / 1e9) seconds")
