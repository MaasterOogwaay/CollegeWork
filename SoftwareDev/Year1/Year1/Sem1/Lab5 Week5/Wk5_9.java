import java.util.Scanner;

public class Wk5_9
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter 3 words: ");
		String word1 = in.next();
		String word2 = in.next();
		String word3 = in.next();

		if (word1.compareTo(word2) < 0 && word2.compareTo(word3) < 0)
		{
			System.out.println(word1);
			System.out.println(word2);
			System.out.println(word3);
		}
		else if (word1.compareTo(word2) > 0 && word2.compareTo(word3) > 0)
		{
			System.out.println(word3);
			System.out.println(word2);
			System.out.println(word1);
		}
		else if (word1.compareTo(word3) > 0 && word3.compareTo(word2) > 0)
		{
			System.out.println(word2);
			System.out.println(word3);
			System.out.println(word1);
		}
		else if (word1.compareTo(word2) > 0 && word2.compareTo(word3) < 0)
		{
			System.out.println(word2);
			System.out.println(word3);
			System.out.println(word1);
		}
	}
}