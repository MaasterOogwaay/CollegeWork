import java.util.Scanner;
public class Wk4_6
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter two characters: ");

		String word1 = in.next();
		String word2 = in.next();

		char ch1 = word1.charAt(0);
		char ch2 = word2.charAt(0);

		if (ch1 != ch2) {
			System.out.println("\'"+ch1+"\' does NOT equal \'"+ch2+"\'");
		} else {
			System.out.println("\'"+ch1+"\' equals \'"+ch2+"\'");
		}
	}
}