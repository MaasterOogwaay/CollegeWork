package swDev2_1;

public abstract class Car implements Machine {
	protected double thePrice;
	public Car(double price) {
		this.thePrice = price;
	}
	
	public double getPrice() {
		return this.thePrice;
	}
	
	public String toString() {
		return this.getClass().getSimpleName();
	}
	
	public abstract boolean isPractical();
}

class Saloon extends Car {
	Saloon(double price) {
		super(price);
	}
	
	public void start() {
		System.out.println("Saloon::start");
	}
	
	public void stop() {
		System.out.println("Saloon::stop");
	}
	
	public boolean isPractical() {
		return true;
	}
}

class Hatchback extends Car {
	Hatchback(double price) {
		super(price);
	}
	
	public void start() {
		System.out.println("Hatchback::start");
	}
	
	public void stop() {
		System.out.println("Hatchback::stop");
	}
	
	public boolean isPractical() {
		return true;
	}
}

class Convertible extends Car implements Desirable {
	Convertible(double price) {
		super(price);
	}
	public void start() {
		System.out.println("Convertible::start");
	}
	
	public void stop() {
		System.out.println("Convertible::stop");
	}
	
	public boolean isPractical() {
		return false;
	}
}
