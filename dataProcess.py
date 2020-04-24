all_txt = open(u"my_data/1587652530_P.fasta", 'r').readlines()
for i in range(0, 23352, 4):
    f = open('./newfasta_p.txt','a+')
#     f.write(all_txt[i + 1].split()[0])
    f.write(all_txt[i].strip())
    f.write('\n')
    f.write(all_txt[i+2].strip())
    f.write('\n')
    f.close()