package week4.code;
import java.util.Scanner;

class Phone {
	private String theNumber = "";
	private String theOwnersName = "";
	private double thePrice = 0.0;
	
	Phone(String aNumber, String aOwnersName, double aPrice) {
		this.theNumber = aNumber;
		this.theOwnersName = aOwnersName;
		this.thePrice = aPrice;
	}
	
	Phone() {
		this.theNumber = "";
		this.theOwnersName = "";
		this.thePrice = 0.0;
	}
	
	public String getNumber() {
		return this.theNumber;
	}


	public void setNumber(String aNumber) {
		this.theNumber = aNumber;
	}
	
	public String getOwnersName() {
		return this.theOwnersName;
	}
	
	public void setOwnerName(String aOwnersName) {
		this.theOwnersName = aOwnersName;
	}
	
	public double getPrice() {
		return this.thePrice;
	}
	
	public void setPrice(double aPrice) {
		this.thePrice = aPrice;
	}
	
	public String toString() {
		return "Number: "+this.theNumber + "\nOwner: " + this.theOwnersName + "\nPrice: €" + this.thePrice;
	}
	
	
}

public class PhoneUserIO {
	private static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		String number = getPhoneNumber();
		String name = getOwner();
		double price = getPrice();
		
		Phone p1 = new Phone();
		p1.setNumber(number);
		p1.setOwnerName(name);
		p1.setPrice(price);
		
		System.out.println(p1.toString());
		
		Phone p2 = new Phone(number, name, price);
		System.out.println(p2.toString());

	}
	
	public static String getPhoneNumber() {
		System.out.print("Please enter a phone number: ");
		return in.nextLine();
	}
	public static String getOwner() {
		System.out.print("Please enter the new owners name: ");
		return in.nextLine();
	}
	public static double getPrice() {
		System.out.print("Please enter a price: ");
		return in.nextDouble();
	}

}
