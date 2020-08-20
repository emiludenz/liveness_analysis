def find_label(str, lab):
	m = "LABEL " + lab
	for s in str:
		if "LABEL" in s:
			if lab in s:
				return s[:s.find(": ")]
		else:
			continue
def replace_relop(str):
	return str.replace("+",",").replace("-",",").replace("*",",").replace("/",",").replace("%",",").replace(" ","").replace("<",",").replace("=",",").replace(">",",")
def replace_nums(str):
	tmp = str.replace("0","å").replace("1","å").replace("2","å").replace("3","å").replace("4","å").replace("5","å").replace("6","å").replace("7","å").replace("8","å").replace("9","")
	tmp = tmp.replace(",å","").replace("å","").replace(" ","")
	return tmp

def get_kill(str, output=True):
	l = [["stmt","Succ","Gen","Kill"]]
	for s in str:
		# 0=statement num,1=succ,2=gen,3=kill,
		row = ["","","",""]
		if ": " in s:
			# statement number
			row[0] =  s[:s.find(": ")]
			# Succ
			if len(str)+1 != int(row[0])+1:
				row[1] = int(row[0])+1
			
		if "IF" in s:
			#Gen
			row[2] = replace_nums(replace_relop(s[s.find("IF")+3:s.find("THEN")]))
			#succ
			t_lab = s[s.find("THEN")+5:s.find("ELSE")].replace(" ","")
			f_lab = s[s.find("ELSE")+5:].replace(" ","")
			row[1] = find_label(str,t_lab) + "," + find_label(str,f_lab)
			
		if "GOTO" in s:
			lab = s[s.find("GOTO")+5:]
			row[1] = find_label(str,lab)

		if "RETURN" in s:
			row[2] = s[s.find("RETURN")+7:]

		if ":=" in s:
			if "M[" in s:
				if s.find("]") < s.find(":="):
				# left side
					right = replace_relop(s[s.find(":=")+2:])
					left = s[:s.find(":=")]
					left = replace_relop(replace_nums(left[left.find("[")+1:left.find("]")]))
					right = replace_relop(replace_nums(right))
					tmp = right
					# Kill
					if len(left) == 2:
						left = left[0]
					row[3] = left
					
				else:
					# right side
					#gen
					tmp = replace_relop(s[s.find(":=")+2:])
					tmp = replace_nums(tmp[tmp.find("[")+1:tmp.find("]")])
					#tmp = s[:s.find(":=")]
					
					# Kill
					row[3] = s[s.find(": ")+1:s.find(":=")].replace(" ","")
			
			elif "CALL" in s:
				fun = s[s.find("CALL")+5:]
				tmp = replace_relop(fun[fun.find("(")+1:fun.find(")")])
				# Kill
				row[3] = s[s.find(": ")+1:s.find(":=")].replace(" ","")
				
			else:	
				# Gen 
				tmp = replace_relop(s[s.find(":=")+2:])
				# Kill
				row[3] = s[s.find(": ")+1:s.find(":=")].replace(" ","")
			#Gen
			tmp = replace_nums(tmp)
			row[2] = tmp.replace(" ","")
			
			# Kill
			#row[3] = s[s.find(": ")+1:s.find(":=")].replace(" ","")
		l = l + [row]
		#l.append(string)
	if output:
		for i in l:
			print(f"|{i[0]}\t|{i[1]}\t|{i[2]}\t|{i[3]}\t|")
	return l		


def remove_from_set(set1,set2):
	set2 = set2.split(",")
	if type(set1) != type([]):
		set1 = set1.split(",")
	ret = []
	for s in set1:
		if s not in set2 and s != '':
			ret.append(s)
	return ret


def join_set(set1,set2):
	ret = []
	if type(set1) != type([]):
		#set1 = [set1]
		set1 = set1.split(",")
	if type(set2) != type([]):
		set2 = set2.split(",")
		#set2 = [set2]
	for s in set1 + set2:
		if s not in ret and s != '':
			ret.append(s)
	return ret

def clean_set(set1):
	ret = []
	for s in set1:
		if s != '' and s not in ret:
			ret.append(s)
	return ret

def print_in_out(list1,list2,iter):
	width = 12

	print(f"Iteration {iter}")
	print(f"Stmt num| out[i] | in[i]    |")
	for i in range(len(list1)):
		out = ",".join(list1[i])
		out = out.replace(" ","")
		o = out.ljust((width-len(out))," ")
		            
		#print(o.replace(" ","ø"))
		_in = ",".join(list2[i]).replace(" ","")
		_i = _in.ljust((width-len(_in))," ")
		print(f"{i+1}\t| {o} | {_i} |")
		#print(len(out))
 		

def fp_iteration(gen_kill_set, output):
	m = gen_kill_set[1:]
	res = [["out[i]","in[i]"]]
	ret = []
	out_set = ["" for i in range(len(m))]
	in_set = ["" for i in range(len(m))]
	iteration = 0
	same = False
	if output:
		print_in_out(out_set,in_set,iteration)
	while not same:
		iteration += 1
		prev_out = out_set.copy()
		prev_in = in_set.copy()
		ret.append([prev_out,prev_in])
		out_set = ["" for i in range(len(m))]
		in_set = ["" for i in range(len(m))]
		
		for i in range(len(m)-1,-1,-1):
			
			succ = m[i][1]
			#out calc	
			
			succ = str(succ).split(",")
			succ_set = []
			for s in succ:
				if s != '':
					s = int(s)
					if s <= len(m)+1:
						# s - 1 to convert between the zero index array and the original numbering
						succ_set = join_set(succ_set, in_set[s-1])
						succ_set = join_set(succ_set, prev_in[s-1])

			# out set
			out_set[i] = succ_set
			gen = m[i][2]
			kill = m[i][3]

			# in set
			_set = remove_from_set(out_set[i],kill)
			in_set[i] = join_set(gen,_set)
		
		
		for i in range(0,len(m)):	
			if out_set[i] == prev_out[i] and in_set[i] == prev_in[i]:
				same = True
			else:
				same = False
				break
		if output:
			print_in_out(out_set,in_set,iteration)
		
	return ret


def get_interference_table(kill_set, fp_iter):
	pass