import java.util.Scanner;
public class Q2_A
{
	public static void main (String[] args)
	{
		// Loop through the inputs
		// Check to see if which is the smallest and which is the largest
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a sequence of integers, q to quit: ");
		int value = in.nextInt();
		int max = value;
		int min = value;

		while (in.hasNextInt())
		{
		    value = in.nextInt();
		    if (value > max)
		    {
		        max = value;
		    }
		    if (value < min)
		    {
		        min = value;
		    }
		}
		System.out.println("Smallest: "+min+", "+"Largest: "+max);
	}
}