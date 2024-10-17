import java.util.Scanner;
public class Main{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        if(5*x>=y)
        System.out.print("YES");
        else
        System.out.print("NO");
    }
}