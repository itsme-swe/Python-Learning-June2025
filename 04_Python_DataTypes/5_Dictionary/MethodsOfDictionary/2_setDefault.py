# 💥 setdefault() returns the value of a key (if the key is in dictionary). Else, it inserts a key with the default value to the dictionary.

d1 = {1: "defender", 2: "rubicon", 3: "lexus", 4: "fortuner"}

d1.setdefault(5)

print(d1) # {1: 'defender', 2: 'rubicon', 3: 'lexus', 4: 'fortuner', 5: None}
