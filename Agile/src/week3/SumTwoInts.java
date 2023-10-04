package week3;

import java.util.Scanner;

public class SumTwoInts {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter an integer: ");
		int num1 = in.nextInt();
		System.out.print("Enter an integer: ");
		int num2 = in.nextInt();
		
		if (num1 < 1 || num2 < 1) {
			System.out.println("Please enter valid positive integers!");
		} else {
			int total = num1 + num2;
			System.out.println("Sum = "+ total);
		}
		
		in.close();

	}

}
