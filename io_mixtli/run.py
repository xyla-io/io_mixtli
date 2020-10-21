import click

from . import io_r
from pathlib import Path
from typing import Tuple

class Mixtli:
  use_the_force: bool
  
  def __init__(self, use_the_force: bool):
    self.use_the_force = use_the_force

@click.group()
@click.option('--use-the-force', 'use_the_force', is_flag=True)
@click.pass_context
def run(ctx: any, use_the_force: bool):
  ctx.obj = Mixtli(use_the_force=use_the_force)
  print(f'Running, using the force: {ctx.obj.use_the_force}')

@run.command()
@click.argument('path', type=click.Path(file_okay=True, dir_okay=False, readable=True))
@click.argument('run_args', nargs=-1)
@click.pass_obj
def r(mixtli: Mixtli, path: click.Path, run_args: Tuple[str]):
  script = io_r.IORScript()
  output = script.run(
    script_path=path,
    run_args=list(run_args)
  )
  print(f'Ran {path} with output:\n\n {output}')

@run.group()
@click.pass_obj
def model(mixtli: Mixtli):
  print(f'--> "model" command...')

@model.command()
@click.pass_obj
def media_mix(mixtli: Mixtli):
  print(f'----> "media-mix" command...')