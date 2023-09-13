import java.util.Scanner;
public class Wk4_4
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a word: ");
		String word = in.next();

		if (word.length() < 4) {
			System.out.println("\""+word+"\" is a short word!");
		} else {
			System.out.println("\""+word+"\" is NOT a short word!");
		}
	}
}