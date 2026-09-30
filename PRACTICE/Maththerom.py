#initial value 3-2r
#0>dx   dx+4(xk) + 6 ,x++
# 0<dx  dx+4(xk-yk) +10 ,y--,x++
# x==y  break

import matplotlib.pyplot as plt

r = int(input("Enter the radius of circle: "))
li_of_value = []

xk = 0
yk = r
dk = 3 - 2 * r

while xk <= yk:
    li_of_value.append((xk, yk))
    if dk < 0:
        dk = dk + 4 * xk + 6
    else:
        dk = dk + 4 * (xk - yk) + 10
        yk -= 1
    xk += 1

swap_list = [(y, x) for x, y in li_of_value]
li_of_value.extend(reversed(swap_list))
print(li_of_value)
x = [p[0] for p in li_of_value]
y = [p[1] for p in li_of_value]

plt.figure(figsize=(6,6))

plt.plot(x, y, color="blue", linewidth=2, label="Quarter Circle Arc")

plt.scatter(x, y, color="red", s=40, zorder=5, label="Circle Points")

plt.axhline(0, color="black", linewidth=1)  
plt.axvline(0, color="black", linewidth=1)  

for (xi, yi) in li_of_value:
    plt.text(xi+0.2, yi+0.2, f"({xi},{yi})", fontsize=8, color="green")
plt.gca().set_aspect("equal")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
