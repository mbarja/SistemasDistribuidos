package p5;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.text.DecimalFormat;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;

public class Tabla extends JFrame {
	private DefaultTableModel dtm;

    public Tabla() {

        String[] columnNames = {"RoundTrip Delay", "Offset", "Offset estimado","Fecha y hora",};
        Object[][] datos = {};

        dtm = new DefaultTableModel(datos, columnNames);
        final JTable table = new JTable(dtm);

        table.setPreferredScrollableViewportSize(new Dimension(600, 200));
        table.getColumn(columnNames[0]).setPreferredWidth(50);
        table.getColumn(columnNames[1]).setPreferredWidth(50);
        table.getColumn(columnNames[2]).setPreferredWidth(100);
        table.getColumn(columnNames[3]).setPreferredWidth(100);
        
        DefaultTableCellRenderer centerRenderer = new DefaultTableCellRenderer();
        centerRenderer.setHorizontalAlignment( JLabel.CENTER );
        table.setDefaultRenderer(String.class, centerRenderer); 
        
        JScrollPane scrollPane = new JScrollPane(table);
        getContentPane().add(scrollPane, BorderLayout.CENTER);       
        addWindowListener(new WindowAdapter() {           
            public void windowClosing(WindowEvent e) {
                System.exit(0);               
            }
        });
        this.pack();
        this.setVisible(true);
    }
    
    public void AgregarNuevaFila(double roundTripDelay,double offset, String fecha) {
    	 // Agregar nueva fila
    	String offsetStr = new DecimalFormat("0.00").format(offset*1000);
    	String roundTripDelayStr = new DecimalFormat("0.00").format(roundTripDelay*1000);
    	String offsetEstimado = ObtenerOffsetEstimado(roundTripDelay, offset);
        Object[] newRow = {roundTripDelayStr, offsetStr, offsetEstimado,fecha};
        dtm.addRow(newRow);

    }

	private String ObtenerOffsetEstimado(double roundTripDelay, double offset) {
		String offsetEstimado="";
		double offsetMenor = offset-roundTripDelay;
		double offsetMayor = offset + roundTripDelay;
		String offsetMenorStr = new DecimalFormat("0.00").format(offsetMenor*1000);
		String offsetMayorStr = new DecimalFormat("0.00").format(offsetMayor*1000);
		offsetEstimado=offsetMenorStr+" <= O <= "+offsetMayorStr;
		return offsetEstimado;
	}
   
}