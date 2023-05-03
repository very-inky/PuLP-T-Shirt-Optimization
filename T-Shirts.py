import pulp
# 
# Initialize model
model = pulp.LpProblem("Tshirt_Problem", pulp.LpMaximize)
 
# Define variables
x1 = pulp.LpVariable("white", lowBound=0, upBound=50, cat="Integer")
x2 = pulp.LpVariable("blue", lowBound=0, upBound=15, cat="Integer")
x3 = pulp.LpVariable("yellow", lowBound=0, upBound=10, cat="Integer")
x4 = pulp.LpVariable("red", lowBound=0, upBound=12, cat="Integer")
 
# Profit
model += 7 * x1 + 8 * x2 + 8 * x3 + 6 * x4, "Total Profit"
 
# Constraints
model += x1 + x2 + x3 + x4 == 50  # Total shirts constraint
model += 20 * x2 + 20 * x3 + 40 * x4 <= 480  # Time constraint
 
# Solve the problem
model.solve()
 
# Print the solution
print(f"White shirts: {x1.value()}")
print(f"Blue shirts: {x2.value()}")
print(f"Yellow shirts: {x3.value()}")
print(f"Red shirts: {x4.value()}")
print(f"Total profit: {pulp.value(model.objective)}")
