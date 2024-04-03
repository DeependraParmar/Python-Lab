amazon = {'a','b','c','d'}
microsoft = {'c','f','h'}
atlassian = {'g','h'}

print("Students with multiple placement are: ", ((amazon & microsoft) | (microsoft & atlassian)))