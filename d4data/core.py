
def download(source, dest=None):
    """ Downloads datasource from uri to local path; will take arguments- and set object attributes to those arguments- or default to objects attributes."""
    if dest:
        source.local_url = dest
    return source.client.download(source.remote_url, source.local_url)

def upload(source, dest=None):
    """ Upload local to uri (dest=None) or some other dest"""
    if not dest:
        dest = source.remote_url
    return source.client.upload(source.local_url, dest)

def send(source, dest, src="remote"):
    if src == "remote":
        src = source.remote_url
    elif src == "local":
        src = source.local_url
    else:
        raise Exception("src must be either local or remote")
    return source.client.send(src, dest)
