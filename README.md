# veeam_solution

A small program that synchronizes 2 directories one way.

The program takes `in_folder` (source), `out_folder` (destination), `period` and `log_file` as arguments.
- `in_folder`: REQUIRED. The source directory of synchronization
- `out_folder`: REQUIRED. The contents of this directory will become identical to source
- `period`: REQUIRED. How often synchronization runs (in seconds)
- `log_file`: REQUIRED. Path to logfile. Logs are in addition printed to stdout

Usage: `python main.py in_folder out_folder period log_file`