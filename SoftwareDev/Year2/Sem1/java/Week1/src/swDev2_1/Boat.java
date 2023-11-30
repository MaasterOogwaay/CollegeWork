package swDev2_1;

public abstract class Boat implements Machine {
	protected double thePrice;
	public Boat(double price) {
		this.thePrice = price;
	}
	
	public double getPrice() {
		return this.thePrice;
	}
	
	public String toString() {
		return this.getClass().getSimpleName();
	}
}

class Yacht extends Boat implements Desirable {
	Yacht(double price) {
		super(price);
	}
	
	public void start() {
		System.out.println("Yacht::start");
	}
	
	public void stop() {
		System.out.println("Yacht::stop");
	}
}

class Canoe extends Boat {
	Canoe(double price) {
		super(price);
	}
	
	public void start() {
		System.out.println("Canoe::start");
	}
	
	public void stop() {
		System.out.println("Canoe::stop");
	}
}

class Kayak extends Boat {
	Kayak(double price) {
		super(price);
	}
	
	public void start() {
		System.out.println("Kayak::start");
	}
	
	public void stop() {
		System.out.println("Kayak::stop");
	}
}
