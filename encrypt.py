#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

while True:
    user_input = input("> ")
    
    encrypted_string = ""
    
    for c in user_input:
        offset = random.randint(0, 90)
        
        encrypted_string = encrypted_string + chr((ord(c) - 32 + offset) % 90 + 32) + chr(offset + 32)
    
    print("======================================")
    print(encrypted_string)
    print("======================================")