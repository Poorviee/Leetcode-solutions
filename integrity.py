data = input("Enter the data packet: ")

reverse_data = data[::-1]

if data == reverse_data:
    print("Data Integrity Verified (Palindrome)")
else:
    print("Data Corrupted or Modified")