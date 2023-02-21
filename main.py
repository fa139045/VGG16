from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

def getPrediction(filename):

    model = VGG16()
    image = load_img('static/uploads/'+filename, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat, top=5)

    label1 = label[0][0]
    label2 = label[0][1]
    label3 = label[0][2]
    label4 = label[0][3]
    label5 = label[0][4]

    print(label1)
    print('Label' + '=' + str(label1[1]))
    print('Acc' + '=' + str(label1[2]))

    return label1[1], round(label1[2]*100),label2[1], round(label2[2]*100),label3[1], round(label3[2]*100),label4[1], round(label4[2]*100),label5[1], round(label5[2]*100)
