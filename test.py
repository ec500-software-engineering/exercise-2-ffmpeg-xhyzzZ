from main import tranfer_video
import queue 
import pytest

def test_compute(genpat):
	q = queue.Queue()
	vid = str(genpat)
	q.put(vid)
	length = tranfer_video(q,vid)
	assert length == pytest.approx(1.)

if __name__ == '__main__':
	pytest.main(['-x',__file__])