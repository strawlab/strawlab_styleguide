import os, sys, subprocess, pickle
import matplotlib
import matplotlib.font_manager as fmanager

def is_ubuntu():
    if not sys.platform.startswith('linux'):
        return False
    release = subprocess.check_output('lsb_release --id --short', shell=True)\
              .lower().strip()
    return release=='ubuntu'

def have_ttf_in_cache( mstpath ):
    found_ms_ttf = False
    if fmanager.fontManager is not None:
        for ttffile in fmanager.fontManager.ttffiles:
            if ttffile.startswith( mstpath ):
                found_ms_ttf = True
                break
    return found_ms_ttf

def verify_ms_fonts_on_ubuntu():
    assert is_ubuntu()

    # verify we have the MS fonts installed -------------
    pkg = 'ttf-mscorefonts-installer'
    try:
        subprocess.check_call('dpkg -s %s'%pkg, stdout=open('/dev/null','w'),
                              shell=True)
    except subprocess.CalledProcessError, err:
        raise RuntimeError(
            'system package missing. do this: apt-get install %s'%pkg)

    # ensure they are in current font path
    mstpath = '/usr/share/fonts/truetype/msttcorefonts'
    assert os.path.exists(mstpath)

    if not have_ttf_in_cache( mstpath ):
        if hasattr(fmanager,'_rebuild'):
            # extend ttf path to include MS fonts
            orig_ttfpath = os.environ.get('TTFPATH',None)
            if orig_ttfpath is not None:
                newpath = os.pathsep.join((orig_ttfpath, mstpath ))
            else:
                newpath = mstpath
            os.environ['TTFPATH'] = newpath

            # rebuild the cache
            matplotlib.font_manager._rebuild()
            assert have_ttf_in_cache( mstpath )

def setup_defaults():
    rcParams = matplotlib.rcParams
    rcParams['svg.fonttype'] = 'none' # No text as paths. Assume font installed.

    rcParams['font.serif'] = ['Times New Roman']
    rcParams['font.sans-serif'] = ['Arial']
    rcParams['font.family'] = 'sans-serif'

    if is_ubuntu():
        verify_ms_fonts_on_ubuntu()
