import java.util.Scanner;
public class MultipleInputsStrings
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter 3 words (seperate by spaces, then press enter): ");
		String word1 = in.next();
		String word2 = in.next();
		String word3 = in.next();
		System.out.println("The first word: "+word1);
		System.out.println("The second word: "+word2);
		System.out.println("The third word: "+word3);
	}
}