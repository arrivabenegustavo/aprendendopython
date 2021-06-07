'''
Esta exemplo faz parte de HERANÇA MÚLTIPLA, JUNTO COM ARQUIVO LOG.LOG
'''

class LogMixin:
    @staticmethod
    def write(msg):
        with open('Log.log', 'a+') as f:
            f.write(f'{msg}\n')
            
            
    def log_info(self, msg):
        self.write(f'INFO: {msg}')
        
    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
         
 
        

