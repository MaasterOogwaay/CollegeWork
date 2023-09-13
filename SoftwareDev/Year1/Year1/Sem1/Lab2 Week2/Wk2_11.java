import java.util.Scanner;
public class Wk2_11
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter the drive name: ");
		String driveName = in.next();
		System.out.print("Please enter the file path: ");
		String filePath = in.next();
		System.out.print("Please enter the file name: ");
		String fileName = in.next();
		System.out.print("Please enter the file extension: ");
		String fileExtension = in.next();

		System.out.println("File path: "+driveName +":" + filePath + fileName + "."+ fileExtension);
	}
}