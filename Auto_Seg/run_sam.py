import sys
import sam_segmenter_gui_v6

# Accept optional arguments: image_path and device
def get_arg(index, default=None):
    try:
        return sys.argv[index]
    except IndexError:
        return default

image_path = get_arg(1)
device = get_arg(2, "cpu")  # default to cpu

print(f"[run_sam] Using device: {device}")
if image_path:
    print(f"[run_sam] Received image_path: {image_path}")

if hasattr(sam_segmenter_gui_v6, 'main'):
    try:
        if image_path:
            sam_segmenter_gui_v6.main(image_path, device=device)
        else:
            sam_segmenter_gui_v6.main(device=device)
    except TypeError:
        # Fallback if main() does not accept device argument
        if image_path:
            sam_segmenter_gui_v6.main(image_path)
        else:
            sam_segmenter_gui_v6.main()
elif hasattr(sam_segmenter_gui_v6, 'SegmenterApp'):
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    try:
        if image_path:
            window = sam_segmenter_gui_v6.SegmenterApp(image_path, device=device)
        else:
            window = sam_segmenter_gui_v6.SegmenterApp(device=device)
    except TypeError:
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
