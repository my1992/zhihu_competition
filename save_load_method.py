import os
import pickle


# 存储模型
def save_model(mpath, mname, obj):
    try:
        with open(os.path.join(mpath, mname), 'wb') as f:
            pickle.dump(obj, f)
        print("Successfully saved model %s to %s" % (mname, os.path.join(mpath, mname)))
    except:
        os.makedirs(mpath)
        print('Successfully made directory %s' % mpath)
        with open(os.path.join(mpath, mname), 'wb') as f:
            pickle.dump(obj, f)
        print("Successfully saved model %s from %s" % (mname, os.path.join(mpath, mname)))


# 读取模型
def load_model(mpath, mname):
    with open(os.path.join(mpath, mname), 'rb') as f:
        obj = pickle.load(f)
    print("Successfully loaded model %s" % (mname))
    return obj