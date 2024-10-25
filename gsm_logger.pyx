# gsm_logger.pyx
from libc.stdio cimport fopen, fprintf, fclose

cdef class GSMLogger:
    cdef:
        FILE* logfile
    
    def __cinit__(self, filename):
        self.logfile = fopen(filename.encode('utf-8'), "a")
        if not self.logfile:
            raise IOError("Failed to open log file")

    def log_message(self, msg):
        if self.logfile:
            fprintf(self.logfile, b"Received GSM message: %s\n", msg.encode('utf-8'))

    def __dealloc__(self):
        if self.logfile:
            fclose(self.logfile)