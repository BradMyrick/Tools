/*
ask user for a number of minutes
convert minutes to seconds
print the number of seconds
*/

public class Main {
public static void main(String[] args) {
        int minutes;
        System.out.print("Enter a number of minutes: ");
        minutes = System.in.read();
        int seconds = minutes * 60;
        System.out.println("The number of seconds is " + seconds);
    }
}
