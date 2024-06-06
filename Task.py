def to_binary(num, store):
    bin_num = str(bin(num)[2::])
    s = bin_num.zfill(store)
    translation_table = str.maketrans("01", "10")
    s = s.translate(translation_table)

to_binary(9,8)