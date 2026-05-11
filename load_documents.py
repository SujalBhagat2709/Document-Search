import os

def load_documents(folder):
    
    documents = {}
    
    for file in os.listdir(folder):
        
        path = os.path.join(folder, file)
        
        if file.endswith(".txt"):
            
            with open(path, "r", encoding="utf-8") as f:
                documents[file] = f.read()
    
    return documents


if __name__ == "__main__":
    
    docs = load_documents("documents")
    
    print("Loaded documents:", len(docs))