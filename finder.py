import cv2
import numpy as np
import pickle,json
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from scipy.spatial import distance
import os,glob
os.environ["CUDA_VISIBLE_DEVICES"]="0"



def get_model():
    base_model = VGG16(weights='imagenet', include_top=True)
    model = Model(inputs=base_model.input,
                  outputs=base_model.get_layer('fc2').output)
    return model

def feature_extraction(img,model):
    img = cv2.resize(img,(224,224))
    img = image.img_to_array(img)
    img4d = np.expand_dims(img, axis=0)
    pred = model.predict(img4d)[0,:]
    return pred

filenames = glob.glob("./Tunics/*")

list_pickl = ['./precompute/tunic/tunic.pickle']

# del model
final = {}
model = get_model()
for idx, filename in enumerate(filenames):
        _, ftail = os.path.split(filename)
        fhead, _ = os.path.splitext(ftail)
        dups = []
        print('1')
        img = cv2.imread(filename)
        feat_img = feature_extraction(img, model)
        for files in list_pickl:
            print('2')
            with open(files, 'rb') as f:
                b = pickle.load(f)
                pid = list(b.keys())
                feats = list(b.values())
                print('3')
                for i, feat in enumerate(feats):
                    dist = distance.euclidean(feat,feat_img)
                    print('4')
                    if dist == 0:
                        if fhead != pid[i]:
                            print('5')
                            dups.append(pid[i])
        final[fhead] = dups
        
                    


del model

print(final)

json = json.dumps(final, indent=5)
f = open("./results/result_tunic.json","w")
f.write(json)
f.close()
