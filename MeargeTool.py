def merge_the_tools(string, k):
    # your code goes here
    # lst = [str(set(string[i:i + k])) for i in range(0, len(string), k)]
    for i in range(0,len(string),k):
        print("".join(dict.fromkeys(string[i:i+k])))




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
