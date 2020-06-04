import os.path


def user_picture1(request):
    """A view that is vulnerable to malicious file access."""
    filename = request.GET.get('p')
    # BAD: This could read any file on the file system
    data = open(filename, 'rb').read()
    return None


def user_picture2(request):
    """A view that is vulnerable to malicious file access."""
    base_path = '/server/static/images'
    filename = request.GET.get('p')
    # BAD: This could still read any file on the file system
    data = open(os.path.join(base_path, filename), 'rb').read()
    return None


def user_picture3(request):
    """A view that is not vulnerable to malicious file access."""
    base_path = '/server/static/images'
    filename = request.GET.get('p')
    #GOOD -- Verify with normalised version of path
    fullpath = os.path.normpath(os.path.join(base_path, filename))
    if not fullpath.startswith(base_path):
        raise ValueError("illegal request")
    data = open(fullpath, 'rb').read()
    return None
