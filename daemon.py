import util
import io
import datetime 
import shutil, os

class Synchronizer:
    """
    Class that synchronizes 2 folders.

    Contents of 'src' will NOT be changed.
    Contents of 'dst' will be replaced by contents of 'src'

    Call sync() to synchronize.
    
    Arguments:
        src: source diretory
        dst: destination directory
        log_file: opened file in text mode with write
    """
    src: str
    dst: str
    log_file: io.TextIOWrapper

    def __init__(self, src: str, dst: str, log_file: io.TextIOWrapper):
        self.src = src
        self.dst = dst
        self.log_file = log_file

    def sync(self):
        (in_folder, in_folder_list) = util.create_folder_hash_disctionary(self.src)
        (out_folder, out_folder_list)  = util.create_folder_hash_disctionary(self.dst)

        matched = list()
        overwrite = list()

        keys = list(in_folder.keys())

        for k in keys:
            if(out_folder.get(k)):
                #File exists in out, must check hash
                if (out_folder.get(k) == in_folder.get(k)):
                    #File hash matches, we can skip
                    matched.append(k)    
                else:
                    # Must overwrite, different version
                    overwrite.append(k)
                del out_folder[k]
                del in_folder[k]
            else:
                #File does not exists in out, must copy
                pass
        
        #Remaining files in 'in_folder' do not exists in 'out_folder'
        #Remaining files in 'out_folder' do not exists in 'in-folder'

        to_delete = out_folder_list - in_folder_list
        missing_folders = in_folder_list - out_folder_list

        self._create_dirs(missing_folders)
        self._do_deletes(list(out_folder.keys()), to_delete)
        self._do_copies(list(in_folder.keys()))
        self._do_copies(overwrite, True)
        self._do_already_synced(matched)

    def _do_deletes(self, files: list[str], folders: list[str]):
        """Deletes given and directories in the destination"""
        for file in files:
            os.remove(f'{self.dst}/{file}')
            self._log('DELETE', f'{self.dst}/{file}', 'File does not exist in the source directory')
            pass
        for folder in folders:
            try:
                shutil.rmtree(f'{self.dst}/{folder}')
                self._log('DELETE', f'{self.dst}/{folder}', 'Directory does not exist in the source directory')
            except FileNotFoundError:
                pass
            pass
    
    def _do_copies(self, files: list[str], overwrite = False):
        """
        Copies files from source to destination. Throws exception if the directory does not exist.

        Call 'create_dirs' first if the existence of directories can't be guaranteed
        """
        reason = 'File does not exist in the output directory'
        if overwrite:
            reason = 'File exists, hash mismatch'
        for file in files:
            shutil.copy(f"{self.src}/{file}", f"{self.dst}/{file}")
            self._log('COPY', f"{self.src}/{file}", reason)
            pass

    def _do_already_synced(self, files: list[str]):
        """Logs files that have the same hash in both directories"""
        for file in files:
            self._log('SKIP', f"{self.src}/{file}", 'File exists with matching hash')
            pass

    def _create_dirs(self, folders: set[str]):
        """Creates missing directories in the destination directory"""
        for folder in folders:
            f = f"{self.dst}/{folder}"
            try:
                os.makedirs(f)
                self._log('MKDIR', f, 'Directory does not exist in destination')
            except FileExistsError:
                pass
    
    def _log(self, op: str, path: str, reason: str):
        """
        Writes log.
        
        Arguments:
            op: Operation performed
            path: Path to the file on which the operation was performed
            reason: Why did this operation happen?
        """
        now = datetime.datetime.strftime(datetime.datetime.now(), "%b %d, %Y %H:%M:%S")
        msg = f"{now} - {op} {path} {reason}"
        print(msg)
        self.log_file.write(f"{msg}\n")

def runSynchronization(src: str, dst: str, period: int, log: io.TextIOWrapper):
    # TODO: timings (repeat every period)
    tmp = Synchronizer(src, dst, log)
    tmp.sync()