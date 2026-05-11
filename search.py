from load_documents import load_documents

def search_documents(query, folder="documents"):
    
    documents = load_documents(folder)
    
    results = []
    
    for name, content in documents.items():
        
        if query.lower() in content.lower():
            results.append(name)
    
    return results


if __name__ == "__main__":
    
    query = "machine learning"
    
    matches = search_documents(query)
    
    print("Matching Documents:")
    
    for match in matches:
        print(match)