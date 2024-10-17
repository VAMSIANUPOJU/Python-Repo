import java.util.Scanner;
public class Main{
    public static void main(String [] args){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        System.out.println(n/365);
        int p=(n%365)/7;
        System.out.println(p);
    }
}