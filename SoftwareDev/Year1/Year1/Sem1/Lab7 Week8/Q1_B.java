public class Q1_B
{
	public static void main (String[] args)
	{
		int total = 0;
		//       A       B     C
		for(int x = 1; x <= 100; x++)
		{
			total = total + x*x;
		}
		System.out.println("Total: "+total);
	}
}