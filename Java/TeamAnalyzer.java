import java.sql.*;

public class TeamAnalyzer {
    // All the "against" column suffixes:
    static String[] types = {
        "bug","dark","dragon","electric","fairy","fight",
        "fire","flying","ghost","grass","ground","ice","normal",
        "poison","psychic","rock","steel","water"
    };

    public static void main(String... args) throws Exception {
        // Take six command-line parameters
        if (args.length < 6) {
            print("You must give me six Pokemon to analyze");
            System.exit(-1);
        }

        // This bit of JDBC magic I provide as a free gift :-)
        // The rest is up to you.
        try (Connection con = DriverManager.getConnection("jdbc:sqlite:pokemon.db")) {
            for (String arg : args) {
                print("Analyzing " + arg);

                // Analyze the pokemon whose pokedex_number is in "arg"

                // You will need to write the SQL, extract the results, and compare
                // Remember to look at those "against_NNN" column values; greater than 1
                // means the Pokemon is strong against that type, and less than 1 means
                // the Pokemon is weak against that type
            }

            String answer = input("Would you like to save this team? (Y)es or (N)o: ");
            if (answer.equalsIgnoreCase("Y") || answer.equalsIgnoreCase("YES")) {
                String teamName = input("Enter the team name: ");

                // Write the pokemon team to the "teams" table
                print("Saving " + teamName + " ...");
            }
            else {
                print("Bye for now!");
            }
        }        
    }

    /*
     * These are here just to have some symmetry with the Python code
     * and to make console I/O a little easier. In general in Java you
     * would use the System.console() Console class more directly.
     */
    public static void print(String msg) {
        System.console().writer().println(msg);
    }

    /*
     * These are here just to have some symmetry with the Python code
     * and to make console I/O a little easier. In general in Java you
     * would use the System.console() Console class more directly.
     */
    public static String input(String msg) {
        return System.console().readLine(msg);
    }
}
