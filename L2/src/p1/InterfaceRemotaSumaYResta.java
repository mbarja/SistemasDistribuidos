package p1;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceRemotaSumaYResta extends Remote {
    public int suma (int a, int b) throws RemoteException; 
    
    public int resta(int a, int b) throws RemoteException;
}