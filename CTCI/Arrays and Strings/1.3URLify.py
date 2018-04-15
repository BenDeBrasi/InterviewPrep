def URLify(string):
    st = ""
    for c in string:
        if c == ' ':
            st += "%20"
        else:
            st += c
    
    return st

def URLify1(string):
    count = 0
    for c in string:
        if c == ' ':
            count += 3
        else:
            count += 1
    
    arr = list(range(count))
    
    j = 0
    for i in range(len(string)):
        if string[i] == ' ':
            arr[j] ='%'
            arr[j+1] = '2'
            arr[j+2] = '0'
            j+=3
        else:
            arr[j] = string[i]
            j+=1
    
    return ''.join(arr)

print(URLify1("hello world"))
