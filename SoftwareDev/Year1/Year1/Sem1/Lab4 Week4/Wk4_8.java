import java.util.Scanner;
public class Wk4_8
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a word: ");

		String word1 = in.next();

		if (word1.charAt(0) <= 90) {
			System.out.println("The word \""+word1+"\" starts with a capital \'"+word1.charAt(0)+"\'");
		} else {
			System.out.println("The word \""+word1+"\" starts with a lowercase \'"+word1.charAt(0)+"\'");
		}
	}
}