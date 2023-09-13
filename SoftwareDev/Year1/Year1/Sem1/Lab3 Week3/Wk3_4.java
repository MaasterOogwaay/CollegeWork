import java.util.Scanner;
public class Wk3_4
{
	public static void main(String[] args)
	{
		// compound assignment operator  a op=b => a = a op b  where op is + - / * or %

		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a positive integer no longer than five digits:");

		int number = in.nextInt(); //12345

		int digit5 = number % 10; // 12345%10 = 5
		number /= 10; // number = number / 10    12345/10 = 1234

		int digit4 = number % 10; // 1234 % 10 = 4
		number /= 10; // 1234/10 = 123

		int digit3 = number % 10; // 123% 10 = 3
		number /= 10; // 123/10 = 12

		int digit2 = number % 10; //12%10 = 2
		number /= 10; // 12/10 = 1

		int digit1 = number % 10; // 1%10 = 1


		System.out.printf("%d %d %d %d %d\n", digit1, digit2, digit3, digit4, digit5);
	}
}
