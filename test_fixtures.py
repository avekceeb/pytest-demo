from pytest import fixture, skip


NFS_VERSIONS = ('3', '4.2')
NFS_VERSIONS_NAMES = [f'NFSv{x}' for x in NFS_VERSIONS]


@fixture(scope="module", params=NFS_VERSIONS, ids=NFS_VERSIONS_NAMES)
def nfs_versions(request):
    yield request.param


def test_fixture(nfs_versions):
    assert nfs_versions in NFS_VERSIONS
