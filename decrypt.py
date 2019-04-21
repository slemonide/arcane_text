#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    user_input = input("> ")
    
    user_input = iter(user_input)
    
    decrypted_text = ""
    
    for c in user_input:
        char = ord(c)
        offset = ord(next(user_input))

        decrypted_text = decrypted_text + chr(((char - 32) - (offset - 32)) % 90 + 32)

    print("======================================")
    print(decrypted_text)
    print("======================================")