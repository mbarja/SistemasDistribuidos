package p4;
import java.awt.Font;
import java.awt.Color;
import java.awt.GridLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import java.util.*;
import java.text.*;
 
public class Reloj {
	ClockLabel dateLable;
	ClockLabel timeLable;
	ClockLabel dayLable;
	
		
	public Reloj (long horaInicial) {
		
		dateLable = new ClockLabel("date");
	    timeLable = new ClockLabel("time");
	    dayLable = new ClockLabel("day");
	 
	    JFrame.setDefaultLookAndFeelDecorated(true);
	    JFrame f = new JFrame("Reloj del Cliente");
	    f.setSize(300,150);
	    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    f.setLayout(new GridLayout(3, 1));
	 
	    f.add(dateLable);
	    f.add(timeLable);
	    f.add(dayLable);
	 
	    f.getContentPane().setBackground(Color.black);
	 
	    f.setVisible(true);
	    
	    ActualizarHora(horaInicial);
	}
	
	public void ActualizarHora(long timer) {
		this.dateLable.ActualizarHora(timer);
		this.dayLable.ActualizarHora(timer);
		this.timeLable.ActualizarHora(timer);
	}
 
}
 
class ClockLabel extends JLabel{
 
  String type;
  SimpleDateFormat sdf;
 
  public ClockLabel(String type) {
    this.type = type;
    setForeground(Color.green);
 
    switch (type) {
      case "date" : sdf = new SimpleDateFormat("  MMMM dd yyyy");
                    setFont(new Font("sans-serif", Font.PLAIN, 12));
                    setHorizontalAlignment(SwingConstants.LEFT);
                    break;
      case "time" : sdf = new SimpleDateFormat("hh:mm:ss a");
                    setFont(new Font("sans-serif", Font.PLAIN, 40));
                    setHorizontalAlignment(SwingConstants.CENTER);
                    break;
      case "day"  : sdf = new SimpleDateFormat("EEEE  ");
                    setFont(new Font("sans-serif", Font.PLAIN, 16));
                    setHorizontalAlignment(SwingConstants.RIGHT);
                    break;
      default     : sdf = new SimpleDateFormat();
                    break;
    }
 
  }
 
  public void ActualizarHora(long timer) {
    Date d = new Date(timer);
    setText(sdf.format(d));
  }

}