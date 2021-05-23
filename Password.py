def count_chars(str):
     upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1
          elif str[i] >= '0' and str[i] <= '9': number_ctr += 1
          else: special_ctr += 1
     return upper_ctr, lower_ctr, number_ctr, special_ctr

num = int(input("Enter length of String:"))

password  = input("Enter Password:")
u, l, n, s = count_chars(password)
print('Special characters: ',s)
print('Digits: ',n)
print('\nUppercase alphabets: ',u)
print('Lowercase alphabets: ',l)

if(num<8):
    print((8 - num)," more characters should be added" )
else:
    print("Strong Password. Good to go!")