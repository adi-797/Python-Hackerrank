def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
 
    word_list = wrapper.wrap(text=string)
    temp = ""
    for element in word_list:
        temp = temp + str(element) + "\n"
    return temp
        
