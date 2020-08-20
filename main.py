from lib_live import *


def main():
	gen_set = get_kill(ex7,True)
	fp_set = fp_iteration(gen_set,True)


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

ex3 = [
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

ex4 = [
	"1: x := CALL f(x,y+5)",
	"2: M[x+8] := y+5+x",
	"3: a := M[x+5]"
]

ex5 = [
	"1: LABEL start",
	"2: IF a < b THEN next ELSE swap",
	"3: LABEL swap",
	"4: t := a",
	"5: a := b",
	"6: b := t",
	"7: LABEL next",
	"8: z := 0",
	"9: b := b % a",
	"10: IF b = z THEN end ELSE start",
	"11: LABEL end",
	"12: RETURN a"
]

ex6 = [
	"1: z := 0",
	"2: LABEL begin",
	"3: a := x + 7",
	"4: y := y + a",
	"5: b := y % 3",
	"6: x := x - b",
	"7: c := x + b",
	"8: z := z - c",
	"9: IF y < x THEN end ELSE begin",
	"10: LABEL end",
	"11: RETURN z"
]

ex7 = ["1: LABEL test",
"2: IF a = 0 THEN exit ELSE body",
"3: LABEL body",
"4: x := a - b",
"5: b := x / b",
"6: y := a - 5",
"7: a := y + a",
"8: GOTO test",
"9: LABEL exit",
"10: RETURN b"]


if __name__ == '__main__':
	main()