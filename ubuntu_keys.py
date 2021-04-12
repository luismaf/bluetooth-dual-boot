LTK = "af,ba,0b,39,32,66,c0,cc,17,b6,dc,da,cc,4f,5e,1f"
KeyLength = "00000010"
ERand = "20,dd,df,fa,77,9a,67,11"
EDIV = "0000f374"
IRK = "4f,d5,a1,5a,43,c2,9f,d4,7f,e0,43,ad,8a,af,3b,27"

# Calculate 'Key' value
IRK = "".join(IRK.split(",")).upper()
print("[IdentityResolvingKey]\nKey={}".format(IRK))

# Calculate 'Key' value
Key = "".join(LTK.split(",")).upper()
print("\n[LongTermKey]\nKey={}".format(Key))

# Print Autenticated=0
print("Authenticated=0");

# Calculate 'EncSize' value
EncSize = int(KeyLength, 16)  # Convert hex to decimal
print("EncSize={}".format(EncSize))

# Calculate EDiv value
EDiv = int(EDIV, 16)  # Convert hex to decimal
print("EDiv={}".format(EDiv))

# Calculate Rand value
ERand_list = ERand.split(",")
ERand_list.reverse()  # Reverse order of hex pairs
ERand_rev_hex = "".join(ERand_list)
Rand = int(ERand_rev_hex, 16)  # Convert hex to decimal
print("Rand={}".format(Rand))
