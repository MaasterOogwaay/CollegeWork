package oop1.shop;

public abstract class Television implements ElectronicDevice {
	String theMake, theModel;
	
	public Television(String aMake, String aModel) {
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
}

class Plasma extends Television implements HighlyDesirable {
	Plasma(String aMake, String aModel) {
		super(aMake, aModel);
	}
	
	public void turnOn() {
		System.out.println("Plasma::turnOn()");
	}
	
	public void turnOff() {
		System.out.println("Plasma::turnOff()");
	}
}

class LED extends Television {
	LED(String aMake, String aModel) {
		super(aMake, aModel);
	}
	
	public void turnOn() {
		System.out.println("LED::turnOn()");
	}
	
	public void turnOff() {
		System.out.println("LED::turnOff()");
	}
}
