def filter_freezing(temperatures):
    above_freezing = []
    for temp in temperatures:
        if temp > 0:
            above_freezing.append(temp)
    return above_freezing
print(filter_freezing([12, 15, 18, 5]))