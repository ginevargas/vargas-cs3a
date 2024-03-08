import streamlit as st

st.header("XOR Cipher")

plaintext = bytes(st.text_area("Plain Text:").encode())
key = bytes(st.text_input("Key:").encode())

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""

    ciphertext = bytearray()
    
    for i in range(len(plaintext)):
       # plaintext_byte = plaintext[i]
      #  key_byte = key[i % len(key)]
        ciphertext.append(plaintext[i] ^ key[i % len(key)])
        st.write(f"Plaintext byte: {plaintext[i]:08b} = {chr(plaintext[i])}")
        st.write(f"Key byte:       {key [i % len(key)]:08b} = {chr(key[i % len (key)])}")
        st.write(f"XOR result:     {ciphertext[-1]:08b} = {chr(ciphertext[-1])}")
        st.write("--------------------")       

    return ciphertext  

def xor_decrypt(ciphertext, key):
    """Decrypts ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key) # XOR decryption is the same as encryption 

if st.button("Submit"): 
    if not key:
        st.error("Invalid key")
    else:
        if not(1 < len(plaintext) >= len(key)>=1):
            st.write("Plaintext length should be equal or greater than the length of key")
        elif not plaintext != key: 
            st.write("Plaintext should not be equal to the key")
    
        else: 
            cipher_text = xor_encrypt(plaintext, key)
            st.write("Ciphertext:", cipher_text.decode())
    
            decryption =  xor_decrypt(cipher_text, key)
            st.write("Decrypted:", decryption.decode())

st.balloons()
st.snow()

import streamlit as st

st.header("Primitive Root Calculator")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def compute_modulus(base, exponent, mod):
    result = 1
    for _ in range(exponent):
        result = (result * base) % mod
    return result

def get_primitive_input(prompt):
    user_input = st.text_input(prompt)
    return user_input

def get_primitive_roots(p):
    primitive_roots = []
    for g in range(1, p):
        is_primitive_root = True
        powers = set()
        for j in range(1, p):
            res = compute_modulus(g, j, p)
            powers.add(res)
            if res == 1:
                break
        if len(powers) == p - 1:
            primitive_roots.append(g)
    return primitive_roots

def print_primitive_roots(p, primitive_number):
    if not is_prime(p):
        st.write(f"{p} is not a prime number!!")
        return  
  
    if not 1 <= primitive_number < p:
        st.error("Please enter a number greater than 1.")
        return

    print_results = []
    for g in range(1, p):
        output = []
        for j in range(1, p):
            res = compute_modulus(g, j, p)
            output.append(f"{g}^{j} mod {p} = {res}")
            if res == 1:
                break
        if g in get_primitive_roots(p):
            output[-1] += f" ==> {g} is primitive root of {p}, "
        else:
            output.append('')
        print_results.append(", ".join(output))
    
    st.write("\n".join(print_results))
    primitive_roots = get_primitive_roots(p)
    if primitive_number in primitive_roots:
        st.write(f"{primitive_number} is primitive root: True {primitive_roots}")
    else:
        st.write(f"{primitive_number} is NOT primitive root: False {primitive_roots}")

# Streamlit UI
p_input = get_primitive_input("Enter a prime number:")
primitive_number_input = get_primitive_input("Enter a primitive number:")
if st.button('Calculate'):
    if p_input and primitive_number_input:
        p = int(p_input)
        primitive_number = int(primitive_number_input)
        print_primitive_roots(p, primitive_number)
