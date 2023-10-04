package week3;

import java.util.Scanner;
public class ProductThreeInts {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter an integer: ");
		int num1 = in.nextInt();
		System.out.print("Enter an integer: ");
		int num2 = in.nextInt();
		System.out.print("Enter an integer: ");
		int num3 = in.nextInt();
		
		if (num1 < 1 || num2 < 1 || num3 < 3) {
			System.out.println("Please enter valid positive integers!");
		} else {
			int total = num1 * num2 * num3;
			System.out.println("Product = "+ total);
		}
		
		in.close();

	}

}
