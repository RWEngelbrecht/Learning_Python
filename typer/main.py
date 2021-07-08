import typer

app = typer.Typer()

@app.command()
def hello(name:str=typer.Argument('World'), secret:bool=False):
  print(f'Hello {name}!')
  if secret: print(f'This is secret string you need flag to see')

@app.command()
def bye():
  print('Goodbye cruel world!')


if __name__ == "__main__":
  app()