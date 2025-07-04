import  java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int mynumber = (int)(Math.random()*100);
        int Guessnumber = 0;
        do {
            System.out.println("Guess the number : ");
            Guessnumber = sc.nextInt();
            if (Guessnumber==mynumber){
                System.out.println("woohoo correct number");
                break;
            } else if (Guessnumber>mynumber) {
                System.out.println("your Number is Big");
            } else if (Guessnumber<mynumber) {
                System.out.println("your number is small");
            }
        } while (Guessnumber>=0);
        System.out.println("My number was : ");
        System.out.println(mynumber);
    }
}