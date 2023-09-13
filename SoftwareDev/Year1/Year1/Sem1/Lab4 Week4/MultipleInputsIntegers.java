import java.util.Scanner;
public class MultipleInputsIntegers
{
	public static void main (String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter 3 numbers (seperate by spaces, then press enter): ");
		int num1 = in.nextInt();
		int num2 = in.nextInt();
		int num3 = in.nextInt();

		System.out.println("The first number: "+num1);
		System.out.println("The second number: "+num2);
		System.out.println("The third number: "+num3);
	}
}