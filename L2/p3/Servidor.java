/*
 * Servidor.java
 *
 * Contiene el código para instanciar y publicar el objetoRemoto en la rmiregistry
 */
 
import java.rmi.Naming;                    /* lookup         */
import java.rmi.registry.Registry;         /* REGISTRY_PORT  */

/**
 * Servidor para el ejemplo de RMI.
 * Exporte un metodo para sumar dos enteros y devuelve el resultado.
 */
public class Servidor 
{
    
    /** Crea nueva instancia de Servidor rmi */
    public Servidor() {
        try 
        {
		// Se indica a rmiregistry donde están las clases.
		// Cambiar el paht al sitio en el que esté. Es importante
		// mantener la barra al final.
		/*	System.setProperty(
				"java.rmi.server.codebase",
				"file:/D:/users/javier/java/rmi_simple/src_servidor/");
		*/	
            // Se publica el objeto remoto
            InterfaceRemota objetoRemoto = new ObjetoRemoto();
			String rname = "//localhost:" + Registry.REGISTRY_PORT  + "/ObjetoRemoto";
            Naming.rebind (rname, objetoRemoto);
			
			InterfaceRemotaMD objetoRemotoMD = new ObjetoRemotoMD();
			String rnameMD = "//localhost:" + Registry.REGISTRY_PORT  + "/ObjetoRemotoMD";
            Naming.rebind (rnameMD, objetoRemotoMD);
            
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        new Servidor();
    }
}
