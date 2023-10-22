package week6.code;

class Art {
	Art() {
		// System.out.println(getClass().getSimpleName() + " Constructor");
		System.out.println("Art Constructor");
	}
	
	public void sketch() {
		System.out.println("Art::sketch()");
		
	}
	
	@Override
	public String toString() {
		return "Art::toString()";
	}
	
}

class Drawing extends Art {
	Drawing() {
		// System.out.println(getClass().getSimpleName() + " Constructor");
		System.out.println("Drawing Constructor");
	}
	
	public void sketch() {
		System.out.println("Drawing::sketch()");
		
	}
	
	@Override
	public String toString() {
		return "Drawing::toString()";
	}
	
}

public class Cartoon extends Drawing {
	
	Cartoon() {
		System.out.println("Cartoon Constructor");
	}
	
	public void sketch() {
		System.out.println("Cartoon::sketch()");
	}
	
	public void tomAndJerry() {
		System.out.println("Cartoon::tomAndJerry()");
	}
	
	public void sketch(Art a) {
		tomAndJerry(); // calls method but not safely 
	}
	
	public static void upcasting() {
		Art a1 = new Art();
		System.out.println("---| upcasting a1 |---");
		System.out.println(a1);
		
		Art a2 = new Drawing();
		System.out.println("---| upcasting a2 |---");
		System.out.println(a2);
		
		Art a3 = new Drawing();
		System.out.println("---| upcasting a3 |---");
		System.out.println(a3);
	}

	public static void downcasting() {
		Art a = new Drawing();
		Drawing d1 = a; // ERROR
		Drawing d2 = (Drawing) a; // OK due to downcast
	}
	
	public static void main(String[] args) {
		
		//Cartoon c = new Cartoon();
		//System.out.println("---| c.sketch(new Art()) |---");
		// 1. Creates new art constructor
		// 2. Passes art into sketch method
		// 3. Goes to sketch(Art a)
		// 4. Goes to tomAndJerry() and prints what's in there
		//c.sketch(new Art());
		
		//System.out.println("---| c.sketch(new Drawing()) |---");
		//c.sketch(new Drawing());
		
		//System.out.println("---| c.sketch(new Cartoon()) |---");
		//c.sketch(new Cartoon());
		
		System.out.println("---| upcasting() |---");
		upcasting();
		
		// TODO
		// System.out.println("---| downcasting() |---");
		// downcasting();
		

	}

}
