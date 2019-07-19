from efficient_apriori import apriori

transactions = [('eggs', 'bacon', 'soup'),
                ('eggs', 'bacon', 'apple'),
                ('soup', 'bacon', 'banana')]

itemsets, rules = apriori(transactions, min_support=0.6,  min_confidence=0.8)

print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}]
