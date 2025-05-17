import sys
import EnhancedControlNetCannyGUIBoc
import json

# Accept an optional argument for the temp_data_file
if len(sys.argv) > 1:
    temp_data_file = sys.argv[1]
    print(f"[run_eccg.py] Received temp_data_file: {temp_data_file}")
    try:
        with open(temp_data_file, 'r') as f:
            data = json.load(f)
        print(f"[run_eccg.py] Loaded data: {data}")
        # You can pass 'data' to main() or set it globally if needed
    except Exception as e:
        print(f"[run_eccg.py] Failed to load temp_data_file: {e}")

if hasattr(EnhancedControlNetCannyGUIBoc, 'main'):
    EnhancedControlNetCannyGUIBoc.main()
else:
    print('EnhancedControlNetCannyGUIBoc has no main() function.') 