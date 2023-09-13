import java.util.Scanner;

public class Wk5_5
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Should order be strict or lenient? ");
		String check = in.next();
		System.out.print("Please enter 3 numbers: ");
		int num1 = in.nextInt();
		int num2 = in.nextInt();
		int num3 = in.nextInt();

		if (check.equals("strict"))
		{
			if (num1 < num2 && num2 < num3)
			{
				System.out.println("increasing");
			}
			else if (num1 > num2 && num2 > num3)
			{
				System.out.println("decreasing");
			}
			else
			{
				System.out.println("neither");
			}
		};


		if (check.equals("lenient"))
		{
			if (num1 < num2 && num2 < num3 || num1 < num2 && num2 == num3)
			{
				System.out.println("increasing");
			}
			else if (num1 > num2 && num2 > num3 || num1 == num2 && num2 > num3)
			{
				System.out.println("decreasing");
			}
			else
			{
				System.out.println("both increasing and decreasing");
			}
		}
	}
}
