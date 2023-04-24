import java.io.*;
import java.util.*;
class Cotton
{
	public static void slowPrint(String text, int speed) throws InterruptedException, IOException{
      // import java.io.* for method to work
      Writer w = new PrintWriter(System.out);
      for(int t = 0; t < text.length(); t++){
        System.out.print(text.charAt(t));
        w.flush();
        Thread.sleep(speed);
      }
    }

    //Context displayed
    public static void display() throws IOException, InterruptedException
    {
    	System.out.println("################################");
		System.out.println("	HELP ME WITH DA COTTON!!    ");
		System.out.println("################################");
		slowPrint(">> Random Guy : Welcome to the land of Cotton pickers!\n>> Do you see the old man there?\n>> Yeah the one with the blue panties\n>> Your job is to help the man count the cotton in his massive fields!",60);
		slowPrint("\n\n\n>> Farmer : Please count the fields for me! : ",40);
    }
	public static void main(String[] args) throws IOException, InterruptedException{

		//Loading and creating stuff;
		display();
		BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
		Random random = new Random();
		ArrayList<Integer> rotten_cottons = new ArrayList<>();

		//Playing the game with user
		try{
			int fields = Integer.parseInt(rd.readLine());
			int[] cottons = new int[fields];
			slowPrint("\n>> Farmer : GOOD! Now count the number of cotton in each field",30);
			for(int i=0; i < fields; i++)
			{
				String msg1 = "\n>> How many in field " + (i+1) + " : ";
				slowPrint(msg1,30);
				cottons[i] = Integer.parseInt(rd.readLine());
			}
			int field_no = random.nextInt(fields);

			String msg2 = "\n>> You need to work on field " + field_no;
			slowPrint(msg2,40); 


			int cotton_num = cottons[field_no];

			for(int j=0; j <= (cotton_num / 4) + 1; j++)
				rotten_cottons.add(random.nextInt(1,cotton_num + 1));

			slowPrint("\n>> Random entity : There are some rotten cottons here on this field.\n>> You will be asked which cottons are healthy\n>> If you name a rotten cotton you shall die!",40);
			int k = 1;
			while(k <= (cotton_num / 2) + 1)
			{
				System.out.println("\n>> Farmer : So which cotton do you think it is???");
				int user_thinks = Integer.parseInt(rd.readLine());
				if(user_thinks < 0 || user_thinks > cotton_num)
				{
					System.out.println(">> Invalid Cotton!");
				}
				else{
					if(rotten_cottons.contains(user_thinks))
					{
						//if player loses
						slowPrint(">> \nGAME OVER\nYOU ARE DEAD :/",80);
						System.exit(0);
					}
					else{
						System.out.println("GOOD!I'll Ask again");
						k++;
					}
				}

			}
			
		}catch(Exception e)
		{
			slowPrint(">>\nWHO : G     L     I      T      C      H    !@#$%^&*",120);
			System.exit(0);
		}
		//if player wins ->
		slowPrint(">>\nYOU HAVE PASSED THE TEST\nYOUR JOURNEY AWAITS YOU!",90);

	}
}