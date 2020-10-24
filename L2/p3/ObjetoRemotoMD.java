/*
 * ObjetoRemoto.java
 */
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.lang.*;
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
		try{
			Thread currentThread = Thread.currentThread();
			System.out.println("id of the thread is " + currentThread.getId());
			Thread.sleep(10000);
		}catch(InterruptedException ex){
			System.out.println(ex.getMessage());
		}
        return a*b;
    }
	/**
     * Obtiene el cociente de los numeros que le pasan y la devuelve.
     */
    public int dividir(int a, int b) 
    {
	    System.out.println ("Dividiendo " + a + " / " + b +"...");
		try{
			Thread currentThread = Thread.currentThread();
			System.out.println("id of the thread is " + currentThread.getId());
			Thread.sleep(10000);
		}catch(InterruptedException ex){
			System.out.println(ex.getMessage());
		}
        return a/b;
    }
    
}
