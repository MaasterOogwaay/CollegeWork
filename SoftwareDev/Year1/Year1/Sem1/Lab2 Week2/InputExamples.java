import java.util.Scanner;
public class InputExamples
{
	public static void main (String[] agrs)
	{
		Scanner in = new Scanner (System.in);

		System.out.print("Please enter your age: ");
		int age = in.nextInt();
		System.out.print("please enter what you think is the average age in this lab: ");
		double averageLabAge = in.nextDouble();
		System.out.print("Please enter your name: ");
		String name = in.next();

		System.out.println("Hello "+name+"!");
		System.out.println("You are "+age+" years old!");

		System.out.println("Average class age is: "+averageLabAge);
	}
}
