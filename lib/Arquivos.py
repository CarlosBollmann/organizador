import os;
import shutil;

def ListarArquivos(path, extension):
    caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    docs = [arq for arq in arquivos if arq.lower().endswith(extension)]
    return docs

def CopiarArquivo(file,path_source,path_dest):
    try:
        source = os.path.join(path_source,file)
        dest = os.path.join(path_dest,file)
        
        shutil.copy(source,dest)
        return 0
    except:
        return -1
