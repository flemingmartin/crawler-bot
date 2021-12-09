import threading

class StoppableThread(threading.Thread):
    '''
        Implementación de Clase Thread con la posibilidad de ser detenido.
        Cuenta con un metodo stop() y un metodo de chequeo stopped()
        Hereda de threading.Thread
    '''

    def __init__(self,  *args, **kwargs):
        '''
            Constructor de la clase StoppableThread
        '''
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        '''
            Función que produce el evento de stop
        '''
        self._stop_event.set()

    def stopped(self):
        '''
            Función de chequeo del evento de stop
            Devuelve
            --------
                True:   si el evento stop se produjo
                False:  si el evento stop no se produjo
        '''
        return self._stop_event.is_set()