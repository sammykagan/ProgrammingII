import csv
import matplotlib.pyplot as plt
import numpy as np

with open("global_firearm_data.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

#print(data)
headers = data.pop(0)
#print(headers)

homicides_per_100k = []
firearms_per_100 = []
comps = ["Australia", "Austria", "Belgium", "Canada", "Croatia", "Denmark", "England and Wales", "France", "Geramny", "Iceland", "Ireland, Italy", "India", "Korea, South", "Singapore", "Spain", "Sweden", "Taiwan", "Switzerland", "United States", "Turkey"]
countries = []

for country in data:
    if country[0] in comps:
        try:
            homicides = float(country[5])
            firearms = float(country[-2])
            name = country[0]
            homicides_per_100k.append(homicides)
            firearms_per_100.append(firearms)
            countries.append(name)
        except:
            print(country[0], "had incomplete data.")

print(countries)
print(firearms_per_100)
print(homicides_per_100k)

plt.figure(1, figsize=(12,6))
plt.scatter(firearms_per_100, homicides_per_100k)

# best fit line
m, b = (np.polyfit(firearms_per_100, homicides_per_100k, 1))
fit_x = [0, 100]
fit_y = [b, m * 100 + b]
plt.plot(fit_x, fit_y)

plt.title("Homicides vs. Gun Ownership by Country")
plt.xlabel("Firearms per 100 people")
plt.ylabel("Homicides by firearm per 100k people")

for i in range(len(countries)):
    plt.annotate(countries[i], xy=(firearms_per_100[i] - 3, homicides_per_100k[i] + 0.05))

plt.show()