package semm1.equals;

public class Dog {
	private String name;
	private int age;
	
	public Dog(String name, int age) {
		super();
		this.name = name;
		this.age = age;
	}
	
	// no equals()
	// no toString()
	// uses inherited ones from Object:
	//		- toString() returns semm1.equals.Dog@4aa8f0b4
	//		- equals() compares references to see if they are pointing at the same object
	//			- this is the same as ==
}
