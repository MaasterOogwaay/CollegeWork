import java.util.Scanner;
public class Wk2_10
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter the length: ");
		int length = in.nextInt();
		System.out.print("Please enter the width: ");
		int width = in.nextInt();

		int pLength = 2*length;
		int pWidth = 2*width;
		int perimeter = pLength+pWidth;

		double diagonalLength = Math.sqrt(Math.pow(length, 2) + Math.pow(width, 2));

		System.out.println("The area: "+length*width);
		System.out.println("The perimeter: "+perimeter);
		System.out.println("The diagonal distance: "+diagonalLength);
	}
}