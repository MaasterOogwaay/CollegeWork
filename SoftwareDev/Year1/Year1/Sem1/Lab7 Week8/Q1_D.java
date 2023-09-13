import java.util.Scanner;
public class Q1_D
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter two numbers: ");
		int num1 = in.nextInt();
		int num2 = in.nextInt();

		int low = Math.min(num1, num2);
		int high = Math.max(num1, num2);
		int total = 0;
		//       A       B     C
		for(int x = low; x <= high; x++)
		{
			if(x%2 != 0)
			{
				total = total + x;
			}
		}
		System.out.println("Total: "+total);
	}
}