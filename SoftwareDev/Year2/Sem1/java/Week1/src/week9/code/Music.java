package week9.code;

public class Music {
	public static void main(String[] args) {
		Instrument[] orchestra = new Instrument[5];
//		orchestra[0] = new Instrument();
//		orchestra[1] = new Instrument();
//		orchestra[2] = new Instrument();
//		orchestra[3] = new Instrument();
//		orchestra[4] = new Instrument();
		
		orchestra[0] = new Stringed();
		orchestra[1] = new Wind();
		orchestra[2] = new Percussion();
		orchestra[3] = new Brass();
		orchestra[4] = new Woodwind();
		
		tuneAll(orchestra);
	}
	
	public static void tune(Instrument i) {
		i.play();
		System.out.println(i.what());
		i.adjust();
		
		
	}
	
	public static String tuneAll(Instrument[] e) {
		for (int i = 0; i < e.length; i++) {
			  tune(e[i]);
			}
		return "";
	}
	
}

interface Instrument {
	public void play(); // abstract by default
	
	public String what();
	
	public void adjust();
}

class Stringed implements Instrument {
	public void play() {
		System.out.println("Stringed::play()");
	}
	
	public String what() {
		return "Stringed";
	}
	
	public void adjust() {
		System.out.println("Stringed::adjust()");
	}
}

class Wind implements Instrument {
	public void play() {
		System.out.println("Wind::play()");
	}
	
	public String what() {
		return "Wind";
	}
	
	public void adjust() {
		System.out.println("Wind::adjust()");
	}
}

class Percussion implements Instrument {
	public void play() {
		System.out.println("Percussion::play()");
	}
	
	public String what() {
		return "Percussion";
	}
	
	public void adjust() {
		System.out.println("Percussion::adjust()");
	}
}

class Brass extends Wind {
	public void play() {
		System.out.println("Brass::play()");
	}
	
	public String what() {
		return "Brass";
	}
}

class Woodwind extends Wind {
	public void play() {
		System.out.println("Woodwind::play()");
	}
	
	public String what() {
		return "Woodwind";
	}
}
