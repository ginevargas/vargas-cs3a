import streamlit as st

st.header("Primitive Root")

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
def is_primitive_check(g, p): 
    primitive_roots = []
    for i in range(1, p):
        temp = set()
        output = ''
        for j in range(1, p):
            residue = pow(i, j, p)
            output += f"{i}^{j} mod {p} = {residue}"
            if j < p - 1:
                output += ", "
            temp.add(residue)
            if residue == 1:
                break
        if len(temp) == p - 1:
            primitive_roots.append(i)
            output += f" ==> {i} is primitive root of {p}, "
        print(output)
    if g in primitive_roots:
        return True, primitive_roots
    else:
        return False, primitive_roots
            
    
q = int(input())
g = int(input())

if is_prime(q):
    is_primitive_root, primitive_roots = is_primitive_check(g, q)
    if is_primitive_root:
        st.write(f"{g} is primitive root: {is_primitive_root} {primitive_roots}")
    else:
        st.write(f"{g} is NOT primitive root of {q} - List of Primitive roots: {primitive_roots}")
else:
    st.write(f"{q} is not a prime number!!")

