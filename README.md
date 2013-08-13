Simply pip install it:

    sudo pip install -e git://github.com/PunchTab/geoip-dat.git@5230ff37d67f78749d1897ace6a67d47177731b7#egg=geoipdat

Then get the path to the dat file:

    import geoipdat
    geoipdat.get_path()

You can then use pygeoip:

    import pygeoip
    i4 = pygeoip.GeoIP(geoipdat.get_path(), pygeoip.MEMORY_CACHE)
    gi4.record_by_addr('24.130.13.49')
