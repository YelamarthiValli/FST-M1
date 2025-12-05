package activities;

import java.util.ArrayList;

public class Activity9 {
	public static void main(String[] args) {
		ArrayList<String> myNames = new ArrayList<String>();
		myNames.add("Upesh");
        myNames.add("Manasa");
        myNames.add("Baby");
        myNames.add(3, "x");
        myNames.add(1, "Fam");
        
        System.out.println("Printing all the names");
        for(String m:myNames) {
        	System.out.println(m);
        }
        
        System.out.println("3rd name is " + myNames.get(2));
        System.out.println("Is Fawn is in the list: " + myNames.contains("Fawn"));
        System.out.println("Length of the List " + myNames.size());
        
        myNames.remove("x");
        
        System.out.println("Printing all the names in new list");
        for(String m:myNames) {
        	System.out.println(m);
        }
        
        System.out.println("New length of the list " + myNames.size());
        
	}
}
