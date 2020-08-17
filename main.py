from lib_live import *


def main():
	ex = ["0: LABEL begin",
		"1: z := a+b",
		"2: a := z+b",
		"3: IF y < x THEN end ELSE begin",
		"4: LABEL end"]
	
	ex2 = ["1: z := 0",
		"2: LABEL begin",
		"3: a := x + 7",
		"4: y := y + a",
		"5: b := y % 3",
		"6: x := x - b",
		"7: c := x + b",
		"8: z := z - c",
		"9: IF y < x THEN end ELSE begin",
		"10: LABEL end",
		"11: RETURN z",
		"12: GOTO end"]
	
	ex3 =[
		"1: a := 0",
		"2: b := 1",
		"3: z := 0",
		"4: LABEL loop",
		"5: IF n = z THEN end ELSE body",
		"6: LABEL body",
		"7: t := a + b",
		"8: a := b",
		"9: b := t",
		"10: n := n - 1",
		"11: z := 0",
		"12: GOTO loop",
		"13: LABEL end",
		"14: RETURN a"]

	ex4 =[
		"1: x := CALL f(x,y+5)",
		"2: M[x+8] := y+5+x",
		"3: a := M[x+5]"
	]
	gen_set = get_kill(ex3,False)
	fp_iteration(gen_set,True)


if __name__ == '__main__':
	main()