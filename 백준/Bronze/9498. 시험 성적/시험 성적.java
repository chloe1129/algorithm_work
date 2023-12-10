import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

// 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int score = Integer.parseInt(bf.readLine());

        if (score>= 90) bw.write('A');
        else if (score >= 80) bw.write('B');
        else if (score >= 70) bw.write('C');
        else if (score >= 60) bw.write('D');
        else bw.write('F');

        bw.flush();

        // 스트림 닫기
        bw.close();
    }
}