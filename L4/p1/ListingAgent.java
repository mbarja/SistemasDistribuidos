package examples.ListingAgent;
import jade.core.*;
import java.io.*;
import jade.core.behaviours.CyclicBehaviour;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.*; 
import java.lang.management.ManagementFactory;
import com.sun.management.OperatingSystemMXBean;
import java.net.*;
import java.text.*;

public class ListingAgent extends Agent
{
	String strdir = "C:\\Users\\Lala\\Documents\\SD2020";                // Dir to list
	String[] list;
	Map<String, String> map = new HashMap<String, String>();
	ContainerID destino = null;
	Location origen = null;
	long tsInicio=0;
	long tsFin=0;
	public void setup()
	{
		tsInicio=System.currentTimeMillis();
		System.out.println("Se crea al agente --> " + getName());
		// inicializa origen y destino
		destino = new ContainerID("Container-1", null);
		System.out.println("Destino --> " + destino.getID());
		origen = here();
		System.out.println("Origen --> " + origen.getID());
		// registra el comportamiento deseado del agente
		addBehaviour(new CyclicBehaviour(this){
			public void action() {
				switch(_state){
				case 0:
				// Comienza la migración del agente al destino
					_state++;
					System.out.println("Estado 0 Comienza la migración del agente al destino --> " + destino.getID());
					
					try {
						Thread.sleep(10000);
						doMove(destino);
						System.out.println("Despues de doMove en CyclicBehaviour de Estado 0 --> " + destino.getID());
					} catch (Exception e) {
						System.out.println("fallo al moverse al Container destino");
						e.getMessage();
					}
					break;
				case 1:
				// el agente llegó al destino, recupera el directorio y regresa
					_state++;
					System.out.println("Estado 1 agente llegó a destino, recupera directorio y regresa a --> " + origen.getID());
					System.out.println("**********************************SE ESTA EJECUTANDO EL AGENTE *******************************************");
					long tsLlegada=System.currentTimeMillis();
					
					try {
						
						OperatingSystemMXBean bean = (com.sun.management.OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
						Thread.sleep(10000);
						map.put("Id", here().getID());
						Date d = new Date(tsLlegada);
						DateFormat df = new SimpleDateFormat("dd/MM/yy HH:mm:ss");
						map.put("Fecha y hora", df.format(d));
						map.put("RAM total", String.valueOf(bean.getTotalMemorySize()));
						map.put("RAM libre", String.valueOf(bean.getFreeMemorySize()));
						map.put("OS", System.getProperty("os.name"));
						
					} catch (Exception e) {
						System.out.println("Falló al recuperar directorio dir.list()");
						e.getMessage();
					}
					// regresa al origen e imprime el directorio
					try {
						System.out.println("regresando a --> " + origen.getID());
						doMove(origen);
						System.out.println("despues de domove en CyclicBehaviour estado 1 --> " + here().getID());
					} catch (Exception e) {
						System.out.println("Falla al mover al regresar al origen"); 
						e.getMessage();
					}
					break;
				case 2:
					System.out.println("**********************************RESULTADOS *******************************************");
					tsFin=System.currentTimeMillis();
					System.out.println("*************** Duracion del recorrido: "+(tsFin-tsInicio)+"(ms)");
					// destruye al agente
					Iterator it = map.entrySet().iterator();
					while (it.hasNext()) {
						Map.Entry pair = (Map.Entry)it.next();
						System.out.println("*************** "+pair.getKey() + " = " + pair.getValue());
						it.remove(); // avoids a ConcurrentModificationException
					}
					
					System.out.println("destruye al agente --> " + getName());
					doDelete();
					break;
				default:
					myAgent.doDelete();
				}
			}
			private int _state = 0; // variable de máquina de estados del agente
		});

		// registra un comportamiento dummy a los efectos de verificar concurrencia y movilidad
		addBehaviour(new CyclicBehaviour(this){
        
			public void action() 
			{
				// arranca muestra cartel, duerme 5 segundos y muestra otro cartel
				_contador++;
				System.out.println("Behaviour dummy antes de dormir ciclo--> " + _contador + " --> " + here().getID());
				try {
					Thread.sleep(5000);
				} catch (InterruptedException ex) {
					Logger.getLogger(ListingAgent.class.getName()).log(Level.SEVERE, null, ex);
				}
				System.out.println("Behaviour dummy despues de dormir ciclo--> " + _contador + " --> " + here().getID());
			}

			private int _contador = 0; // cuenta la cantidad de ciclos en que se ejecuta el comportamiento
	     
		});
	}

	// Luego de ser movido el agente ejecuta este código
	protected void afterMove() {
		System.out.println("Siempre ejecuta afterMove cuando al llegar --> " + here().getID());
	}
}


