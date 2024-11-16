outer_variable = "out"

def scope_test(level1):
    print(f'this is one level deep {level1}')
    level1 = "in"
    def scope_test2(level2):
        print(f'this is two levels deep {level2}')
    
    scope_test2(level1)

scope_test(outer_variable)