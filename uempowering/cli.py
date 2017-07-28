import os
import json
import click
from uempowering import Empowering

config = {
    'url': os.getenv('EMPOWERING_URL', None),
    'key': os.getenv('EMPOWERING_KEY_FILE', None),
    'cert': os.getenv('EMPOWERING_CERT_FILE', None),
    'company_id': os.getenv('EMPOWERING_COMPANY_ID', None),
    'username': os.getenv('EMPOWERING_USERNAME', None),
    'password': os.getenv('EMPOWERING_PASSWORD', None)
}

@click.group()
@click.pass_context
def uempowering(ctx):
    try:
        ctx.obj['emp'] = Empowering(ctx.obj['config'], debug=False)
    except Exception, e:
        click.echo('Empowering service connection failed')

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
@click.option('--match', default=None)
def get_contract(ctx, ids, match):
    if not ids: 
        click.echo(json.dumps(ctx.obj['emp'].get_contract([], match), indent=4))
    for id in list(ids):
        click.echo(json.dumps(ctx.obj['emp'].get_contract(id, match), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_measurements(ctx, ids):
   for id in list(ids):
       click.echo(json.dumps(ctx.obj['emp'].get_dh_measurements_by_contract(id), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ot', nargs=1)
@click.argument('ids', nargs=-1)
@click.option('--start', default=None)
@click.option('--end', default=None)
def get_contract_results(ctx, ot, ids, start, end):
   for id in list(ids):
       click.echo(json.dumps(ctx.obj['emp'].get_results_by_contract(ot, id, start, end), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_contract_stats(ctx, ids):
    click.echo("min_measures Minimum value of the month")
    click.echo("max_measures Maximun value of the month")
    click.echo("count_measures Number of values")
    click.echo("power Contracted power")
    click.echo("sum_measures Sum of monthly measures")
    for id in list(ids):
        click.echo(json.dumps(ctx.obj['emp'].get_contract_stats(id), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_contract_errors(ctx, ids):
    for id in list(ids):
        click.echo(json.dumps(ctx.obj['emp'].get_contract_errors(id), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_contract_errors(ctx, ids):
    for id in list(ids):
        click.echo(json.dumps(ctx.obj['emp'].get_contract_errors(id), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ot', nargs=1)
@click.option('--start', default=None)
@click.option('--end', default=None)
def get_ot_status(ctx, ot, start, end):
    click.echo(json.dumps(ctx.obj['emp'].get_ot_status(ot, start, end), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_measurements(ctx, ids):
   for id in list(ids):
       click.echo(json.dumps(ctx.obj['emp'].get_dh_measurements_by_contract(id), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_tariffs(ctx, ids):
    if not ids:
       click.echo(json.dumps(ctx.obj['emp'].get_tariffs([]), indent=4))
    for id in list(ids):
    
        print id
        click.echo(json.dumps(ctx.obj['emp'].get_tariffs(id), indent=4))

@uempowering.command()
@click.pass_context
@click.option('--item', type=(unicode, unicode), multiple=True)
def get_time_slots(ctx, item):
    if not item:
       click.echo(json.dumps(ctx.obj['emp'].get_time_slots([]), indent=4))
    for tariff_id,name in list(item):
        click.echo(json.dumps(ctx.obj['emp'].get_time_slots(tariff_id=tariff_id,name=name), indent=4))

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def delete_contract(ctx, ids):
    for id in list(ids):
        click.echo(json.dumps(ctx.obj['emp'].delete_contract(id), indent=4))

if __name__ == '__main__':
    uempowering(obj={'config': config})
