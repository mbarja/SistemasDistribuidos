/*
 * ObjetoRemoto.java
 */
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.lang.*;
/**
 * Objeto que implementa la interfaz remota
 */
public class ObjetoRemoto extends UnicastRemoteObject implements InterfaceRemota
{
    /**
     * Construye una instancia de ObjetoRemoto
     * @throws RemoteException
     */
    protected ObjetoRemoto () throws RemoteException
    {
        super();
    }

    /**
     * Obtiene la suma de los sumandos que le pasan y la devuelve.
     */
    public int suma(int a, int b) 
    {
	    System.out.println ("Sumando " + a + " + " + b +"...");
		try{
			Thread currentThread = Thread.currentThread();
			System.out.println("id of the thread is " + currentThread.getId());
			Thread.sleep(10000);
		}catch(InterruptedException ex){
			System.out.println(ex.getMessage());
		}
        return a+b;
    }
	/**
     * Obtiene la resta de los numeros que le pasan y la devuelve.
     */
    public int resta(int a, int b) 
    {
	    System.out.println ("Restando " + a + " + " + b +"...");
		Thread currentThread = Thread.currentThread();
		System.out.println("id of the thread is " + currentThread.getId());
		
        return a-b;
    }
    
}
