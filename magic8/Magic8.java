
// Import required class
import java.util.Random;

public class Magic8 {
  public static void main(String[] args) {
    System.out.println(RandomFortune());
    System.out.println(RandomFortune());
    System.out.println(RandomFortune());
    System.out.println(RandomFortune());
    System.out.println(RandomFortune());
  }

  // Static class to return 1 of 10 random fortunes
  public static String RandomFortune() {
    // Create instance of Random class
    Random rand = new Random();

    // Generate random number 0-9
    int rand_int = rand.nextInt(10);

    // Declare fortune return variable
    String fortune;

    // Define fortune as different string based on random integer
    switch (rand_int) {
      case 0:
        fortune = "Live long and prosper";
        break;
      case 1:
        fortune = "A journey of a thousand miles begins with the first step";
        break;
      case 2:
        fortune = "Peace be with you";
        break;
      case 3:
        fortune = "The roulette wheel favours you today";
        break;
      case 4:
        fortune = "Stay away from crowded places";
        break;
      case 5:
        fortune = "Buy Bitcoin. Now sell. Buy! SELL SELL SELL!!";
        break;
      case 6:
        fortune = "The voices you hear when you are home alone should not be trusted";
        break;
      case 7:
        fortune = "Water your plants";
        break;
      case 8:
        fortune = "Eat vegetables";
        break;
      case 9:
        fortune = "Go back to bed, today is not for you";
        break;
      default:
        fortune = "Good luck!";
    }

    // Return the fortune
    return fortune;
  }
}