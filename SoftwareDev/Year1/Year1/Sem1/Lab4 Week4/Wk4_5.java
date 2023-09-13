import java.util.Scanner;
public class Wk4_5
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter two numbers: ");
		int num1 = in.nextInt();
		int num2 = in.nextInt();

		if (num1 < num2) {
			System.out.println(num1+" is smaller than "+num2);
		} else {
			System.out.println(num1+" is greater then or equal to "+num2);
		}
	}
}