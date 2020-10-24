/*
 * InterfaceRemota.java
 *
 */

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Interface remota con los métodos que se pueden llamar en remoto
 */
public interface InterfaceRemotaMD extends Remote {
    public int multiplicar (int a, int b) throws RemoteException; 
	public int dividir (int a, int b) throws RemoteException;
}