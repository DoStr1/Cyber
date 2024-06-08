def to_binary(num, store):
    bin_num = bin(num)[2:]
    if len(bin_num) >= store:
        print("Need More Space")
        return
    
    bin_num = bin_num.zfill(store)
    
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in bin_num)
    twos_complement = list(ones_complement)
    
    carry = 1
    for i in range(len(twos_complement) - 1, -1, -1):
        if carry == 0:
            break
        if twos_complement[i] == '1':
            twos_complement[i] = '0'
        else:
            twos_complement[i] = '1'
            carry = 0

    twos_complement_str = ''.join(twos_complement)
    result = '1' + twos_complement_str[1:]  
    
    print(result)



to_binary(42,8)