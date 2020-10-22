/*
 * Cliente.java
 *
 * Ejemplo de muy simple de rmi
 */

import java.rmi.Naming;                    /* lookup         */
import java.rmi.registry.Registry;         /* REGISTRY_PORT  */

import java.net.MalformedURLException;     /* Exceptions...  */
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

import java.util.Arrays;
import java.util.List;

/*
 * Ejemplo de cliente rmi 
*/
public class Cliente {
    private InterfaceRemota objetoRemoto;
	private InterfaceRemotaMD objetoRemotoMD;
    /** Crea nueva instancia de Cliente */
    public Cliente(String alfa) 
    {
        try
        {
			// Lugar en el que está el objeto remoto.
			// Debe reemplazarse "localhost" por el nombre o ip donde está corriendo "rmiregistry".
			// Naming.lookup() obtiene el objeto remoto
			String rname = "//" + alfa + ":" + Registry.REGISTRY_PORT + "/ObjetoRemoto";
            objetoRemoto = (InterfaceRemota)Naming.lookup (rname);
 
			String rnameMD = "//" + alfa + ":" + Registry.REGISTRY_PORT + "/ObjetoRemotoMD";
            objetoRemotoMD = (InterfaceRemotaMD)Naming.lookup (rnameMD);
            
        } catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (RemoteException e) {
			e.printStackTrace();
		} catch (NotBoundException e) {
			e.printStackTrace();
		}
    }
	
	public void sumar(String a, String b){
	try
        {
			System.out.print(a+" + "+b+"= ");
			System.out.println (objetoRemoto.suma(Integer.parseInt(a),Integer.parseInt(b)));
		} catch (RemoteException e) {
			e.printStackTrace();
		} 
		
	}
	
	public void restar(String a, String b){
	try
        {
			System.out.print(a+" - "+b+"= ");
			System.out.println (objetoRemoto.resta(Integer.parseInt(a),Integer.parseInt(b)));
		} catch (RemoteException e) {
			e.printStackTrace();
		} 
		
	}
	
	public void multiplicar(String a, String b){
	try
        {
			System.out.print(a+" * "+b+"= ");
			System.out.println (objetoRemotoMD.multiplicar(Integer.parseInt(a),Integer.parseInt(b)));
		} catch (RemoteException e) {
			e.printStackTrace();
		} 
		
	}
	public void dividir(String a, String b){
	try
        {
			System.out.print(a+" / "+b+"= ");
			System.out.println (objetoRemotoMD.dividir(Integer.parseInt(a),Integer.parseInt(b)));
		} catch (RemoteException e) {
			e.printStackTrace();
		} 
		
	}
	
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Cliente cliente = new Cliente(args[0]);
		
		String[] operaciones = new String[]{"R", "S", "M", "D", "F"};
		List<String> list = Arrays.asList(operaciones);
		boolean clienteActivo=true;
		
		while(clienteActivo){
			
			System.out.println("INGRESE UNA OPERACION S(suma), R(resta), M(multiplicacion), D(division), F(finalizar)"); 
			String operacion = System.console().readLine(); 
			if(operacion.equals("F")) clienteActivo=false;
			
			else if(list.contains(operacion)){
				
				System.out.println("Ingrese el primer numero"); 
				String a = System.console().readLine(); 
				System.out.println("Ingrese el segundo numero"); 
				String b = System.console().readLine(); 
				
				switch(operacion) 
				{ 
					case "S": 
						cliente.sumar(a,b);
						break; 
					case "R": 
						cliente.restar(a,b);
						break; 
					case "M": 
						cliente.multiplicar(a,b);
						break; 
					case "D": 
						cliente.dividir(a,b);
						break; 
					default: 
						System.out.println("operacion no valida"); 
				} 
			}else {
				System.out.println("operacion no valida"); 
			}
		}
		
    }
    
}
