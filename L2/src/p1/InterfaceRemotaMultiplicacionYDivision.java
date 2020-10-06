package p1;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceRemotaMultiplicacionYDivision extends Remote{
	
	public int multiplicar (int a, int b) throws RemoteException; 
    public int dividir(int a, int b) throws RemoteException;
    
}
