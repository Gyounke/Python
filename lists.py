friends = ["Bod", "Ally", "Serge"]
lucky_numbers = [ 21,59, 78, 4, 6, 10, 29, 48]

print(friends)

friends[1] = "GIS"
print(friends[2])
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Crew")
print(friends)

friends.insert(2, "Ken")
print(friends)

friends.clear()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)