import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
public class AddEmployee2 
{
	static Connection con = null;
	static Statement stmt = null;
	static ResultSet rs = null;

	public static void main(String[] args) 
	{
		init_db();  // open the connection to the database
		Scanner in = new Scanner(System.in);
		try
		{
				System.out.print("Please enter the first name: ");
				String firstName = in.nextLine();
				
				System.out.print("Please enter the last name: ");
				String lastName = in.nextLine();
				
				System.out.print("Please enter the address1: ");
				String address1 = in.nextLine();
				
				System.out.print("Please enter the address2: ");
				String address2 = in.nextLine();
				
				System.out.print("Please enter the town: ");
				String town = in.nextLine();
				
				System.out.print("Please enter the contactNo: ");
				String contactNo = in.nextLine();
				
				System.out.print("Please enter the dateOfBirth: ");
				String dateOfBirth = in.nextLine();
				
				System.out.print("Please enter the gender: ");
				String gender = in.nextLine();
				
				System.out.print("Please enter the postion: ");
				String position = in.nextLine();
				
				System.out.print("Please enter the rate: ");
				double rate = in.nextDouble();
				
				String str = "INSERT INTO employees VALUES(null,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

				PreparedStatement pstmt = con.prepareStatement(str);
				pstmt.setString(1, firstName);
				pstmt.setString(2, lastName);
				pstmt.setString(3, address1);
				pstmt.setString(4, address2);
				pstmt.setString(5, town);
				pstmt.setString(6, contactNo);
				pstmt.setString(7, dateOfBirth);
				pstmt.setString(8, gender);
				pstmt.setString(9, position);
				pstmt.setDouble(10, rate);

				// Returns number of rows inserted
				int rows = pstmt.executeUpdate();

    			System.out.println("Number of rows updated successfully: "+rows);
    			in.close();
		}
		catch (SQLException sqle)
		{
			System.out.println("Error: failed to get number of records");
			// sqle.printStackTrace();
		}
		try
		{
			con.close();
		}
		catch (SQLException sqle)
		{
			System.out.println("Error: failed to close the database");
		}
	}
	public static void init_db()
	{
		try
		{
			Class.forName("com.mysql.cj.jdbc.Driver");
			String url="jdbc:mysql://localhost:3306/library?useTimezone=true&serverTimezone=UTC";
			con = DriverManager.getConnection(url, "root", "admin");
			stmt = con.createStatement();
		}
		catch(Exception e)
		{
			System.out.println("Error: Failed to connect to database\n" + e.getMessage());
		}
	}
}

