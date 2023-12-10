import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

// A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성
public class Main {
    public static void main(String[] args) throws IOException {
        // 입력
        // BufferedReader 선언하기
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        // Read 데이터는 Line 단위로만 나워져 공백 단위로 데이터 가공 시 따로 처리 필요
        // String s = bf.readLine();

        // StringTokenizer 사용, nextToken을 사용해 입력받은 값을 공백 단위로 구분해 호출
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        // String.split 함수 사용, 배열에 공백 단위로 끊어서 데이터 저장
        // String array[] = s.split(" ");

        // System.out.println(a+b);

        // 출력
        // BufferedWriter 선언하기
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 출력
        bw.write((a+b) + "\n");
        bw.write((a-b) + "\n");
        bw.write((a*b) + "\n");
        bw.write((a/b) + "\n");
        bw.write((a%b) + "\n");

        // 줄바꿈
        // bw.newLine();

        bw.flush();

        // 스트림 닫기
        bw.close();
    }
}