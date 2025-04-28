# =========================
# Mini-AES 16-bit Encryption and Decryption
# Struktur sesuai spesifikasi:
# SubNibbles, ShiftRows, MixColumns, AddRoundKey, Key Expansion, 3 Rounds
# =========================

# S-Box untuk SubNibbles
SBOX = {
    0x0: 0xE, 0x1: 0x4, 0x2: 0xD, 0x3: 0x1,
    0x4: 0x2, 0x5: 0xF, 0x6: 0xB, 0x7: 0x8,
    0x8: 0x3, 0x9: 0xA, 0xA: 0x6, 0xB: 0xC,
    0xC: 0x5, 0xD: 0x9, 0xE: 0x0, 0xF: 0x7
}

# Inverse S-Box untuk dekripsi
INV_SBOX = {v: k for k, v in SBOX.items()}

# Tabel perkalian untuk GF(2^4) pada MixColumns
GF_MUL_TABLE = [
    [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0],
    [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF],
    [0x0, 0x2, 0x4, 0x6, 0x8, 0xA, 0xC, 0xE, 0x3, 0x1, 0x7, 0x5, 0xB, 0x9, 0xF, 0xD],
    [0x0, 0x3, 0x6, 0x5, 0xC, 0xF, 0xA, 0x9, 0xB, 0x8, 0xD, 0xE, 0x7, 0x4, 0x1, 0x2]
]

# Fungsi perkalian di GF(2^4)
def gf_mul(a, b):
    return GF_MUL_TABLE[a][b]

# SubNibbles - substitusi dengan S-Box
def sub_nibbles(state):
    return [SBOX[n] for n in state]

# ShiftRows - rotasi baris ke kiri
def shift_rows(state):
    return [state[0], state[3], state[2], state[1]]

# MixColumns - mixing antar kolom
def mix_columns(state):
    return [
        gf_mul(0x3, state[0]) ^ gf_mul(0x2, state[1]),
        gf_mul(0x2, state[0]) ^ gf_mul(0x3, state[1]),
        gf_mul(0x3, state[2]) ^ gf_mul(0x2, state[3]),
        gf_mul(0x2, state[2]) ^ gf_mul(0x3, state[3])
    ]

# AddRoundKey - XOR dengan round key
def add_round_key(state, key):
    return [s ^ k for s, k in zip(state, key)]

# Untuk key expansion
def nibble_sub(n):
    return SBOX[n]

# Key Expansion - menghasilkan semua round keys
def key_expansion(key):
    rcon = [0x1, 0x2]  # konstanta round
    w = key.copy()
    for i in range(2):
        temp = nibble_sub(w[4*i + 3]) ^ rcon[i]
        w.append(w[4*i + 0] ^ temp)
        w.append(w[4*i + 1] ^ w[4*i + 4])
        w.append(w[4*i + 2] ^ w[4*i + 5])
        w.append(w[4*i + 3] ^ w[4*i + 6])
    return [w[0:4], w[4:8], w[8:12]]  # 3 round keys

# ==================
# ENCRYPTION PROCESS
# ==================
def encrypt(plaintext, key):
    round_keys = key_expansion(key)  # Generate Round Keys
    state = plaintext
    print(f"Plaintext: {[hex(x) for x in state]}")
    
    # --- ROUND 0: AddRoundKey ---
    print(f"Round Key 0: {[hex(x) for x in round_keys[0]]}")
    state = add_round_key(state, round_keys[0])
    print(f"After Add Round Key (R0): {[hex(x) for x in state]}")

    for i in range(2):  # 2 rounds utama
        # --- SubNibbles ---
        state = sub_nibbles(state)
        print(f"After Sub Nibbles (R{i+1}): {[hex(x) for x in state]}")

        # --- ShiftRows ---
        state = shift_rows(state)
        print(f"After Shift Rows (R{i+1}): {[hex(x) for x in state]}")

        # --- MixColumns (hanya di round 1) ---
        if i < 1:
            state = mix_columns(state)
            print(f"After Mix Columns (R{i+1}): {[hex(x) for x in state]}")

        # --- AddRoundKey ---
        print(f"Round Key {i+1}: {[hex(x) for x in round_keys[i+1]]}")
        state = add_round_key(state, round_keys[i+1])
        print(f"After Add Round Key (R{i+1}): {[hex(x) for x in state]}")

    return state  # Output Ciphertext

# ==================
# DECRYPTION PROCESS
# ==================
def inv_sub_nibbles(state):
    return [INV_SBOX[n] for n in state]

def inv_shift_rows(state):
    return [state[0], state[3], state[2], state[1]]

def inv_mix_columns(state):
    return [
        gf_mul(0x3, state[0]) ^ gf_mul(0x2, state[1]),
        gf_mul(0x2, state[0]) ^ gf_mul(0x3, state[1]),
        gf_mul(0x3, state[2]) ^ gf_mul(0x2, state[3]),
        gf_mul(0x2, state[2]) ^ gf_mul(0x3, state[3])
    ]

def decrypt(ciphertext, key):
    round_keys = key_expansion(key)
    state = ciphertext
    print(f"\nCiphertext: {[hex(x) for x in state]}")
    
    # --- ROUND 2: AddRoundKey ---
    print(f"Round Key 2: {[hex(x) for x in round_keys[2]]}")
    state = add_round_key(state, round_keys[2])
    print(f"After Add Round Key (R2): {[hex(x) for x in state]}")

    # --- Inverse ShiftRows ---
    state = inv_shift_rows(state)
    print(f"After Inv Shift Rows (R2): {[hex(x) for x in state]}")

    # --- Inverse SubNibbles ---
    state = inv_sub_nibbles(state)
    print(f"After Inv Sub Nibbles (R2): {[hex(x) for x in state]}")

    # --- ROUND 1: AddRoundKey ---
    print(f"Round Key 1: {[hex(x) for x in round_keys[1]]}")
    state = add_round_key(state, round_keys[1])
    print(f"After Add Round Key (R1): {[hex(x) for x in state]}")

    # --- Inverse MixColumns ---
    state = inv_mix_columns(state)
    print(f"After Inv Mix Columns (R1): {[hex(x) for x in state]}")

    # --- Inverse ShiftRows ---
    state = inv_shift_rows(state)
    print(f"After Inv Shift Rows (R1): {[hex(x) for x in state]}")

    # --- Inverse SubNibbles ---
    state = inv_sub_nibbles(state)
    print(f"After Inv Sub Nibbles (R1): {[hex(x) for x in state]}")

    # --- ROUND 0: AddRoundKey ---
    print(f"Round Key 0: {[hex(x) for x in round_keys[0]]}")
    state = add_round_key(state, round_keys[0])
    print(f"After Add Round Key (R0): {[hex(x) for x in state]}")

    return state  # Output Plaintext

# ==================
# UTILITY FUNCTIONS
# ==================
def str_to_nibbles(s):
    return [int(c, 16) for c in s]

def nibbles_to_str(nibbles):
    return ''.join(f"{n:X}" for n in nibbles)

# ==================
# MAIN PROGRAM
# ==================
if __name__ == "__main__":
    while True:
        print("\nPilih operasi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            plaintext = input("plaintext (4 hex): ")
            key = input("key (4 hex): ")
            assert len(plaintext) == 4 and len(key) == 4
            pt_nibbles = str_to_nibbles(plaintext)
            key_nibbles = str_to_nibbles(key)
            ct = encrypt(pt_nibbles, key_nibbles)
            print(f"Ciphertext: {nibbles_to_str(ct)}")
        elif choice == '2':
            ciphertext = input("ciphertext (4 hex): ")
            key = input("key (4 hex): ")
            assert len(ciphertext) == 4 and len(key) == 4
            ct_nibbles = str_to_nibbles(ciphertext)
            key_nibbles = str_to_nibbles(key)
            pt = decrypt(ct_nibbles, key_nibbles)
            print(f"Decrypted plaintext: {nibbles_to_str(pt)}")
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
