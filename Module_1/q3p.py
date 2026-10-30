def check(text):
    stack=[]
    max_depth=0
    depth=0
    pairs={")":"(", "}":"{" ,"]":"["}
    
    for i ,ch in enumerate(text):
        if ch in "{([":
            stack.append((ch,i+1))
            depth+=1
            max_depth=max(max_depth,depth)

        elif ch in "})]":
            if not stack or stack[-1][0] !=pairs[ch]:
                print("Invalided position",i+1)
                return
            stack.pop()
            depth-=1

    if stack:
        print("Invalid position",stack[0][1])
    else:
         print("Valid, max depth", max_depth)
               
text=input()
check(text)