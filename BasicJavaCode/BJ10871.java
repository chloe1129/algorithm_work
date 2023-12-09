import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int x = sc.nextInt();
        int t;

        ArrayList<Integer> a = new ArrayList<Integer>();

        for(int i=0; i < n; i++){
            t = sc.nextInt();
            if(t<x){
                a.add(t);
            }
        }
        sc.close();
        for(int i=0;i<a.size();i++){
            System.out.print(a.get(i) + " ");
        }
    }
}