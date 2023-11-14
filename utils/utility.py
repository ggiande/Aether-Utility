import os
import subprocess
import tarfile
import shutil
import typing

from constants import Constants
from typing import List, Set, Dict
from rich.console import Console
from rich.table import Table


class Utility:
    """
    Utility stores functions used for logging, extracting, printing, and additional items
    """

    def __init__(self) -> None:
        """
        Special method that replaces a constructor/__new()__
        """

    @classmethod
    def get_abs_file_paths(cls, path: str) -> List[str]:
        os.chdir(path)
        file_paths = [os.path.join(path, filename) for filename in os.listdir(os.path.abspath(path)) if
                      os.path.isfile(filename)]
        return file_paths

    @classmethod
    def write_file(cls, filepath, file) -> None:
        with open(filepath, 'w') as written_file:
            written_file.writelines(file)
            written_file.close()

    @classmethod
    def read_file(cls, filepath) -> List[str]:
        with open(filepath, 'r') as file:
            file_lines_list = file.readlines()
            file.close()
            return file_lines_list

    @classmethod
    def replace_line(cls, file, replace_text, line_num) -> None:
        file[line_num] = file[line_num].replace(file[line_num].split("=")[1], replace_text)

    @classmethod
    def wmic_kill_java_processes(cls, cwd: str, shell: bool = True, verbose=True):
        """ Windows Management Instrumentation Command-line is a command line tool leveraged to kill processes """

        command = f"wmic process where \"name like '%java'\" delete"
        process = subprocess.Popen(command, cwd=cwd, shell=shell, stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            if not verbose:
                return
            print(line.decode(errors='ignore').strip('\r\n'))

    @classmethod
    def ps_kill_java_processes(cls, cwd: str, shell: bool = True, verbose=True):
        """ procps package on linux distros to kill processes """
        command = "pkill java"
        process = subprocess.Popen(command, cwd=cwd, shell=shell, stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            if not verbose:
                return
            print(line.decode(errors='ignore').strip('\r\n'))

    @classmethod
    def console_table(cls, title: str, rows=None, columns=None) -> None:
        if columns is None:
            columns = Constants.DEFAULT_ENTRY_COLUMNS.copy()
        if rows is None:
            rows = Constants.DEFAULT_ENTRY_ROW.copy()
        table = Table(title=title)
        rows = rows
        columns = columns
        for column in columns:
            table.add_column(column)
        for row in rows:
            table.add_row(*row, style='bright_green')
        console = Console()
        console.print(table)
