package week4;
import java.util.Scanner;
public class costPer100KM {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Please Enter the fuel efficiency: ");
		int fuelEfficiency = in.nextInt();
		
		System.out.print("Please Enter the price of petrol: ");
		double priceOfPetrol = in.nextDouble();
		
		if (fuelEfficiency < 0) {
			System.out.println("Please enter a valid postive Fuel Efficiency");
		} else if(priceOfPetrol < 0) {
			System.out.println("Please enter a valid Price Of Petrol");
		} else {
			double result = fuelEfficiency * priceOfPetrol;
			System.out.println("Cost per 100 KM = " + result);
		}

	}

}

