import dill
import numpy as np

nemt = {'hello' : np.sum(0.0)}

with open('test_sesh.pkl', 'wb') as f:
	dill.dump_session(f)

with open('nemt_test.pkl', 'wb') as f:
	dill.dump(nemt, f)