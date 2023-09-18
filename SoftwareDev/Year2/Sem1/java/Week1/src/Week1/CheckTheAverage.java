package Week1;

import java.util.Scanner;

public class CheckTheAverage {
	private static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		// type sysout then ctrl+space
		System.out.println("Please enter a number: ");
	    int x = sc.nextInt();
	    System.out.println("You have entered the number: "+x);
	    
		System.out.println("Please enter a number: ");
	    int y = sc.nextInt();
	    System.out.println("You have entered the number: "+y);
	    
		System.out.println("Please enter a number: ");
	    int z = sc.nextInt();
	    System.out.println("You have entered the number: "+z);

	    // if you start with string it concats nums otherwise it adds
	    System.out.println("You have entered the numbers: "+x+" "+y+" "+" "+z);
	    
	    double average = calcAverage(x,y,z);
	    System.out.println("Average: "+average);
	    
	    if (average < 10) {
	    	System.out.println("The average is less then 10:");
	    } else if (average >=10 && average <= 20) {
	    	System.out.println("The average is betwen 10 and 20:");
	    } else if (average > 20) {
	    	System.out.println("The average is greater than 20:");
	    }
	    
	}
	// access modifier, non access modifier, return type
	// name, inputs, body
	// if the return type is not void, we have to include return in the body
	public static double calcAverage(int a, int b, int c) {
		// double result = (a+b+c)/3;
		// return result;
		return (a+b+c)/3;
		
	}
}
