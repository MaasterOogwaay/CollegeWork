package oop1.shop;

public abstract class Computer implements ElectronicDevice {
	String theMake, theModel;
	
	public Computer(String aMake, String aModel) {
		theMake = aMake;
		theModel = aModel;
	}
	
	public String getTheMake() {
		return theMake;
	}
	
	public String getTheModel() {
		return theModel;
	}
	
	@Override
	public String toString() {
		return getTheMake() + " " + getTheModel();
	}
	
	public abstract boolean login(String user, String pass);
	
	public abstract boolean logout();
}

class Laptop extends Computer {
	Laptop(String aMake, String aModel) {
		super(aMake, aModel);
	}
	
	public void turnOn() {
		System.out.println("Laptop::turnOn()");
	}
	
	public void turnOff() {
		System.out.println("Laptop::turnOff()");
	}
	
	@Override
	public boolean login(String user, String pass) {
		System.out.println("Laptop::login()");
		return true;
	}
	
	@Override
	public boolean logout() {
		System.out.println("Laptop::logout()");
		return true;
	}
}

class Ipad extends Computer implements HighlyDesirable {
	Ipad(String aMake, String aModel) {
		super(aMake, aModel);
	}
	
	public void turnOn() {
		System.out.println("Ipad::turnOn()");
	}
	
	public void turnOff() {
		System.out.println("Ipad::turnOff()");
	}
	
	@Override
	public boolean login(String user, String pass) {
		System.out.println("Ipad::login()");
		return true;
	}
	
	@Override
	public boolean logout() {
		System.out.println("Ipad::logout()");
		return true;
	}
}
