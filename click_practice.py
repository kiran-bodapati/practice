import click


@click.command()
@click.option('--add',default=1)
def student(add):
    result=2+add
    click.echo(result)

if __name__=="__main__":
     student()
   