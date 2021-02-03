#!/urs/local/bin/python

import os
import os.path
import subprocess

from itertools import combinations

path = os.path.expanduser("~/generate_backbone")

# Get all combination of [1, 2, 3]
# of length 3
picking = 1
comb = combinations(['ch', 'sk', 'ta', 'th', 'vn', 'de', 'ge', 'ca', 'me', 'us', 'cl', 'pe'], picking)

#filename = 'select_2.txt'
#with open("/Users/chalermpong/Desktop/"+filename, "w") as file:
#	for i in comb:
#		i = ''.join(map(str, i))
#		i = i
#		file.write("%s\n" % i)

#filename = 'prrsv_filters_eu_'

count = 0

for i in comb:
	i = ''.join(map(str, i))
	i = i

	country_1 = (i[0:2])
	country_2 = (i[2:4])
	country_3 = (i[4:6])
	country_4 = (i[6:8])
	country_5 = (i[8:10])
	country_6 = (i[10:12])
	country_7 = (i[12:14])
	country_8 = (i[14:16])
	country_9 = (i[16:18])
	country_10 = (i[18:20])
	country_11 = (i[20:22])
	country_12 = (i[22:24])

	if country_1 == "ch":
		fasta_1 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "sk":
		fasta_1 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "ta":
		fasta_1 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "th":
		fasta_1 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "vn":
		fasta_1 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "de":
		fasta_1 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "ge":
		fasta_1 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "ca":
		fasta_1 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "me":
		fasta_1 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "us":
		fasta_1 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "cl":
		fasta_1 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "pe":
		fasta_1 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"

	if country_2 == "ch":
		fasta_2 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "sk":
		fasta_2 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "ta":
		fasta_2 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "th":
		fasta_2 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "vn":
		fasta_2 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "de":
		fasta_2 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "ge":
		fasta_2 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "ca":
		fasta_2 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "me":
		fasta_2 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "us":
		fasta_2 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "cl":
		fasta_2 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "pe":
		fasta_2 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"

	if country_3 == "ch":
		fasta_3 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "sk":
		fasta_3 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "ta":
		fasta_3 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "th":
		fasta_3 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "vn":
		fasta_3 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "de":
		fasta_3 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "ge":
		fasta_3 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "ca":
		fasta_3 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "me":
		fasta_3 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "us":
		fasta_3 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "cl":
		fasta_3 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "pe":
		fasta_3 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"

	if country_4 == "ch":
		fasta_4 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "sk":
		fasta_4 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "ta":
		fasta_4 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "th":
		fasta_4 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "vn":
		fasta_4 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "de":
		fasta_4 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "ge":
		fasta_4 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "ca":
		fasta_4 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "me":
		fasta_4 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "us":
		fasta_4 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "cl":
		fasta_4 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "pe":
		fasta_4 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"

	if country_5 == "ch":
		fasta_5 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "sk":
		fasta_5 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "ta":
		fasta_5 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "th":
		fasta_5 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "vn":
		fasta_5 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "de":
		fasta_5 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "ge":
		fasta_5 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "ca":
		fasta_5 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "me":
		fasta_5 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "us":
		fasta_5 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "cl":
		fasta_5 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "pe":
		fasta_5 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"

	if country_6 == "ch":
		fasta_6 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "sk":
		fasta_6 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "ta":
		fasta_6 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "th":
		fasta_6 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "vn":
		fasta_6 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "de":
		fasta_6 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "ge":
		fasta_6 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "ca":
		fasta_6 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "me":
		fasta_6 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "us":
		fasta_6 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "cl":
		fasta_6 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "pe":
		fasta_6 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"

	if country_7 == "ch":
		fasta_7 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "sk":
		fasta_7 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "ta":
		fasta_7 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "th":
		fasta_7 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "vn":
		fasta_7 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "de":
		fasta_7 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "ge":
		fasta_7 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "ca":
		fasta_7 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "me":
		fasta_7 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "us":
		fasta_7 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "cl":
		fasta_7 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "pe":
		fasta_7 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"

	if country_8 == "ch":
		fasta_8 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "sk":
		fasta_8 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "ta":
		fasta_8 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "th":
		fasta_8 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "vn":
		fasta_8 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "de":
		fasta_8 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "ge":
		fasta_8 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "ca":
		fasta_8 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "me":
		fasta_8 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "us":
		fasta_8 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "cl":
		fasta_8 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "pe":
		fasta_8 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"

	if country_9 == "ch":
		fasta_9 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "sk":
		fasta_9 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "ta":
		fasta_9 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "th":
		fasta_9 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "vn":
		fasta_9 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "de":
		fasta_9 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "ge":
		fasta_9 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "ca":
		fasta_9 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "me":
		fasta_9 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "us":
		fasta_9 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "cl":
		fasta_9 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "pe":
		fasta_9 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"

	if country_10 == "ch":
		fasta_10 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "sk":
		fasta_10 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "ta":
		fasta_10 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "th":
		fasta_10 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "vn":
		fasta_10 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "de":
		fasta_10 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "ge":
		fasta_10 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "ca":
		fasta_10 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "me":
		fasta_10 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "us":
		fasta_10 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "cl":
		fasta_10 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "pe":
		fasta_10 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"

	if country_11 == "ch":
		fasta_11 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "sk":
		fasta_11 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "ta":
		fasta_11 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "th":
		fasta_11 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "vn":
		fasta_11 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "de":
		fasta_11 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "ge":
		fasta_11 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "ca":
		fasta_11 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "me":
		fasta_11 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "us":
		fasta_11 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "cl":
		fasta_11 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "pe":
		fasta_11 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"

	if country_12 == "ch":
		fasta_12 = path+"/FASTA/NA/01_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "sk":
		fasta_12 = path+"/FASTA/NA/02_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "ta":
		fasta_12 = path+"/FASTA/NA/03_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "th":
		fasta_12 = path+"/FASTA/NA/04_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "vn":
		fasta_12 = path+"/FASTA/NA/05_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "de":
		fasta_12 = path+"/FASTA/NA/06_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "ge":
		fasta_12 = path+"/FASTA/NA/07_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "ca":
		fasta_12 = path+"/FASTA/NA/08_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "me":
		fasta_12 = path+"/FASTA/NA/09_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "us":
		fasta_12 = path+"/FASTA/NA/10_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "cl":
		fasta_12 = path+"/FASTA/NA/11_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "pe":
		fasta_12 = path+"/FASTA/NA/12_prrsv_filters_na_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"

	#fasta_1 = "/Users/chalermpong/Desktop/generate_backbone/FASTA/EU/01_prrsv_filters_eu_"+country_1+".fasta"
	#fasta_2 = "/Users/chalermpong/Desktop/generate_backbone/FASTA/EU/01_prrsv_filters_eu_"+country_2+".fasta"

	#cp_1 = "cp "+fasta_1+" /Users/chalermpong/Desktop/generate_backbone/merge"
	#cp_2 = "cp "+fasta_2+" /Users/chalermpong/Desktop/generate_backbone/merge"

	count = count + 1
	str_count = str(count)
	
	if str_count == "1":
		merge_no = "0"+str_count
	elif str_count == "2":
		merge_no = "0"+str_count
	elif str_count == "3":
		merge_no = "0"+str_count
	elif str_count == "4":
		merge_no = "0"+str_count
	elif str_count == "5":
		merge_no = "0"+str_count
	elif str_count == "6":
		merge_no = "0"+str_count
	elif str_count == "7":
		merge_no = "0"+str_count
	elif str_count == "8":
		merge_no = "0"+str_count
	elif str_count == "9":
		merge_no = "0"+str_count
	else:
		merge_no = str_count

	if picking == 1:
		dir_comb = "comb_01"
	elif picking == 2:
		dir_comb = "comb_02"
	elif picking == 3:
		dir_comb = "comb_03"
	elif picking == 4:
		dir_comb = "comb_04"
	elif picking == 5:
		dir_comb = "comb_05"
	elif picking == 6:
		dir_comb = "comb_06"
	elif picking == 7:
		dir_comb = "comb_07"
	elif picking == 8:
		dir_comb = "comb_08"
	elif picking == 9:
		dir_comb = "comb_09"
	elif picking == 10:
		dir_comb = "comb_10"
	elif picking == 11:
		dir_comb = "comb_11"
	elif picking == 12:
		dir_comb = "comb_12"

	merge_name = "prrsv_filters_na_"+i
	merge_fasta = "cat "+path+"/merge/*.fasta > "+path+"/merge/"+"ref_"+merge_name+".fasta"

	fasta_merge = path+"/merge/"+"ref_"+merge_name+".fasta"

	#cp_fasta_merge = "cp "+fasta_merge+" "+path+"/"+dir_comb+"/"+merge_no+"_"+merge_name
	cp_fasta_merge = "cp "+fasta_merge+" "+path+"/"+dir_comb+"/"+merge_name

	rm = "rm "+path+"/merge/*"

	try:
		#path_dir_name = os.path.abspath(path+"/"+dir_comb+"/"+merge_no+"_"+merge_name)
		path_dir_name = os.path.abspath(path+"/"+dir_comb+"/"+merge_name)
		#if not os.path.exists(path+"/"+dir_comb+"/"+merge_no+"_"+merge_name):
		if not os.path.exists(path+"/"+dir_comb+"/"+merge_name):
			os.makedirs(path_dir_name)
	except OSError as e:
		if e.errno == 17:
			break

	merge_sh_path = path+"/merge.sh"
	#merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	
	if picking == 1:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 2:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 3:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 4:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 5:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 6:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 7:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 8:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 9:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 10:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 11:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 12:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+cp_12+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]

	with open(merge_sh_path, 'w') as rsh:
		rsh.writelines(merge_sh)
	subprocess.call(['chmod', '+x', merge_sh_path])
	subprocess.call(merge_sh_path)

	path_comb = path+"/"+dir_comb
	#foldername = merge_no+"_"+merge_name
	foldername = merge_name
	filename = "ref_"+merge_name

	# 1. Prepare your reference alignment
	# 1.1 Alignment with MAFFT.
	alignment = "mafft --auto "+path_comb+"/"+foldername+"/"+filename+".fasta > "+path_comb+"/"+foldername+"/"+filename+".aln.fasta"

	#1.2 Remove duplicate with Seqmagick.
	deduplicate = "seqmagick convert --deduplicate-sequences "+path_comb+"/"+foldername+"/"+filename+".aln.fasta "+path_comb+"/"+foldername+"/"+filename+".aln.dedup.fasta"

	# 2. When you have your alignment ready
	# 2.1 Build tree with FastTree (Model selected) and cerate a log file.
	build_tree = "FastTree -log "+path_comb+"/"+foldername+"/"+filename+".tree.log -nt -gtr "+path_comb+"/"+foldername+"/"+filename+".aln.dedup.fasta > "+path_comb+"/"+foldername+"/"+filename+".tree"

	# 2.2 Make reference package with Taxtastic.
	make_reference = "taxit create -l nod -P "+path_comb+"/"+foldername+"/"+filename+".refpkg --aln-fasta "+path_comb+"/"+foldername+"/"+filename+".aln.dedup.fasta --tree-stats "+path_comb+"/"+foldername+"/"+filename+".tree.log --tree-file "+path_comb+"/"+foldername+"/"+filename+".tree"

	# 2.3 Convert alignment format from Fasta to Stockholm format.
	convert_alignment = "seqmagick convert "+path_comb+"/"+foldername+"/"+filename+".aln.dedup.fasta "+path_comb+"/"+foldername+"/"+filename+".aln.dedup.sto"

	# 2.4 Build HMM profile with HMM 
	build_hmm = "hmmbuild "+path_comb+"/"+foldername+"/"+filename+".aln.dedup.hmm "+path_comb+"/"+foldername+"/"+filename+".aln.dedup.sto"

	sh_path  = path_comb+"/generate_backbone.sh"
	sh = ["#!/bin/bash\n", 'cmd="'+alignment+' '+'&& '+deduplicate+' '+'&& '+build_tree+' '+'&& '+make_reference+' '+'&& exit'+'"'+'\n', "eval $cmd"]  
	with open(sh_path, 'w') as rsh:
	    rsh.writelines(sh)
	subprocess.call(['chmod', '+x', sh_path])
	subprocess.call(sh_path)

	sh_path_  = path_comb+"/generate_backbone_.sh"
	sh_ = ["#!/bin/bash\n", 'cmd="'+convert_alignment+' '+'&& '+build_hmm +' '+'&& exit'+'"'+'\n', "eval $cmd"]
	with open(sh_path_, 'w') as rsh_:
	    rsh_.writelines(sh_)
	subprocess.call(['chmod', '+x', sh_path_])
	subprocess.call(sh_path_)

	#minio_path = "minio/prrsv/generate_backbone/na/"+dir_comb+"/"
	minio_path = "minio/prrsv/generate_backbone_rerun/na/"+dir_comb+"/"
	minio_cp = path_dir_name

	rm_ = "rm -rfv "+path_dir_name

	sh_minio_path = path_comb+"/minio_cp.sh"
	sh_minio = ["#!/bin/bash\n", 'cmd="'+'mc cp -r '+minio_cp+ ' '+minio_path+' '+'&& '+rm_+' '+'&& exit'+'"'+'\n', "eval $cmd"]
	with open(sh_minio_path, 'w') as rsh_:
	    rsh_.writelines(sh_minio)
	subprocess.call(['chmod', '+x', sh_minio_path])
	subprocess.call(sh_minio_path)

	#break

#	with open("/Users/chalermpong/Desktop/generate_backbone/02/"+filename+i+".fasta", "w") as file:
#		file.write("%s\n" % "test")
