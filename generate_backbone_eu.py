#!/urs/local/bin/python

import os
import os.path
import subprocess

from itertools import combinations

path = os.path.expanduser("~/generate_backbone")

# Get all combination of [1, 2, 3]
# of length 3
picking = 1
comb = combinations(['ch', 'sk', 'th', 'al', 'bu', 'cr', 'de', 'ge', 'hu', 'it', 'po', 'ro', 'sr', 'sl', 'sn', 'sp', 'uk', 'us'], picking)

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
	country_13 = (i[24:26])
	country_14 = (i[26:28])
	country_15 = (i[28:30])
	country_16 = (i[30:32])
	country_17 = (i[32:34])
	country_18 = (i[34:36])

	if country_1 == "ch":
		fasta_1 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "sk":
		fasta_1 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "th":
		fasta_1 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "al":
		fasta_1 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "bu":
		fasta_1 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "cr":
		fasta_1 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "de":
		fasta_1 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "ge":
		fasta_1 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "hu":
		fasta_1 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "it":
		fasta_1 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "po":
		fasta_1 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "ro":
		fasta_1 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "sr":
		fasta_1 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "sl":
		fasta_1 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "sn":
		fasta_1 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "sp":
		fasta_1 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "uk":
		fasta_1 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"
	elif country_1 == "us":
		fasta_1 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_1+".fasta"
		cp_1 = "cp "+fasta_1+" "+path+"/merge"

	if country_2 == "ch":
		fasta_2 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "sk":
		fasta_2 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "th":
		fasta_2 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "al":
		fasta_2 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "bu":
		fasta_2 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "cr":
		fasta_2 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "de":
		fasta_2 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "ge":
		fasta_2 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "hu":
		fasta_2 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "it":
		fasta_2 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "po":
		fasta_2 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "ro":
		fasta_2 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "sr":
		fasta_2 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "sl":
		fasta_2 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "sn":
		fasta_2 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "sp":
		fasta_2 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "uk":
		fasta_2 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"
	elif country_2 == "us":
		fasta_2 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_2+".fasta"
		cp_2 = "cp "+fasta_2+" "+path+"/merge"

	if country_3 == "ch":
		fasta_3 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "sk":
		fasta_3 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "th":
		fasta_3 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "al":
		fasta_3 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "bu":
		fasta_3 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "cr":
		fasta_3 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "de":
		fasta_3 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "ge":
		fasta_3 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "hu":
		fasta_3 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "it":
		fasta_3 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "po":
		fasta_3 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "ro":
		fasta_3 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "sr":
		fasta_3 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "sl":
		fasta_3 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "sn":
		fasta_3 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "sp":
		fasta_3 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "uk":
		fasta_3 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"
	elif country_3 == "us":
		fasta_3 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_3+".fasta"
		cp_3 = "cp "+fasta_3+" "+path+"/merge"

	if country_4 == "ch":
		fasta_4 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "sk":
		fasta_4 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "th":
		fasta_4 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "al":
		fasta_4 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "bu":
		fasta_4 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "cr":
		fasta_4 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "de":
		fasta_4 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "ge":
		fasta_4 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "hu":
		fasta_4 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "it":
		fasta_4 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "po":
		fasta_4 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "ro":
		fasta_4 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "sr":
		fasta_4 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "sl":
		fasta_4 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "sn":
		fasta_4 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "sp":
		fasta_4 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "uk":
		fasta_4 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"
	elif country_4 == "us":
		fasta_4 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_4+".fasta"
		cp_4 = "cp "+fasta_4+" "+path+"/merge"

	if country_5 == "ch":
		fasta_5 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "sk":
		fasta_5 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "th":
		fasta_5 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "al":
		fasta_5 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "bu":
		fasta_5 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "cr":
		fasta_5 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "de":
		fasta_5 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "ge":
		fasta_5 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "hu":
		fasta_5 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "it":
		fasta_5 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "po":
		fasta_5 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "ro":
		fasta_5 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "sr":
		fasta_5 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "sl":
		fasta_5 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "sn":
		fasta_5 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "sp":
		fasta_5 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "uk":
		fasta_5 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"
	elif country_5 == "us":
		fasta_5 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_5+".fasta"
		cp_5 = "cp "+fasta_5+" "+path+"/merge"

	if country_6 == "ch":
		fasta_6 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "sk":
		fasta_6 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "th":
		fasta_6 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "al":
		fasta_6 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "bu":
		fasta_6 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "cr":
		fasta_6 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "de":
		fasta_6 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "ge":
		fasta_6 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "hu":
		fasta_6 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "it":
		fasta_6 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "po":
		fasta_6 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "ro":
		fasta_6 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "sr":
		fasta_6 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "sl":
		fasta_6 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "sn":
		fasta_6 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "sp":
		fasta_6 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "uk":
		fasta_6 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"
	elif country_6 == "us":
		fasta_6 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_6+".fasta"
		cp_6 = "cp "+fasta_6+" "+path+"/merge"

	if country_7 == "ch":
		fasta_7 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "sk":
		fasta_7 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "th":
		fasta_7 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "al":
		fasta_7 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "bu":
		fasta_7 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "cr":
		fasta_7 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "de":
		fasta_7 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "ge":
		fasta_7 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "hu":
		fasta_7 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "it":
		fasta_7 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "po":
		fasta_7 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "ro":
		fasta_7 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "sr":
		fasta_7 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "sl":
		fasta_7 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "sn":
		fasta_7 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "sp":
		fasta_7 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "uk":
		fasta_7 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"
	elif country_7 == "us":
		fasta_7 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_7+".fasta"
		cp_7 = "cp "+fasta_7+" "+path+"/merge"

	if country_8 == "ch":
		fasta_8 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "sk":
		fasta_8 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "th":
		fasta_8 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "al":
		fasta_8 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "bu":
		fasta_8 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "cr":
		fasta_8 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "de":
		fasta_8 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "ge":
		fasta_8 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "hu":
		fasta_8 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "it":
		fasta_8 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "po":
		fasta_8 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "ro":
		fasta_8 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "sr":
		fasta_8 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "sl":
		fasta_8 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "sn":
		fasta_8 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "sp":
		fasta_8 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "uk":
		fasta_8 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"
	elif country_8 == "us":
		fasta_8 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_8+".fasta"
		cp_8 = "cp "+fasta_8+" "+path+"/merge"

	if country_9 == "ch":
		fasta_9 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "sk":
		fasta_9 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "th":
		fasta_9 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "al":
		fasta_9 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "bu":
		fasta_9 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "cr":
		fasta_9 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "de":
		fasta_9 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "ge":
		fasta_9 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "hu":
		fasta_9 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "it":
		fasta_9 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "po":
		fasta_9 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "ro":
		fasta_9 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "sr":
		fasta_9 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "sl":
		fasta_9 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "sn":
		fasta_9 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "sp":
		fasta_9 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "uk":
		fasta_9 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"
	elif country_9 == "us":
		fasta_9 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_9+".fasta"
		cp_9 = "cp "+fasta_9+" "+path+"/merge"

	if country_10 == "ch":
		fasta_10 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "sk":
		fasta_10 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "th":
		fasta_10 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "al":
		fasta_10 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "bu":
		fasta_10 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "cr":
		fasta_10 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "de":
		fasta_10 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "ge":
		fasta_10 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "hu":
		fasta_10 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "it":
		fasta_10 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "po":
		fasta_10 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "ro":
		fasta_10 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "sr":
		fasta_10 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "sl":
		fasta_10 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "sn":
		fasta_10 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "sp":
		fasta_10 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "uk":
		fasta_10 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"
	elif country_10 == "us":
		fasta_10 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_10+".fasta"
		cp_10 = "cp "+fasta_10+" "+path+"/merge"

	if country_11 == "ch":
		fasta_11 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "sk":
		fasta_11 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "th":
		fasta_11 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "al":
		fasta_11 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "bu":
		fasta_11 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "cr":
		fasta_11 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "de":
		fasta_11 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "ge":
		fasta_11 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "hu":
		fasta_11 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "it":
		fasta_11 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "po":
		fasta_11 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "ro":
		fasta_11 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "sr":
		fasta_11 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "sl":
		fasta_11 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "sn":
		fasta_11 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "sp":
		fasta_11 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "uk":
		fasta_11 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"
	elif country_11 == "us":
		fasta_11 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_11+".fasta"
		cp_11 = "cp "+fasta_11+" "+path+"/merge"

	if country_12 == "ch":
		fasta_12 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "sk":
		fasta_12 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "th":
		fasta_12 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "al":
		fasta_12 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "bu":
		fasta_12 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "cr":
		fasta_12 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "de":
		fasta_12 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "ge":
		fasta_12 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "hu":
		fasta_12 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "it":
		fasta_12 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "po":
		fasta_12 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "ro":
		fasta_12 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "sr":
		fasta_12 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "sl":
		fasta_12 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "sn":
		fasta_12 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "sp":
		fasta_12 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "uk":
		fasta_12 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"
	elif country_12 == "us":
		fasta_12 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_12+".fasta"
		cp_12 = "cp "+fasta_12+" "+path+"/merge"

	if country_13 == "ch":
		fasta_13 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "sk":
		fasta_13 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "th":
		fasta_13 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "al":
		fasta_13 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "bu":
		fasta_13 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "cr":
		fasta_13 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "de":
		fasta_13 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "ge":
		fasta_13 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "hu":
		fasta_13 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "it":
		fasta_13 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "po":
		fasta_13 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "ro":
		fasta_13 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "sr":
		fasta_13 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "sl":
		fasta_13 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "sn":
		fasta_13 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "sp":
		fasta_13 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "uk":
		fasta_13 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"
	elif country_13 == "us":
		fasta_13 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_13+".fasta"
		cp_13 = "cp "+fasta_13+" "+path+"/merge"

	if country_14 == "ch":
		fasta_14 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "sk":
		fasta_14 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "th":
		fasta_14 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "al":
		fasta_14 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "bu":
		fasta_14 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "cr":
		fasta_14 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "de":
		fasta_14 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "ge":
		fasta_14 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "hu":
		fasta_14 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "it":
		fasta_14 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "po":
		fasta_14 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "ro":
		fasta_14 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "sr":
		fasta_14 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "sl":
		fasta_14 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "sn":
		fasta_14 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "sp":
		fasta_14 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "uk":
		fasta_14 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"
	elif country_14 == "us":
		fasta_14 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_14+".fasta"
		cp_14 = "cp "+fasta_14+" "+path+"/merge"

	if country_15 == "ch":
		fasta_15 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "sk":
		fasta_15 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "th":
		fasta_15 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "al":
		fasta_15 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "bu":
		fasta_15 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "cr":
		fasta_15 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "de":
		fasta_15 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "ge":
		fasta_15 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "hu":
		fasta_15 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "it":
		fasta_15 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "po":
		fasta_15 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "ro":
		fasta_15 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "sr":
		fasta_15 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "sl":
		fasta_15 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "sn":
		fasta_15 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "sp":
		fasta_15 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "uk":
		fasta_15 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"
	elif country_15 == "us":
		fasta_15 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_15+".fasta"
		cp_15 = "cp "+fasta_15+" "+path+"/merge"

	if country_16 == "ch":
		fasta_16 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "sk":
		fasta_16 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "th":
		fasta_16 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "al":
		fasta_16 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "bu":
		fasta_16 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "cr":
		fasta_16 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "de":
		fasta_16 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "ge":
		fasta_16 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "hu":
		fasta_16 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "it":
		fasta_16 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "po":
		fasta_16 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "ro":
		fasta_16 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "sr":
		fasta_16 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "sl":
		fasta_16 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "sn":
		fasta_16 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "sp":
		fasta_16 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "uk":
		fasta_16 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"
	elif country_16 == "us":
		fasta_16 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_16+".fasta"
		cp_16 = "cp "+fasta_16+" "+path+"/merge"

	if country_17 == "ch":
		fasta_17 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "sk":
		fasta_17 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "th":
		fasta_17 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "al":
		fasta_17 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "bu":
		fasta_17 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "cr":
		fasta_17 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "de":
		fasta_17 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "ge":
		fasta_17 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "hu":
		fasta_17 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "it":
		fasta_17 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "po":
		fasta_17 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "ro":
		fasta_17 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "sr":
		fasta_17 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "sl":
		fasta_17 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "sn":
		fasta_17 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "sp":
		fasta_17 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "uk":
		fasta_17 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"
	elif country_17 == "us":
		fasta_17 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_17+".fasta"
		cp_17 = "cp "+fasta_17+" "+path+"/merge"

	if country_18 == "ch":
		fasta_18 = path+"/FASTA/EU/01_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "sk":
		fasta_18 = path+"/FASTA/EU/02_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "th":
		fasta_18 = path+"/FASTA/EU/03_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "al":
		fasta_18 = path+"/FASTA/EU/04_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "bu":
		fasta_18 = path+"/FASTA/EU/05_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "cr":
		fasta_18 = path+"/FASTA/EU/06_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "de":
		fasta_18 = path+"/FASTA/EU/07_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "ge":
		fasta_18 = path+"/FASTA/EU/08_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "hu":
		fasta_18 = path+"/FASTA/EU/09_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "it":
		fasta_18 = path+"/FASTA/EU/10_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "po":
		fasta_18 = path+"/FASTA/EU/11_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "ro":
		fasta_18 = path+"/FASTA/EU/12_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "sr":
		fasta_18 = path+"/FASTA/EU/13_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "sl":
		fasta_18 = path+"/FASTA/EU/14_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "sn":
		fasta_18 = path+"/FASTA/EU/15_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "sp":
		fasta_18 = path+"/FASTA/EU/16_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "uk":
		fasta_18 = path+"/FASTA/EU/17_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"
	elif country_18 == "us":
		fasta_18 = path+"/FASTA/EU/18_prrsv_filters_eu_"+country_18+".fasta"
		cp_18 = "cp "+fasta_18+" "+path+"/merge"

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
	elif picking == 13:
		dir_comb = "comb_13"
	elif picking == 14:
		dir_comb = "comb_14"
	elif picking == 15:
		dir_comb = "comb_15"
	elif picking == 16:
		dir_comb = "comb_16"
	elif picking == 17:
		dir_comb = "comb_17"
	elif picking == 18:
		dir_comb = "comb_18"

	merge_name = "prrsv_filters_eu_"+i
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
	elif picking == 13:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+cp_12+' && '+cp_13+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 14:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+cp_12+' && '+cp_13+' && '+cp_14+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 15:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+cp_12+' && '+cp_13+' && '+cp_14+' && '+cp_15+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 16:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+cp_12+' && '+cp_13+' && '+cp_14+' && '+cp_15+' && '+cp_16+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 17:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+cp_12+' && '+cp_13+' && '+cp_14+' && '+cp_15+' && '+cp_16+' && '+cp_17+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]
	elif picking == 18:
		merge_sh = ["#!/bin/bash\n", 'cmd="'+cp_1+' && '+cp_2+' && '+cp_3+' && '+cp_4+' && '+cp_5+' && '+cp_6+' && '+cp_7+' && '+cp_8+' && '+cp_9+' && '+cp_10+' && '+cp_11+' && '+cp_12+' && '+cp_13+' && '+cp_14+' && '+cp_15+' && '+cp_16+' && '+cp_17+' && '+cp_18+' && '+merge_fasta+' && '+cp_fasta_merge+' && '+rm+' && exit'+'"'+'\n', "eval $cmd"]

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
	minio_path = "minio/prrsv/generate_backbone_rerun/eu/"+dir_comb+"/"
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
