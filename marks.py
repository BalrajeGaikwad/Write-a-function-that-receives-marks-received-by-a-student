#Write a function that receives marks received by a student in 3 subjects and returns the average and percentage of these marks. 
# Call this function from main() and print the results in main().



def calc(number):
    total_sum=0
    for i in number:
        total_sum+=i


    average=total_sum/5

    percentage=(total_sum/500)*100

    return total_sum, average,percentage



def main():
    number=[]

    for i in range(1,6):
        
        num=int(input("Enter the number "))
        number.append(num)

    total_sum,average,percentage=calc(number)
    print(total_sum)
    print(average)
    print(percentage)



if __name__=="__main__":
    main()






