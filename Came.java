//imported all required packages and classes for program
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

class Came{

//Creating the array which contains the names
public static final String[] Names = {"John", "Sam", "Akhil", "Ron", "Suresh", "Zlatan"};
//Maximum number of tries
public static final int MaxTries = 3;

//Simple function to give context to user and print the names
    public static void DisplayNames()
    {
        System.out.println("#####################################");
        System.out.println("     WHO WAS THE ONE WHO CAME ??     ");
        System.out.println("#####################################");
        System.out.println("Welcome to this name guessing game where you guess who was the one who came!");
        System.out.println("The Names are :");
        System.out.println(Arrays.toString(Names));
    }
    public static void main(String[] args)throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        Random random = new Random();
        //Selecting the random name
        int name = random.nextInt(6);
        int i=1;
        //Boolean to store if user answered correctly
        boolean Answered = false;

        DisplayNames();

        //Time for user to try guessing
        while(i <= MaxTries)
        {
            System.out.println(">> Who was it ?: ");
            //Try catch to handle errors
            try{
                //Conditionals to check the validity of guess
                int choice = Integer.parseInt(read.readLine());
                if(choice > 6 || choice < 0)
                    {
                        System.err.println("Invalid input!");
                        continue;
                    }
                
                if(choice - 1 == name){
                    System.out.println("Yes you got it right. It was " + Names[choice-1] + " indeed!");
                    Answered = true;
                    break;
                }else{
                    System.out.println("Uhuh wrong choice try again\nYou have " + (MaxTries - i) + " choices left\n");
                    i++;
                }
            }catch(NumberFormatException e)
            {
                System.out.println("OOPS input in numbers please !");
            }
        }
        //Finally finishing code
        if(Answered)
            System.out.println("GOOD JOB!! You won!");
        else
            System.out.println("You Lost !\nCorrect answer was : " + Names[name-1]);
    }
}