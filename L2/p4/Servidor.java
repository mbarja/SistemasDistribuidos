package p4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Random;


public class Servidor extends Thread{
	
	private final ServerSocket serverSocket;  
	private boolean clienteConectado=false;
    public Servidor(int puerto) throws IOException 
    {
        serverSocket = new ServerSocket(puerto);
    }

    public void run(){
        while (true){
            try {
                
                Socket server = serverSocket.accept(); 
                clienteConectado=true;
                DataInputStream in = new DataInputStream(server.getInputStream());
                DataOutputStream out = new DataOutputStream(server.getOutputStream());
                while(clienteConectado) {
	                //lee el codigo que envía el cliente.
	                int i=in.readInt();
	                //si es 1, duerme y envía su hora.
	                if(i==1)
	                	{
	                		Thread.sleep((long)(100+new Random().nextInt(51)));
	                		out.writeLong(System.currentTimeMillis());  
	                	}
	                //si es distinto de 1, el cliente finaliza las consultas
	                else clienteConectado=false;
                }
                server.close();
            } catch (UnknownHostException ex) {
                System.out.println(ex.getMessage());
            } catch (IOException | InterruptedException ex) {
           	 System.out.println(ex.getMessage());
           }
        }
    }
    
    public static void main(String[] args) throws IOException 
    {
        int puerto = 1333;
        Thread t = new Servidor(puerto); 
        t.start();
    }
	
}
