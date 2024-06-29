def main():
    plist = []
    
    begin = int(input("Enter the first number here:"))
    end = int(input("Enter the ending number here:"))
    
    for number in range(begin , end + 1):
        if number > 1:
            for i in range (2 , number):
                in number % 2 == 0:
                    break
    
    

    return plist


if __name__ == '__main__':
    main()
