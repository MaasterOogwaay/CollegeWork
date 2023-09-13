import java.util.Scanner;

public class Wk5_1
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a number: ");
		double num = in.nextDouble();

		if (num == 0)
		{
			System.out.println(num+" is zero");
		}
		else if (num > 0)
		{
			System.out.println(num+" is positive");
		}
		else
		{
			System.out.println(num+" is negative");
		}

		if (Math.abs(num) < 1)
		{
			System.out.println(num+" is a small number");
		}
		else if (Math.abs(num) > 1000000)
		{
			System.out.println(num+" is a large number");
		}
	}
}
