import java.util.Scanner;
public class Wk2_9
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter the radius: ");
		int radius = in.nextInt();

		System.out.println("The area: "+Math.PI*radius*radius);
		System.out.println("The circumference: "+2*Math.PI*radius);
		System.out.println("The volume: "+4/3.0*Math.PI*Math.pow(radius, 3));
		System.out.println("The Surface Area: "+Math.PI*radius*radius);
	}
}