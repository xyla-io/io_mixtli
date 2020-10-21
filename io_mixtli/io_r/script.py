import moda
import json

from io_map import IOMap
from typing import List, Dict

class IORScript(IOMap):
  def run(self, script_path: str, run_args: List[str]) -> Dict[str, any]:
    process_arguments = [
      'rscript',
      '--vanilla',
      script_path,
      *run_args
    ]
    process_output = moda.process.run_process_output(
      run_args=process_arguments,
      shell=False
    )
    # TODO: handle the returncode, and stderr components of the tuple
    return json.loads(process_output[1])