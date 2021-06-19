def getPermutations(collection,m,repetition):
    if m > len(collection) and not repetition: return []

    def permutateHelper(collection,m,repetition,permutations, curr_perm = []):
        if m == 1:
            for element in collection:
                new_perm = curr_perm[:]
                new_perm.append(element)
                permutations.append(new_perm)
        else:
            for index,element in enumerate(collection):
                curr_perm.append(element)
                if repetition:
                    permutateHelper(collection,m-1,repetition,permutations,curr_perm)
                else:
                    permutateHelper(collection[:index]+collection[index+1:],m-1,repetition,permutations,curr_perm)
                curr_perm.pop()
    
    permutations = []
    permutateHelper(collection,m,repetition,permutations)
    return permutations

def getCombinations(collection,m,repetition):
    if m > len(collection) and not repetition: return []

    def combineHelper(collection,m,repetition,combinations, curr_perm = []):
        if m == 1:
            for element in collection:
                new_perm = curr_perm[:]
                new_perm.append(element)
                key = ''.join(sorted([str(elem) for elem in new_perm]))
                if key not in combinations:
                    combinations[key] = new_perm
        else:
            for index,element in enumerate(collection):
                curr_perm.append(element)
                if repetition:
                    combineHelper(collection,m-1,repetition,combinations,curr_perm)
                else:
                    combineHelper(collection[:index]+collection[index+1:],m-1,repetition,combinations,curr_perm)
                curr_perm.pop()

    combinations = {}
    combineHelper(collection,m,repetition,combinations)
    combination_sets = []
    for key in combinations:
        combination_sets.append(combinations[key])
    return combination_sets

if __name__ == '__main__':
    def test(type,input,m,repeat):
        print(f'Type: {type}, input: {input}, m = {m}, repetition allowed: {repeat}')
        if type == 'permutation':
            for permutation in getPermutations(input,m,repeat):
                print(permutation)
        else:
            for combintation in getCombinations(input,m,repeat):
                print(combintation)

    collection = ['a','b','c']
    m = 2
    test('permutation',collection,m,False)
    test('permutation',collection,m,True)
    test('combintation',collection,m,False)
    test('combintation',collection,m,True)
    m = 3
    test('permutation',collection,m,False)
    test('permutation',collection,m,True)
    test('combintation',collection,m,False)
    test('combintation',collection,m,True)
    m = 4
    test('permutation',collection,m,False)
    test('permutation',collection,m,True)
    test('combintation',collection,m,False)
    test('combintation',collection,m,True)