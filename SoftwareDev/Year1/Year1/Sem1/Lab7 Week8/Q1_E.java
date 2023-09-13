import java.util.Scanner;
public class Q1_E
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a string of numbers: ");
		int num = in.nextInt();
		int total = 0;
		//       A       B     C
		while (num > 0)
		{
			int digit = num % 10;
			if(digit % 2 == 1)
			{
				total = total + digit;
			}
			num = num / 10;
		}
		System.out.println("Total: "+total);
	}
}