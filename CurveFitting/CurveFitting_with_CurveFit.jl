using CurveFit
using BenchmarkTools
using Plots

function PolyFit(x, y, degree, nx)
    coef = curve_fit(Polynomial, x, y, degree)
    y0b = coef.(nx)
    return y0b
end

xdata = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
ydata = [3.0, 14.0, 23.0, 25.0, 23.0, 15.0, 9.0, 5.0, 9.0, 13.0, 17.0, 24.0, 32.0, 36.0, 46.0]

nx = LinRange(minimum(xdata),maximum(xdata), 100)


result1 = @benchmark PolyFit(xdata, ydata, 1, nx)
println("--------------------time1--------------------")
# minimum, maximum and average execution times in seconds
println("Minimum time: $(minimum(result1.times) / 1e9) seconds")
println("Maximum time: $(maximum(result1.times) / 1e9) seconds")
println("Average time: $(mean(result1.times) / 1e9) seconds")

result2 = @benchmark PolyFit(xdata, ydata, 2, nx)
println("--------------------time2--------------------")
# minimum, maximum and average execution times in seconds
println("Minimum time: $(minimum(result2.times) / 1e9) seconds")
println("Maximum time: $(maximum(result2.times) / 1e9) seconds")
println("Average time: $(mean(result2.times) / 1e9) seconds")

result3 = @benchmark PolyFit(xdata, ydata, 3, nx)
println("--------------------time3--------------------")
# minimum, maximum and average execution times in seconds
println("Minimum time: $(minimum(result3.times) / 1e9) seconds")
println("Maximum time: $(maximum(result3.times) / 1e9) seconds")
println("Average time: $(mean(result3.times) / 1e9) seconds")

yfit1 = PolyFit(xdata, ydata, 1, nx)
yfit2 = PolyFit(xdata, ydata, 2, nx)
yfit3 = PolyFit(xdata, ydata, 3, nx)
scatter(xdata, ydata, label="Data")
plot!(nx, yfit1, label="Degree1")
plot!(nx, yfit2, label="Degree2")
plot!(nx, yfit3, label="Degree3")
