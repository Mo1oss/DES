# main.py

from encryption import des_encrypt_block_64
from decryption import des_decrypt_block_64


def hex16_to_bin64(hexa16):
    decimal = int(hexa16, 16)
    bin64 = format(decimal, "064b")
    return bin64


def bin64_to_hex16(bin64):
    return format(int(bin64, 2), "016X")


if __name__ == "__main__":
    plaintext_hex = "0123456789ABCDEF"
    key_hex       = "133457799BBCDFF1"

    plaintext_bin = hex16_to_bin64(plaintext_hex)
    key_bin       = hex16_to_bin64(key_hex)

    ciphertext_bin = des_encrypt_block_64(plaintext_bin, key_bin)
    ciphertext_hex = bin64_to_hex16(ciphertext_bin)

    assert ciphertext_hex == "85E813540F0AB405"

    decrypted_bin = des_decrypt_block_64(ciphertext_bin, key_bin)
    decrypted_hex = bin64_to_hex16(decrypted_bin)

    assert decrypted_hex == plaintext_hex

    print("Plaintext (hex): ", plaintext_hex)
    print("Key       (hex): ", key_hex)
    print("Cipher    (hex): ", ciphertext_hex)
    print("Decrypted (hex): ", decrypted_hex)
    print("✔ All DES tests passed successfully!")
