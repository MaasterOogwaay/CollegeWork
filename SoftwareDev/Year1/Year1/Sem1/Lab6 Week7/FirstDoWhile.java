public class FirstDoWhile
{
	public static void main (String[] args)
	{
		int x = 1; // A
		do // repeated code
		{
			System.out.print(x+", ");
			x++; // C
		}while (x <= 5); // B
		System.out.println();
	}
}