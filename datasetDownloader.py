#Lo scopo di questo file è scaricare i file di COCO necessari per la rete tramite FiftyOne

import os
import fiftyone as fo
import fiftyone.zoo as foz

#Controlla se la cartella è vuota
def checkEmptyFolder(path):
    return len( os.listdir(path)) == 0



if __name__ == "__main__":

    #Creiamo (se non esiste) la cartella dove andranno le immagini/annotation
    if os.path.exists("./dataset") == False:
        os.makedirs("dataset")
        fo.config.dataset_zoo_dir = "./dataset" #Diciamo a FiftyOne dove vogliamo i file
    
    #Scarichiamo i vari dataset (train, validation e test) in questo caso COCO 2017
    if checkEmptyFolder("./dataset"):
        dataset = foz.load_zoo_dataset("coco-2017", split="train")
        dataset = foz.load_zoo_dataset("coco-2017", split="validation")
        dataset = foz.load_zoo_dataset("coco-2017", split="test")