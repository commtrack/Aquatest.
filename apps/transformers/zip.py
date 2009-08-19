import os, tempfile, zipfile, tarfile, logging
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse

def get_zipfile(file_list):
    """
    Create a ZIP file on disk and transmit it in chunks of 8KB,                 
    without loading the whole file into memory.                                    
    """
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for file in file_list:
        file = file.encode("utf-8")
        if os.path.exists(file):
            archive.write(file, os.path.basename(file))
        else:
            logging.warn("zipfile could not find %s" % file)
    archive.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=commcarehq.zip'
    response['Content-Length'] = temp.tell()
    # this seek is required for 'response' to work
    temp.seek(0)    
    return response

def get_tarfile(file_list, output_file):
    """
    Create a tar file on disk                               
    """
    export_file = open( output_file, "w+b" )
    tar = tarfile.open(fileobj=export_file, mode="w")
    for file in file_list:
        tar.add(file, os.path.basename(file) )
    tar.close()
    wrapper = FileWrapper(export_file)
    response = HttpResponse(wrapper, content_type='application/tar')
    response['Content-Disposition'] = 'attachment; filename=commcarehq.tar'
    response['Content-Length'] = export_file.tell()
    # this seek is required for 'response' to work
    export_file.seek(0)    
    return response
