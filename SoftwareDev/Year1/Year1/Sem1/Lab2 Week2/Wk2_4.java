import java.util.Scanner;
public class Wk2_4
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter the first number: ");
		int num1 = in.nextInt();
		System.out.print("Please enter the second number: ");
		int num2 = in.nextInt();

		int sum = num1 + num2;
		System.out.println("The average: "+(sum/2.0));
	}
}