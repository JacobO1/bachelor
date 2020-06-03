import dill

def test_dill():
    test_dill.a = 1
    test_dill.b = 2
    test_dill.c = 3
    dill.dump_session("save.pkl")
test_dill ()