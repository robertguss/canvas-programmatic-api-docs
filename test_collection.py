import json
from pathlib import Path

def test_collection():
    collection_path = Path("output/canvas_api.postman_collection.json")
    
    if not collection_path.exists():
        print("❌ Collection file not found!")
        return
    
    with open(collection_path, 'r') as f:
        collection = json.load(f)
    
    print("✅ Collection loaded successfully!")
    print(f"📊 Collection name: {collection['info']['name']}")
    print(f"📊 Total resource folders: {len(collection['item'])}")
    
    # Count total endpoints
    total_endpoints = 0
    for folder in collection['item']:
        if 'item' in folder:
            total_endpoints += len(folder['item'])
    
    print(f"📊 Total endpoints: {total_endpoints}")
    
    # Show some sample folders
    print("\n📁 Sample resource folders:")
    for i, folder in enumerate(collection['item'][:5]):
        endpoint_count = len(folder.get('item', []))
        print(f"   {folder['name']}: {endpoint_count} endpoints")
    
    # Show sample endpoint from Courses
    courses_folder = next((f for f in collection['item'] if f['name'] == 'Courses'), None)
    if courses_folder and courses_folder.get('item'):
        sample_endpoint = courses_folder['item'][0]
        print(f"\n🔍 Sample endpoint: {sample_endpoint['name']}")
        print(f"   Method: {sample_endpoint['request']['method']}")
        print(f"   URL: {sample_endpoint['request']['url']['raw']}")
    
    print("\n✅ Collection validation complete!")

if __name__ == "__main__":
    test_collection()
