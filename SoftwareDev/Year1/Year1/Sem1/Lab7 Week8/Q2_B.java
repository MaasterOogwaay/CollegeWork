import java.util.Scanner;
public class Q2_B
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a sequence of integers, q to quit: ");
		int value = in.nextInt();
		int odd = 0;
		int even = 0;

		while (in.hasNextInt())
		{
		    value = in.nextInt();
		    if (value % 2 == 0)
		    {
		        even++;
		    }
		    else
		    {
		        odd++;
		    }
		}
		System.out.println("Even: "+even+", "+"Odd: "+odd);
	}
}