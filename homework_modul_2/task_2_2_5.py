# task 2.2.5.1

def masa(grams):
    kilo_masa = grams // 1000
    return f"В {grams} граммах содержится {kilo_masa} полных килограмм"

grams = 12345
print(masa(grams))