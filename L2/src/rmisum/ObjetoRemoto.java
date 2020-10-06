/*
 * ObjetoRemoto.java
 */
package rmisum;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * Objeto que implementa la interfaz remota
 */
public class ObjetoRemoto extends UnicastRemoteObject 
    implements InterfaceRemota
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
        return a+b;
    }
    
}
