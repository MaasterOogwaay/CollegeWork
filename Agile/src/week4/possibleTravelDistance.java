package week4;
import java.util.Scanner;
public class possibleTravelDistance {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter litres in tank: ");
		int litresInTank = in.nextInt();
		
		System.out.print("Please enter fuel efficiency: ");
		int fuelEfficiency = in.nextInt();
		
		if (litresInTank < 0) {
			System.out.println("Please enter a valid number of Litres in Tank");
		} else if (fuelEfficiency < 0) {
			System.out.println("Please enter a valid number for Fuel Efficiency");
		} else {
			double result = litresInTank * fuelEfficiency; 
			System.out.println("Possible distance you can travel = " + result);
		}

	}

}
