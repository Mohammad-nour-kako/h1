dec_num = int(input('Enter a Dicemal number:'))
bin_num_list = []
res = dec_num
while res > 0:
    bin_num_list.append(res%2)
    res//=2
bin_num_list.reverse()
bin_num = ""
for bit in bin_num_list:
    bin_num += str(bit)
print('The binary number:',bin_num)
