def boolean_query(query, inverted_index):
    # Split the query into terms and operators
    query_elements = query.split(' ')

    # Initialize the result set with the documents of the first term
    result_set = set(inverted_index[query_elements[0]])

    # Iterate over the rest of the query elements
    for i in range(1, len(query_elements), 2):
        operator = query_elements[i]
        term = query_elements[i+1]

        # Retrieve the documents of the term
        term_docs = set(inverted_index[term])

        # Apply the operator
        if operator == '.':
            result_set = result_set.intersection(term_docs)
        elif operator == '!':
            result_set = result_set.difference(term_docs)
        elif operator == '+':
            result_set = result_set.union(term_docs)

    return  boolean_query(".term1 !term2 .term3 .term4", map_dict)