#include <stdio.h>
void reading_the_vector(int a[104],int* size_of_sequence) {
    /*
    Function that reads the size of the sequence and the sequence itself
    Input: a - the sequence
           size_of_sequence - the size of the sequence
    Output: a - the sequence
            size_of_sequence - the size of the sequence
    */
    printf("Enter the size of the sequence: \n");
    scanf("%d", size_of_sequence);
    if (*size_of_sequence<=0) {
        printf("Invalid size\n");
        return;
    }
    printf("Enter the sequence: \n");
    for (int i = 0; i < *size_of_sequence; i++) {
        scanf("%d", &a[i]);
    }
}
double first_functionality(double x,int n) {
    /*
    Function that computes x^n
    Input: x - the base
           n - the exponent
    Output: x^n
    */
    if (x==0) return 0;
    double result = 1;
    while (n > 0) {
        if (n % 2 == 1) {
            result *= x;
        }
        x *= x;
        n /= 2;
    }
    return result;
}
void printSequence(int b[104],int size_of_sequence) {
    /*
    Function that prints the sequence obtained from the second functionality
    Input: b - the sequence
           size_of_sequence - the size of the sequence
    Output: b - the sequence
    */
    for (int i = 0; i < size_of_sequence; i++) {
        printf("%d ",b[i]);
    }
    printf("\n");
}
void second_functionality(int a[104], int size_of_sequence) {
    /*
    Function that computes the longest contiguous subsequence with alternating signs
    Input: a - the sequence
           size_of_sequence - the size of the sequence
    Output: b - the sequence
    */
    int old_sign=0,sign=0,current_first=0,current_last=0,current_length=1,max_length=1,max_first=0,max_last=0;
    if (a[0]<0)
        old_sign=1;
    else
        old_sign=0;
    for (int i=1;i<size_of_sequence;i++) {
        if (a[i]<0)
            sign = 1;
        else
            sign = 0;
        if (sign!=old_sign) {
            current_length++;
            current_last=i;
        }
        else {
            if (current_length>max_length) {
                max_length=current_length;
                max_first=current_first;
                max_last=current_last;
            }
            current_length=1;
            current_first=i;
            current_last=i;
        }
        old_sign=sign;
    }
    if (current_length>max_length) {
        max_length=current_length;
        max_first=current_first;
        max_last=current_last;
    }
    int b[104],k=0;
    for (int i=max_first;i<=max_last;i++) {
        b[k]=a[i];
        k++;
    }
    printSequence(b,max_length);
}
void printMenu()
{
    /*
    Function that prints the menu
    */
    printf("1. Read the vector\n");
    printf("2. Determine x^n\n");
    printf("3. Longest contiguous subsequence\n");
    printf("4. Exit\n");
}
int main()
{
    int a[104],size_of_sequence = 0;
    while(1) {
        printMenu();
        int option;
        scanf("%d", &option);
        if (option == 1) {
            reading_the_vector(a,&size_of_sequence);
        }
        else if (option == 2) {
            printf("Enter the value of x: \n");
            double x;
            scanf("%lf", &x);
            printf("Enter the value of n: \n");
            int n;
            scanf("%d", &n);
            if (n<0) {
                printf("Invalid value for n\n");
                continue;
            }
            x = first_functionality(x,n);
            printf("The value of x^n is %lf\n", x);

        }
        else if (option == 3) {
            if (size_of_sequence == 0) {
                reading_the_vector(a,&size_of_sequence);
            }
            second_functionality(a,size_of_sequence);
        }
        else if (option == 4) {
            break;
        }
        else {
            printf("Invalid option\n");
        }
    }
    return 0;
}
