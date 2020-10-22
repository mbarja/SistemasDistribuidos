/*
 * ObjetoRemoto.java
 */
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
/**
 * Objeto que implementa la interfaz remota
 */
public class ObjetoRemotoMD extends UnicastRemoteObject implements InterfaceRemotaMD
{
    /**
     * Construye una instancia de ObjetoRemoto
     * @throws RemoteException
     */
    protected ObjetoRemotoMD () throws RemoteException
    {
        super();
    }

    /**
     * Obtiene la suma de los sumandos que le pasan y la devuelve.
     */
    public int multiplicar(int a, int b) 
    {
	    System.out.println ("Multiplicando " + a + " * " + b +"...");
        return a*b;
    }
	/**
     * Obtiene la suma de los sumandos que le pasan y la devuelve.
     */
    public int dividir(int a, int b) 
    {
	    System.out.println ("Dividiendo " + a + " / " + b +"...");
        return a/b;
    }
    
}
