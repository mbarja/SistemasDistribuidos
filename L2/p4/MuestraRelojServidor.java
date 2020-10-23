package p4;

public class MuestraRelojServidor {
	private long horaCliente;
	private long retardo;
	private long horaServidor;
	
	public MuestraRelojServidor(long horaCliente, long retardo, long horaServidor) {
		this.horaCliente=horaCliente;
		this.retardo=retardo;
		this.horaServidor=horaServidor;
		System.out.println("horaCliente: "+this.horaCliente+" retardo: "+this.retardo+" horaServidor: "+this.horaServidor);
	}

	public long getHoraCliente() {
		return horaCliente;
	}

	public void setHoraCliente(long horaCliente) {
		this.horaCliente = horaCliente;
	}

	public long getRetardo() {
		return retardo;
	}

	public void setRetardo(long retardo) {
		this.retardo = retardo;
	}

	public long getHoraServidor() {
		return horaServidor;
	}

	public void setHoraServidor(long horaServidor) {
		this.horaServidor = horaServidor;
	}
	
	public long ObtenerHoraRealDelServidor(){
		return this.horaServidor+(this.retardo/2);
	}

}
