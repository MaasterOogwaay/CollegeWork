package week5.q2.code;
import java.util.Scanner;

public class Showroom {
	private static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String makeOfCar = getMake();
		String modelOfCar = getModel();
		double engineSizeOfCar = getEngineSize();
		
		Car c3 = new Car(makeOfCar, modelOfCar, engineSizeOfCar);
		// Car.getCount();
		System.out.println(c3.toString());

	}

	public static String getMake() {
		System.out.print("Enter the make of car: ");
		String make = in.nextLine();
		return make;
	}
	
	public static String getModel() {
		System.out.print("Enter the model of car: ");
		String model = in.nextLine();
		return model;
	}
	
	public static double getEngineSize() {
		System.out.print("Enter the engine size of the car: ");
		double engineSize = in.nextDouble();
		return engineSize;
	}
}
