def count_substring(string, sub_string):
    i=0
    count = 0
    while i<(len(string)-len(sub_string)+1):
        temp = ""
        before = i
        for j in range(len(sub_string)):
            temp = temp+string[i]
            i = i+1;
        if (temp == sub_string):
            count +=1;
        i = before
        i = i+1;
    return count
