import java.util.Scanner;
public class Wk2_6
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter the first number: ");
		int num1 = in.nextInt();
		System.out.print("Please enter the second number: ");
		int num2 = in.nextInt();

		System.out.println("The maximum: "+Math.max(num1, num2));
	}
}