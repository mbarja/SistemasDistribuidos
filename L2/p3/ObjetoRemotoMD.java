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
	private static int resultadoUltimaOperacion=0;
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
    public synchronized int multiplicar(int a, int b) 
    {
		try{
			Thread currentThread = Thread.currentThread();
			System.out.println("id of the thread is " + currentThread.getId());
			System.out.println("resultadoUltimaOperacion " + resultadoUltimaOperacion);
			System.out.println ("Multiplicando " + a + " * " + b +"...");
			resultadoUltimaOperacion=a*b;
			Thread.sleep(5000);
			
		}catch(InterruptedException ex){
			System.out.println(ex.getMessage());
		}
			
        return resultadoUltimaOperacion;
    }
	/**
     * Obtiene el cociente de los numeros que le pasan y la devuelve.
     */
    public int dividir(int a, int b) 
    {
		try{
			Thread currentThread = Thread.currentThread();
			System.out.println("id of the thread is " + currentThread.getId());
			System.out.println("resultadoUltimaOperacion " + resultadoUltimaOperacion);
			System.out.println ("Dividiendo " + a + " / " + b +"...");
			Thread.sleep(5000);
		}catch(InterruptedException ex){
			System.out.println(ex.getMessage());
		}
        return a/b;
    }
    
}
