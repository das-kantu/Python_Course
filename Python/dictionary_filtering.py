# Example 9: Dictionary Filtering Based on Conditions
# Filtering a dictionary to retain only key-value pairs that satisfy a condition.
# Example dictionary

scores = {'a': 85, 'b': 70, 'c': 95, 'd': 60}

# Filtering to retain scores >= 80
filtered_scores = {name: score for name, score in scores.items() if score >= 80}

print('Filtered Scores:', filtered_scores)