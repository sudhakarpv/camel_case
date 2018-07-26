# camel_case
def main():
    pass
    inp=input().split()
    final=[]
    str1=inp[0]
    str2=inp[1]
    conv=str1.title()
    conv1=str2.title()
    final.append(conv)
    final.append(conv1)
    print(' '.join(final))
if __name__ == '__main__':
    main()
