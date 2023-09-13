import java.util.Scanner;
public class Wk4_3
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a number: ");
		int num1 = in.nextInt();

		if (num1 % 2 == 0) {
			System.out.println(num1+" is an even number!");
		} else {
			System.out.println(num1+" is an odd number!");
		}
	}
}