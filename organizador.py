import os;
import shutil;

from lib import Arquivos

if __name__ == "__main__":
	for documento in Arquivos.ListarArquivos('.\\files\\','docx'):
	    print('Copiando ' + documento)
	    retorno = Arquivos.CopiarArquivo(os.path.basename(documento),os.path.dirname(documento), '.\\files\\documentos')
	    if retorno == -1:
	        print('Erro na cópia dos documentos')
	        
	for documento in Arquivos.ListarArquivos('.\\files\\','xlsx'):
	    print('Copiando ' + documento)
	    retorno = Arquivos.CopiarArquivo(os.path.basename(documento),os.path.dirname(documento), '.\\files\\planilhas')
	    if retorno == -1:
	        print('Erro na cópia das planilhas')