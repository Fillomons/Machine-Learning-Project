# Lo scopo di questo file è scaricare il dataset zoo di COCO tramite FiftyOne

import os
import fiftyone as fo
import fiftyone.zoo as foz

# Controlla se la cartella è vuota
def checkEmptyFolder(path):
    return len( os.listdir(path)) == 0


if __name__ == "__main__":

    # Creiamo (se non esiste) la cartella dove salvare le immagini/annotation
    if not os.path.exists("./dataset"):
        os.makedirs("dataset")
        fo.config.dataset_zoo_dir = "./dataset" # Configuriamo la cartella di salvataggio del dataset
    
    # Scarichiamo i vari segmenti del dataset (train, validation e test)
    if checkEmptyFolder("./dataset"):
        dataset = foz.load_zoo_dataset("coco-2017", split="train")
        dataset = foz.load_zoo_dataset("coco-2017", split="validation")
        dataset = foz.load_zoo_dataset("coco-2017", split="test")