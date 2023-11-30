import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class AddEmployee 
{
	static Connection con = null;
	static Statement stmt = null;
	static ResultSet rs = null;

	public static void main(String[] args) 
	{
		init_db();  // open the connection to the database
		try
		{
				String str = "INSERT INTO employees VALUES(null,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

				PreparedStatement pstmt = con.prepareStatement(str);
				pstmt.setString(1, "Dylan");
				pstmt.setString(2, "Thomas");
				// … [fill in the other values here..]
				pstmt.setString(3, "Yellow Road");
				pstmt.setString(4, "Woodville");
				pstmt.setString(5, "Athlone");
				pstmt.setString(6, "0852338040");
				pstmt.setString(7, "2003-08-11 00:00:00");
				pstmt.setString(8, "M");
				pstmt.setString(9, "Employee");
				pstmt.setDouble(10, 13.50);

				// Returns number of rows inserted
				int rows = pstmt.executeUpdate();

    			System.out.println("Number of rows updated successfully: "+rows);
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

