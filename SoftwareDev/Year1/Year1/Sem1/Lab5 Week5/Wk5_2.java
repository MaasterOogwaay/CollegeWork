import java.util.Scanner;

public class Wk5_2
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a number: ");
		int num = in.nextInt();

		if (num < 0)
		{
			num = num * -1;

		}
		if (num < 10)
		{
			System.out.println(num+" has 1 digits");
		}
		else if (num < 100)
		{
			System.out.println(num+" has 2 digits");
		}
		else if (num < 1000)
		{
			System.out.println(num+" has 3 digits");
		}
		else if (num < 10000)
		{
			System.out.println(num+" has 4 digits");
		}
		else if (num < 100000)
		{
			System.out.println(num+" has 5 digits");
		}
		else if (num < 1000000)
		{
			System.out.println(num+" has 6 digits");
		}
		else if (num < 10000000)
		{
			System.out.println(num+" has 7 digits");
		}
		else if (num < 100000000)
		{
			System.out.println(num+" has 8 digits");
		}
		else if (num < 1000000000)
		{
			System.out.println(num+" has 9 digits");
		}
		else
		{
			System.out.println(num+" has 10 digits");
		}
	}
}