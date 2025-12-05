package activities;

import java.util.HashSet;

public class Activity10 {
	public static void main(String[] args) {
		HashSet<String> hs = new HashSet<String>();
		hs.add("W");
		hs.add("A");
		hs.add("L");
		hs.add("K");
		hs.add("E");
		hs.add("D");
		
		System.out.println("Original Hashset: " + hs);
		System.out.println("Size of the HashSet : " + hs.size());
		System.out.println("Removing D from Hashset: " + hs.remove("D"));
		
		if(hs.remove("Y")) {
			System.out.println("Y is removed from the hash set");
		} else {
			System.out.println("Y is not present in the hashset");
		}
			
		System.out.println("Is W is present in the set: " + hs.contains("W"));
		System.out.println("New HashSet: " + hs);
		}
	}
