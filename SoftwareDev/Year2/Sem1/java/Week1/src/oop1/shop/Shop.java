package oop1.shop;

import java.util.ArrayList;

public class Shop {

	public static void main(String[] args) {
		ArrayList<ElectronicDevice> devices = new ArrayList<>();
		
		ElectronicDevice plasma = new Plasma("Sony", "P300");
		devices.add(plasma);
		
		ElectronicDevice laptop = new Laptop("Dell", "Inspiron");
		devices.add(laptop);

		
		processDevices(devices);

	}
	
	public static void processDevices(ArrayList<ElectronicDevice> devices) {
		for (ElectronicDevice ed : devices) {
			if (ed instanceof HighlyDesirable) {
				System.out.println(ed + " - Highly Desirable Item");
			} else {
				System.out.println(ed);
			}
		}
	}

}
