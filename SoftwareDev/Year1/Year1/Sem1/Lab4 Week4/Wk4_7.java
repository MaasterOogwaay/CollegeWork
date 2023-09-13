import java.util.Scanner;
public class Wk4_7
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter two words: ");

		String word1 = in.next();
		String word2 = in.next();

		if (word1.length() == word2.length()) {
			System.out.println("\""+word1+"\" and "+"\""+word2+"\" are the same length!");
		} else {
			System.out.println("\""+word1+"\" and "+"\""+word2+"\" are NOT the same length!");
		}
	}
}