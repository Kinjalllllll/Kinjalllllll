package chatapplication;


import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.sql.*;

public class LoginC extends JFrame{
private JTextField usernameField;
    private JPasswordField passwordField;
    private JButton loginButton;
    private JLabel usernameLabel, passwordLabel; 


    public LoginC() {
        setTitle("Chatty");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);
        setLocationRelativeTo(null);
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        
       
        usernameLabel = new JLabel("Username:");
        usernameField = new JTextField(20);
        passwordLabel = new JLabel("Password:");
        passwordField = new JPasswordField(20);
        loginButton = new JButton("Login");
        loginButton.setPreferredSize(new Dimension(255, 30));


       
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.insets = new Insets(5, 5, 5, 5);


       
        constraints.gridx = 0;
        constraints.gridy = 0;
        panel.add(usernameLabel, constraints);
        constraints.gridx = 1;
        panel.add(usernameField, constraints);

        constraints.gridx = 0;
        constraints.gridy = 1;
        panel.add(passwordLabel, constraints);
        constraints.gridx = 1;
        panel.add(passwordField, constraints); 
        constraints.gridx = 0;
        constraints.gridy = 2;
        constraints.gridwidth = 5;
        panel.add(loginButton, constraints);

        add(panel);

        
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = usernameField.getText();
                String password = new String(passwordField.getPassword());

                
                if (isValidCredentials(username, password)) {
                   
                   dispose();
                    Client cli = new Client();
                    cli.setVisible(true);
                    
                } else {
                    JOptionPane.showMessageDialog(LoginC.this, "Invalid username or password.", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        setVisible(true);
    }

    
    private boolean isValidCredentials(String username, String password) {
        try {
            Class.forName("com.mysql.cjdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/chatapp", "root", "");
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery("select * from login_c where username='" + username + "' and password='" + password + "'");
            if(rs.next()) {
                return true;
            } else {
                return false;
            }
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(LoginC.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SQLException ex) {
            Logger.getLogger(LoginC.class.getName()).log(Level.SEVERE, null, ex);
        }
        return false;
    }

    public static void main(String[] args) {
        new LoginC();
    }
}