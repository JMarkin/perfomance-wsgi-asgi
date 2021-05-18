import click
import os
import signal

NUM_WORKERS = 2 * 2 + 1


@click.group()
def cli():
    pass


@cli.command()
def falcon_wsgi_bjoern():
    import bjoern

    from app import falcon_wsgi_app

    worker_pids = []

    bjoern.listen(falcon_wsgi_app, "0.0.0.0", 8000)
    for _ in range(NUM_WORKERS):
        pid = os.fork()
        if pid > 0:
            # in master
            worker_pids.append(pid)
        elif pid == 0:
            # in worker
            try:
                bjoern.run()
            except KeyboardInterrupt:
                pass
            exit()

    try:
        for _ in range(NUM_WORKERS):
            os.wait()
    except KeyboardInterrupt:
        for pid in worker_pids:
            os.kill(pid, signal.SIGINT)


if __name__ == '__main__':
    cli()
