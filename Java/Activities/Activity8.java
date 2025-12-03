package activities;

class CustomException extends Exception {
    private String message = null;
 
    public CustomException(String message) {
        this.message = message;
    }
 
    @Override
    public String getMessage() {
        return message;
    }
}
public class Activity8 {

	public static void main(String[] a){
        try {
            Activity8.exceptionTest("This is Activity8");
            Activity8.exceptionTest(null);
            Activity8.exceptionTest("Will print this if null is commented");
        } catch(CustomException mae) {
            System.out.println("Inside catch block: " + mae.getMessage());
        }
    }
 
    static void exceptionTest(String str) throws CustomException {
        if(str == null) {
            throw new CustomException("null value is passed");
        } else {
            System.out.println(str);
        }
    }
}
