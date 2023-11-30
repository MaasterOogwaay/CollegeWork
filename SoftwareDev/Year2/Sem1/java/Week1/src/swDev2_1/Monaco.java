package swDev2_1;

import java.util.ArrayList;

public class Monaco {

	public static void main(String[] args) {
		ArrayList<Machine> machines = new ArrayList<>();
		Machine yacht = new Yacht(500_000);
		machines.add(yacht);
		
		Machine saloon = new Saloon(25_000); 
		machines.add(saloon);
		
		processMachines(machines);

	}
	
	public static void processMachines(ArrayList<Machine> machines) {
		for (Machine vehicle : machines) {
			if (vehicle instanceof Desirable) {
				System.out.println(vehicle + " - Desirable Item");
			} else {
				System.out.println(vehicle);
			}
		}
	}
}

interface Desirable {
	
}

interface Machine {
	public void start();
	public void stop();
	public double getPrice();
}


