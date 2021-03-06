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
     * Obtiene el producto de los numeros que le pasan y la devuelve.
     */
    public int multiplicar(int a, int b) 
    {
	    System.out.println ("Multiplicando " + a + " * " + b +"...");
        return a*b;
    }
	/**
     * Obtiene el cociente de los numeros que le pasan y la devuelve.
     */
    public int dividir(int a, int b) 
    {
	    System.out.println ("Dividiendo " + a + " / " + b +"...");
        return a/b;
    }
    
}
