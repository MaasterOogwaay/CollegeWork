package week5.q1.code;
import java.util.Scanner;

class Volume {
	private int length = 0;
	private int width = 0;
	private int height = 0;
	
	Volume() {
		this.length = 0;
		this.width = 0;
		this.height = 0;
	}
	
	Volume(int l, int w, int h) {
		this.length = l;
		this.width  = w;
		this.height = h;
	}

	public int calcVolume() {
		return this.length * this.width * this.height;
	}
	
	@Override
	public String toString() {
		return "For a length of "+ this.length + ", Width " + this.width + " and Height " + this.height + " the volume is " + calcVolume() + " metres cubed.";
	}
}

public class VolumeUserIO {

	private static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int length = getLength();
		int width = getWidth();
		int height = getHeight();
		
		Volume v1 = new Volume(length, width, height);
		System.out.println(v1.toString());


	}
	public static int getLength() {
		System.out.print("Please enter a length in metres: ");
		return in.nextInt();
	}
	
	public static int getWidth() {
		System.out.print("Please enter a width in metres: ");
		return in.nextInt();
	}
	
	public static int getHeight() {
		System.out.print("Please enter a height in metres: ");
		return in.nextInt();
	}

}
