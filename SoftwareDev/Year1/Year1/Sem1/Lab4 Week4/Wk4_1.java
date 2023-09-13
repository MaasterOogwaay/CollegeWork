import java.util.Scanner;
public class Wk4_1
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a number: ");
		int num1 = in.nextInt();

		if (num1 >= 0)
		{
			System.out.println(num1+" is a positive number!");
		} else {
			System.out.println(num1+" is a negative number!");
		}
	}
}