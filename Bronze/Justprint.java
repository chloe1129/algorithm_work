package Bronze;

import java.util.Scanner;

class Justprint{
    public static void main(String[] args) {
        
    Scanner in = new Scanner(System.in);
    
    while(in.hasNextLine()){
        String str = in.nextLine();
        System.out.println(str);
    }
    in.close();
    }
}