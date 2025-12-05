package activities;

import java.util.HashMap;

public class Activity11 {
	public static void main(String[] args) {
		HashMap<Integer, String> hash_map = new HashMap<Integer, String>();
		hash_map.put(1, "Pink");
        hash_map.put(2, "Blue");
        hash_map.put(3, "White");
        hash_map.put(4, "Green");
        hash_map.put(5, "Black");
        
        System.out.println("The original map: " + hash_map);
        hash_map.remove(3);
        System.out.println("After removing White: " + hash_map);
        
        if(hash_map.containsValue("Blue")) {
        	System.out.println("Blue exists in the Map");
        }else {
        	System.out.println("Blue does not exist in the Map");
        }
        
        System.out.println("Number of colours in the Map is: " + hash_map.size());
	}

}
