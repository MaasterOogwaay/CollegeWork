package semm1.equals;

public class Test {

	public static void main(String[] args) {
		dogs();
		//persons();
	}
	public static void persons() {
		Person joe1 = new Person("Joe Bloggs", 21);
		Person joe2 = new Person("Joe Bloggs", 21);
		// toString()
		System.out.println(joe1);				// Person [age=21, name=Joe Bloggs]
		System.out.println(joe2);				// Person [age=21, name=Joe Bloggs]

		// equals()
		// Get equals() to return true
		System.out.println(joe1 == joe2);		// false, comparing references
		System.out.println(joe1.equals(joe2));	// true
		
		// Get each part of equals() to return false
		// Firstly, compare a Dog and a Person (instanceof protects us from a ClassCastException)
		Dog blackie = new Dog("Blackie", 2);
		System.out.println(joe1.equals(blackie));	// false, Person::equals() called but 
													// 	      'blackie' not a Person
		System.out.println(blackie.equals(joe1));	// false, Object::equals() called but
													// 		  'blackie' and 'joe1' are referring
													//         to 2 different Objects
		
		// Now compare 2 Person objects where their ages are different.
		Person joe3 = new Person("Joe Bloggs", 25);
		Person joe4 = new Person("Joe Bloggs", 26);
		System.out.println(joe3 == joe4);		// false
		System.out.println(joe3.equals(joe4));	// false, different ages

		// Finally, compare 2 Person objects where their names are different.
		Person joe5 = new Person("J. Bloggs", 29);
		Person joe6 = new Person("Joe Bloggs", 29);
		System.out.println(joe5 == joe6);		// false
		System.out.println(joe5.equals(joe6));	// false, different names

	}
	public static void dogs() {
		// Dog
		Dog spot1 = new Dog("Spot", 2);
		Dog spot2 = new Dog("Spot", 2);

		// toString()
		System.out.println(spot1);	// semm1.equals.Dog@4d591d15, calls Object::toString
		System.out.println(spot2);	// semm1.equals.Dog@4aa8f0b4, calls Object::toString

		// equals()
		System.out.println(spot1 == spot2);			// false, 2 different objects
		System.out.println(spot1.equals(spot2));	// false, calls Object::equals() which is
													//        the same as ==
		
	}
}
