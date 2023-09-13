import java.util.Scanner;
public class Wk5_10
{
	public static void main(String [] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please choose a month from a number between 1 and 12: ");
		int digit = in.nextInt();

		String digitName = "";
		switch (digit)
		{
			case 1:
				digitName = "31 days ";
				break;
			case 2:
				digitName = "28 or 29 days";
				break;
			case 3:
				digitName = "31 days";
				break;
			case 4:
				digitName = "30 days";
				break;
			case 5:
				digitName = "31 days";
				break;
			case 6:
				digitName = "30 days";
				break;
			case 7:
				digitName = "31 days";
				break;
			case 8:
				digitName = "31 days";
				break;
			case 9:
				digitName = "31 days";
				break;
			case 10:
				digitName = "31 days";
				break;
			case 11:
				digitName = "30 days";
				break;
			case 12:
				digitName = "31 days";
				break;
			default:
				digitName = "Invalid digit!";
				break;
		}

		System.out.println(digitName);
	}
}