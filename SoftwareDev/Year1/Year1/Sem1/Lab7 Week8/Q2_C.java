import java.util.Scanner;
public class Q2_C
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a sequence of integers, q to quit: ");
		int value;
		int sum = 0;
		while(in.hasNextInt())
		{
			value = in.nextInt();
			sum = sum + value;
			System.out.println("Total: "+sum);
		}
	}
}