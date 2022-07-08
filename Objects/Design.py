from dataclasses import dataclass


@dataclass
class Design:
    name: str
    image: str  # string to file location of image
    processes: []

    def getInfo(self):
        materials = []
        methods = []
        for process in self.processes:
            material = process.material
            if not (material in materials):
                materials.append(material)
            for method in process.methods:
                if not (method in methods):
                    methods.append(method)
        return materials, methods

