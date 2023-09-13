import java.util.Scanner;
public class Wk4_2
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a number: ");
		int num1 = in.nextInt();
		if (num1 % 5 == 0) { //15/5 = 3R0
			System.out.println(num1+" is a multiple of 5!");
		} else { //14/5 = 2R4
			System.out.println(num1+" is NOT a multiple of 5!");
		}
	}
}