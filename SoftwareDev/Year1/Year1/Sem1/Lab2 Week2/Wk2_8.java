import java.util.Scanner;
public class Wk2_8
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter the first number: ");
		int num1 = in.nextInt();
		System.out.print("Please enter the second number: ");
		int num2 = in.nextInt();

		int sum = num1 + num2;
		System.out.println("The sum: "+sum);

		System.out.println("The difference: "+(num1-num2));

		System.out.println("The product: "+(num1*num2));

		System.out.println("The average: "+(sum/2.0));

		System.out.println("The distance: "+Math.abs(num1-num2));

		System.out.println("The maximum: "+Math.max(num1, num2));

		System.out.println("The minimum: "+Math.min(num1, num2));
	}
}