package activities;

public class Activity6 {

    public static void main(String[] args) throws InterruptedException {
        //There is a plane with max 10 passengers
        Plane plane = new Plane(10);
        //Add passengers on the list
        plane.onboard("Upesh");
        plane.onboard("Manasa");
        plane.onboard("Baby");
        plane.onboard("A");
        plane.onboard("B");
        plane.onboard("C");
        plane.onboard("D");
        plane.onboard("E");
        plane.onboard("F");
        plane.onboard("G");
        plane.onboard("H");
        plane.onboard("I");
        //Plane takes off
        System.out.println("Plane took off at: " + plane.takeOff());
        //Print list of people on board
        System.out.println("People on the plane: " + plane.getPassengers());
        //Flying.....
        Thread.sleep(6000);
        //Plane has landed
        plane.land();
        //Plane lands
        System.out.println("Plane landed at: " + plane.getLastTimeLanded());
        System.out.println("People on the plane after landing: " + plane.getPassengers());
    }
}
