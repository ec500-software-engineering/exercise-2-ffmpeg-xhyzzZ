from pytest import approx
import subprocess


def test_duration():
    inp='test.mp4'
    out='480p_video1.mp4'
    outLen = subprocess.call(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',out])
    inLen  = subprocess.call(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',inp])
    assert inLen == approx(outLen)
