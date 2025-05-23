#!/usr/bin/env python   
# -*- coding: utf-8 -*-

# conda activate Ccode3DGen_

# Created by Andre Dickinson
# Email: saraintelai@gmail.com
# date: 2025-01-30

import sys
import ccode3dgen_seg

# Accept an optional argument for the image_path
image_path = sys.argv[1] if len(sys.argv) > 1 else None
if image_path:
    print(f"[run_sam.py] Received image_path: {image_path}")

if hasattr(ccode3dgen_seg, 'main'):
    if image_path:
        ccode3dgen_seg.main(image_path)
    else:
        ccode3dgen_seg.main()
elif hasattr(ccode3dgen_seg, 'SegmenterApp'):
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    # Try to pass image_path if the constructor accepts it
    try:
        if image_path:
            window = ccode3dgen_seg.SegmenterApp(image_path)
        else:
            window = ccode3dgen_seg.SegmenterApp()
    except TypeError:
        window = ccode3dgen_seg.SegmenterApp()
    window.show()
    app.exec_()
else:
    print('No main() or SegmenterApp found in ccode3dgen_seg') 