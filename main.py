from js import document
import math

def factorial(n):
    return math.factorial(n)

def calculate(event=None):
    n = int(document.getElementById("n_input").value)
    r = int(document.getElementById("r_input").value)

    if r > n or n < 0 or r < 0:
        result = "Invalid input: ensure 0 ≤ r ≤ n"
    else:
        perm = factorial(n) // factorial(n - r)
        comb = factorial(n) // (factorial(r) * factorial(n - r))
        result = f"P({n}, {r}) = {perm}<br>C({n}, {r}) = {comb}"

    document.getElementById("output").innerHTML = result
