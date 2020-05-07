#function to compute fibonacci, 
#f(n) = f(n - 1) + f(n - 2)

def fibonacci(nth):
    series = []
    i = 0
    
    while len(series) <= nth:
        if i == 0:
            series.append(0)
        elif i == 1:
            series.append(1)
        else: 
            series.append(series[i - 1] + series[i - 2])
        i += 1
    return series
