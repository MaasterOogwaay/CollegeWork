package week5.q2.code;

public class Car {
	private String theMake = "";
	private String theModel = "";
	private double theEngineSize = 0.0;
	private static int count = 0;
	
	Car() {
		this.theMake = "";
		this.theModel = "";
		this.theEngineSize = 0.0;
	}
	
	Car(String make, String model, double size) {
		this.theMake = make;
		this.theModel = model;
		this.theEngineSize = size;
	}

	public String getTheMake() {
		return theMake;
	}

	public void setTheMake(String theMake) {
		this.theMake = theMake;
	}

	public String getTheModel() {
		return theModel;
	}

	public void setTheModel(String theModel) {
		this.theModel = theModel;
	}

	public double getTheEngineSize() {
		return theEngineSize;
	}

	public void setTheEngineSize(double theEngineSize) {
		this.theEngineSize = theEngineSize;
	}

	public static int getCount() {
		++count;
		return count;
	}
	
	@Override
	public String toString() {
		return "Count: "+ getCount() + "\nMake: " + this.theMake + "\nModel: " + this.theModel + "\nEngine Size: " + this.theEngineSize;
	}
	

}
