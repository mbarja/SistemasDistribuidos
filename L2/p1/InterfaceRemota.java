/*
 * InterfaceRemota.java
 *
 */

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Interface remota con los métodos que se pueden llamar en remoto
 */
public interface InterfaceRemota extends Remote {
    public int suma (int a, int b) throws RemoteException; 
	public int resta (int a, int b) throws RemoteException;
}
