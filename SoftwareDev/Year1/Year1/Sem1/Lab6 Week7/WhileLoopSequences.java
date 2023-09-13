public class WhileLoopSequences
{
	public static void main (String[] args)
	{
		// Checks if x <= 10
		// If true, prints x and increments by 1
		// Now checks if 2 <= 10
		// If true, prints x and increments by 1
		int x = 1; // A
		do // repeated code
		{
			System.out.print(x+", ");
			x++; // C
		}while (x <= 10); // B
		System.out.println();

		// Checks if y <= 20
		// If true, prints y and increases the number by 2
		int y = 2; // A
		do // repeated code
		{
			System.out.print(y+", ");
			y = y + 2; // C
		}while (y <= 20); // B
		System.out.println();

		// Checks if z >= -15 && z <= 15
		// If true, print z and increase the number by 3
		int z = -15; // A
		do // repeated code
		{
			System.out.print(z+", ");
			z = z + 3; // C
		}while (z >= -15 && z <= 15); // B
		System.out.println();

		// Checks if a >= 0
		// If true, prints a and decrements number by 1
		int a = 10; // A
		do // repeated code
		{
			System.out.print(a+", ");
			a--; // C
		}while (a >= 0); // B
		System.out.println();

		// Checks if b >= -50
		// If true, prints b and decreases number by 10
		int b = 50; // A
		do // repeated code
		{
			System.out.print(b+", ");
			b = b -10; // C
		}while (b >= -50); // B
		System.out.println();

		// Checks if c <= 10
		//If true, square c and print it then increase c by 1
		int c = 1; // A
		do // repeated code
		{
			System.out.print((c * c)+", ");
			c++; // C
		}while (c <= 10); // B
		System.out.println();

		//
		//
		int num = 0; // A
		int preNum = num - 1;
		do // repeated code
		{
			System.out.print(num+(num + preNum)+", ");
			num++; // C
		}while (num <= 5); // B
		System.out.println();
	}
}