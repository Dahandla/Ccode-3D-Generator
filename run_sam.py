import sys
import sam_segmenter_gui_v6

# Accept an optional argument for the image_path
image_path = sys.argv[1] if len(sys.argv) > 1 else None
if image_path:
    print(f"[run_sam.py] Received image_path: {image_path}")

if hasattr(sam_segmenter_gui_v6, 'main'):
    if image_path:
        sam_segmenter_gui_v6.main(image_path)
    else:
        sam_segmenter_gui_v6.main()
elif hasattr(sam_segmenter_gui_v6, 'SegmenterApp'):
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    # Try to pass image_path if the constructor accepts it
    try:
        if image_path:
            window = sam_segmenter_gui_v6.SegmenterApp(image_path)
        else:
            window = sam_segmenter_gui_v6.SegmenterApp()
    except TypeError:
        window = sam_segmenter_gui_v6.SegmenterApp()
    window.show()
    app.exec_()
else:
    print('No main() or SegmenterApp found in sam_segmenter_gui_v6') 