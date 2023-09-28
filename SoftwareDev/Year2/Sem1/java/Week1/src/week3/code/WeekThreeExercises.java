package week3.code;
import java.util.Scanner;

public class WeekThreeExercises {
	static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		welcomeToApp();
		greeting();
		
		 String favFilm = favouriteFilm();
		 //System.out.println(favFilm);
		 
		 int rating = filmRating(favFilm);
		 if (rating == 1) {
			 System.out.println("You rated the movie: "+rating+" = Very Bad");
		 }
		 if (rating == 2) {
			 System.out.println("You rated the movie: "+rating+" = Bad");
		 }
		 if (rating == 3) {
			 System.out.println("You rated the movie: "+rating+" = Good");
		 }
		 if (rating == 4) {
			 System.out.println("You rated the movie: "+rating+" = Very Good");
		 }
		 if (rating == 5) {
			 System.out.println("You rated the movie: "+rating+" = Excellent");
		 }
		 
//		 filmRating(favFilm);
		
		//boolean doa = didOswaldActAlone();
//		System.out.println("You rated the movie "+rating);
		

	}
	
	public static void welcomeToApp() {
		System.out.println("Welcome to the app!");
	}
	
	public static void greeting() {
		System.out.print("Enter your first name: ");
		String firstName = in.next();
		System.out.println("Welcome "+firstName);
	}
	
	public static String favouriteFilm() {
		System.out.print("Enter your favourite film: ");
		String favFilm = in.next();
		return "Your favourite film is: "+favFilm; // TODO 
	}
	
	public static int filmRating(String film) {
		System.out.print("How would you rate " + film + " on a scale from 1-5? ");
		int rating = in.nextInt();
		return rating; // TODO
	}
	
	public static boolean didOswaldActAlone() {
		return false; // TODO
	}
	
	public boolean wasOjGuilty() {
		return false; // TODO
	}

}
