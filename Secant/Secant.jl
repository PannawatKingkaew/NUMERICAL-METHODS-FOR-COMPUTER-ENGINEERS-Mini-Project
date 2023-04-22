using BenchmarkTools
f(x) = x^2 - 11
function secant_method(f,a, b, tol)
    if f(a)*f(b) > 0
        println("No root found.")
    else
        while (b - a) >= tol
            midpoint = a - f(a)*(b-a)/(f(b)-f(a))
            if f(midpoint) == 0
                return midpoint
            elseif f(a)*f(midpoint) < 0
                b = midpoint
            else
                a = midpoint
            end
        end       
        return a - f(a)*(b-a)/(f(b)-f(a))
    end
end

result = @benchmark secant_method(f,-1, 5, 0.0001)

println("Answer: ", secant_method(f,-1, 5, 0.0001))
println("Minimum time: $(minimum(result.times) / 1e9) seconds")
println("Maximum time: $(maximum(result.times) / 1e9) seconds")
println("Average time: $(mean(result.times) / 1e9) seconds")

