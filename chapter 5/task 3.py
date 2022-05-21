txt="*"
A="{0:_{1}{2}}"
num=8
for i in range(1,num+1):
    if i==(num/2+1):
        print(A.format(txt, ">", num - i + 1), end="")
        print((txt * (2 * (i - 1))), end="")
        print(A.format(txt, "<", num - i))
    else:
        print(A.format(txt,">",num-i+1), end="")
        print((" "*(2*(i-1))), end="")
        print(A.format(txt,"<",num-i))

