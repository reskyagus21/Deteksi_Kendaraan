from roboflow import Roboflow
rf = Roboflow(api_key="ht2nPpDkIBwNpwA9hvM4")
project = rf.workspace("skripsi-v7dmc").project("deteksi-pelanggaran")
dataset = project.version(4).download("yolov5")
