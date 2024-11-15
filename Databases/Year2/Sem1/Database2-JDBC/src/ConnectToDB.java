import java.sql.*;
public class ConnectToDB 
{
	static Connection con = null;
	static Statement stmt = null;
	static ResultSet rs = null;

	public static void main(String[] args) 
	{
		init_db();  // open the connection to the database
		try
		{
			rs = stmt.executeQuery("SELECT count(*) as total FROM employees");
    			rs.next();//move to first, the query above only produces 1 tuple
   	 		int myTotal = rs.getInt("total");
    			System.out.println("Total employees: "+myTotal);
		}
		catch (SQLException sqle)
		{
			System.out.println("Error: failed to get number of records");
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

