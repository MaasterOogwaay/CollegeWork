import java.util.Scanner;

public class Wk5_6
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter 3 numbers: ");
		int num1 = in.nextInt();
		int num2 = in.nextInt();
		int num3 = in.nextInt();

		if (num1 < num2 && num2 < num3 || num1 > num2 && num2 > num3 || num1 < num2 && num2 == num3)
		{
			System.out.println(num1+" "+ num2+" "+ num3+" is in order");
		}
		else
		{
			System.out.println(num1+" "+ num2+" "+ num3+" is not in order");
		}
	}
}