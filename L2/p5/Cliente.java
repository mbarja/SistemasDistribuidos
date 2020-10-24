package p5;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.text.DecimalFormat;
import java.util.Scanner;

public class Cliente {
	private Tabla tabla;
	
	public Cliente () {
		this.tabla = new Tabla();
	}

	public static void main(String[] args) throws IOException
	{
		
		Cliente cliente = new Cliente();
		System.out.println("Cliente Iniciado");
		while(true){
			System.out.println("****************************");
			System.out.println("Ingrese el servidor NTP a consultar");
			Scanner sc = new Scanner(System.in);
			String servidorNTP = sc.nextLine();
			for(int j=1;j<9;j++)
	        {
				try {
					Thread.sleep(5000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				System.out.println("****************************");
				System.out.println("Consulta "+j);
				cliente.ConsultarAlServidor(servidorNTP);
	        }
		}
	}
	
	private void ConsultarAlServidor(String serverName) {
		// Send request
		DatagramSocket socket;
		try {
			socket = new DatagramSocket();
			InetAddress address = InetAddress.getByName(serverName);
			byte[] buf = new NtpMessage().toByteArray();
			DatagramPacket packet = new DatagramPacket(buf, buf.length, address, 123);
			
			// Set the transmit timestamp *just* before sending the packet
			// ToDo: Does this actually improve performance or not?
			NtpMessage.encodeTimestamp(packet.getData(), 40,(System.currentTimeMillis()/1000.0) + 2208988800.0);
			
			socket.send(packet);
			
			// Get response
			System.out.println("NTP request sent, waiting for response...\n");
			packet = new DatagramPacket(buf, buf.length);
			socket.receive(packet);
			
			// Immediately record the incoming timestamp
			double destinationTimestamp =(System.currentTimeMillis()/1000.0) + 2208988800.0;
			
			
			// Process response
			NtpMessage msg = new NtpMessage(packet.getData());
			
			// Corrected, according to RFC2030 errata
			double roundTripDelay = (destinationTimestamp-msg.originateTimestamp) -
				(msg.transmitTimestamp-msg.receiveTimestamp);
				
			double localClockOffset =
				((msg.receiveTimestamp - msg.originateTimestamp) +
				(msg.transmitTimestamp - destinationTimestamp)) / 2;
			// Display response
			System.out.println("NTP server: " + serverName);
			System.out.println(msg.toString());
			
			System.out.println("Dest. timestamp:     " +
				NtpMessage.timestampToString(destinationTimestamp));
			
			System.out.println("Round-trip delay: " +
				new DecimalFormat("0.00").format(roundTripDelay*1000) + " ms");
			
			System.out.println("Local clock offset: " +
				new DecimalFormat("0.00").format(localClockOffset*1000) + " ms");
		
			socket.close();
			
			tabla.AgregarNuevaFila(roundTripDelay/2,localClockOffset, NtpMessage.timestampToString(msg.receiveTimestamp), serverName);
			
		} catch (SocketException e) {
			e.printStackTrace();
		} catch (UnknownHostException e) {
			e.printStackTrace();
		}catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}
}
