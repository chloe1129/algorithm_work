import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int j = 0; j < 3; j++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());

            int yoot = 0;
            for (int i = 0; i < 4; i++) {
                int temp = Integer.parseInt(st.nextToken());
                if (temp == 0) yoot += 1;
            }

            if (yoot == 1) bw.write("A");
            else if (yoot == 2) bw.write("B");
            else if (yoot == 3) bw.write("C");
            else if (yoot == 4) bw.write("D");
            else bw.write("E");

            bw.newLine();
        }
        bw.close();
    }
}