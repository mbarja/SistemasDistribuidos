package p4;
import java.net.*;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Scanner;

import java.io.*;

public class Cliente {
	 public static SimpleDateFormat SDF = new SimpleDateFormat("HH:mm:ss"); 
	 public static long Timer; 
	 public static long Deriva;
	 private static String serverName;
	 private static int serverPort;
	 
	 public static class RelojCliente extends Thread 
	    {
		 Reloj relojDigital;
	      
	        public RelojCliente(long derivaIngresada)  
	        {
	            Deriva=derivaIngresada;
	            //Seteo hora actual - 10 minutos
	            Timer = System.currentTimeMillis()-600000;
	            relojDigital = new Reloj(Timer);
	            
	        }
	        public void run()
	        {
	            
	            while(true)
	            {
	                try 
	                    {
	                        Thread.sleep(Deriva);    
	                        Timer+=1000;  
	                        relojDigital.ActualizarHora(Timer);
	                        System.out.println(SDF.format(Timer)); 
	                
	                    } 
	                catch (InterruptedException ex) 
	                    {
	                		System.out.println(ex.getMessage());
	                    }
	            }
	        }
	    }
	 
	 public Cliente(String serverName, int serverPort) {
	    	
	        this.serverName = serverName;
	        this.serverPort = serverPort;
	        
	  }
	 
	 public static class ActualizarHora  
	 {
	        public void run() throws IOException
	        {
	        	System.out.println("ActualizarHora");
	        	ArrayList<MuestraRelojServidor> muestrasDelServidor = new ArrayList<MuestraRelojServidor>();
	        	long tsEnvio;
	        	long tsRecepcion;
	            Socket client;
	            client = new Socket(serverName, serverPort);
	            OutputStream outToServer = client.getOutputStream();
	            DataOutputStream out = new DataOutputStream(outToServer);
	            InputStream inFromServer = client.getInputStream();
	            DataInputStream in = new DataInputStream(inFromServer);
	            for(int j=0;j<5;j++)
	            {
	            	tsEnvio=System.currentTimeMillis();
	            	out.writeInt(1);
		            long horaServer = in.readLong();
		            tsRecepcion=System.currentTimeMillis();
		            long retardo = (tsRecepcion-tsEnvio);
		            muestrasDelServidor.add(new MuestraRelojServidor(Timer,retardo, horaServer));
	           
	            }
	            out.writeInt(2);
	            client.close();
	            ObtenerDiferenciaYActualizarDeriva(muestrasDelServidor);
	        }

			private void ObtenerDiferenciaYActualizarDeriva(ArrayList<MuestraRelojServidor> muestrasDelServidor) {
				MuestraRelojServidor muestraDeMenorRetardo = ObtenerMuestraDeMenorRetardo(muestrasDelServidor);
				long horaDelServidor = muestraDeMenorRetardo.ObtenerHoraRealDelServidor();
				
				System.out.println("horaCliente: "+muestraDeMenorRetardo.getHoraCliente());
				System.out.println("horaServidor: "+horaDelServidor);
				//Si la hora del cliente es mayor a la del servidor, debo agrandar la deriva
				System.out.println(Deriva);
				if(muestraDeMenorRetardo.getHoraCliente()>horaDelServidor) {
					Deriva*=2;
				}
				//Si la hora del cliente es menor a la del servidor, debo achicar la deriva
				if(muestraDeMenorRetardo.getHoraCliente()<horaDelServidor) {
					Deriva/=2;
				}
				//Si la hora del cliente es igual a la del servidor, dejo la deriva en 1 segundo
				if(muestraDeMenorRetardo.getHoraCliente()==horaDelServidor) {
					Deriva=1000;
				}
				System.out.println(Deriva);
				
			}

			private MuestraRelojServidor ObtenerMuestraDeMenorRetardo(ArrayList<MuestraRelojServidor> muestrasDelServidor) {
				MuestraRelojServidor muestraDeMenorRetardo=null;
				for(MuestraRelojServidor muestra: muestrasDelServidor){
					if(muestraDeMenorRetardo==null) {
						muestraDeMenorRetardo=muestra;
					}
					if(muestra.getRetardo()<muestraDeMenorRetardo.getRetardo()) {
						muestra=muestraDeMenorRetardo;
					}
				}
				System.out.println("la muestra mas chica es: "+muestraDeMenorRetardo.getRetardo());
				
				return muestraDeMenorRetardo;
			}
	   }
	 
	 
	 public static void main(String[] args) throws InterruptedException, IOException
	    {
	        Scanner sc = new Scanner(System.in);
	        long deriva;
	        System.out.println("Ingrese la deriva inicial (ms)");
	        deriva = sc.nextLong();
	        String serverName = "localhost";
	        int serverPort = 1333;
	        Cliente client = new Cliente(serverName, serverPort);
	        Cliente.RelojCliente relojCliente = new RelojCliente(deriva);
	        Cliente.ActualizarHora actualizarHora = new ActualizarHora();
	     
	        System.out.println("Cada cuanto se deberá actualizar el reloj (ms)?");
	        long CC=sc.nextLong();
	        relojCliente.start();
	        while(true)
	        {
	            Thread.sleep(CC);
	            actualizarHora.run();
	        }
	    }

}
