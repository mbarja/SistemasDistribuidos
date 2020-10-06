package rmisum;

import java.rmi.Naming;                    /* lookup         */
import java.rmi.registry.Registry;         /* REGISTRY_PORT  */

import java.net.MalformedURLException;     /* Exceptions...  */
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

/*
 * Ejemplo de cliente rmi 
*/
public class Cliente {
    
    /** Crea nueva instancia de Cliente */
    public Cliente(String alfa) 
    {
        try
        {
		// Lugar en el que está el objeto remoto.
		// Debe reemplazarse "localhost" por el nombre o ip donde está corriendo "rmiregistry".
		// Naming.lookup() obtiene el objeto remoto
	    String rname = "//" + alfa + ":" + Registry.REGISTRY_PORT + "/ObjetoRemoto";
            InterfaceRemota objetoRemoto = 
                (InterfaceRemota)Naming.lookup (rname);
            
            // Se realiza la suma remota.
            System.out.print ("2 + 3 = ");
            System.out.println (objetoRemoto.suma(2,3));
        } catch (MalformedURLException e) {
	    e.printStackTrace();
	} catch (RemoteException e) {
	    e.printStackTrace();
	} catch (NotBoundException e) {
	    e.printStackTrace();
	}
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        new Cliente(args[0]);
    }
    
}
