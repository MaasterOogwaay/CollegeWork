package week2.code;

public class Primitives {
	public static void main(String[] args) {
//		primitives();
		incrDecr();
		
	}
	
	public static void primitives() {
		long a = 567888;
		short b = 248;
		int c = 12545;
		float d = 1236.0f;
		double e = 346.0;
		byte f = 26;
		char g = 'A';
		boolean h = false;
		
		System.out.println("Byte: " + f + "\nShort: " + b + "\nInt: " + c + "\nLong: " + a + "\nFloat: " + d + "\nDouble: " + e + "\nBoolean: " + h + "\nChar: " + g);
		
	}
	
	public static void casting() {
		byte a1 = -128;
		short b1 = -32767;
		int c1 = 12;
		int c2 = 12;
		int c3 = 300000000;
		int c4 = 2_000_000;
		int c5 = 2_00;
		float f1 = 300000000000000000000000000000000000000.0f;
		float f2 = 300000000000000000000000000000000000000.0f;
		long e = 567888;
		double g = 346.0;
		char h = 65;    

		
	}
	
	public static void incrDecr() {
		int a = 12;
		double b = 12.0;
		
		int c = a;
		int prefixedC = ++c;
		int postfixedC = c++;
		
		double d = b;
		double prefixedD = ++d;
		double postfixedD = d++;
		
		System.out.println("Original a: "+a+" Prefixed: "+prefixedC+" Postfixed: "+postfixedC+"\nOriginal b: "+b+" Prefixed: "+prefixedD+" Postfixed: "+postfixedD);
		
	}

}
