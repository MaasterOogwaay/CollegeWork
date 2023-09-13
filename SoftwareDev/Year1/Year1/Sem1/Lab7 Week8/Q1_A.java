public class Q1_A
{
	public static void main (String[] args)
	{
		int total = 0;
		//       A       B     C
		for(int x = 2; x <= 100; x = x + 2)
		{
			total = total + x;
		}
		System.out.println("Total: "+total);
	}
}