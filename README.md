# CT/synthesized CT Segmentation with TotalSegmentator (GPU)

This script generates multiple anatomy segmentations of head and neck region per case using several TotalSegmentator tasks. 

## What it does

For each input image in:
- `/path/to/TotalSegmentator/data`

the script creates an output folder named:
- `<case_id>_segmentations/`

and runs these segmentation tasks:

1. **total** (ROI subset)
   - `skull`, `spinal_cord`, `esophagus`, `trachea`

2. **head_glands_cavities**
   - saved under: `<case_id>_segmentations/oropharynx/`

3. **craniofacial_structures**
   - saved under: `<case_id>_segmentations/mandible/`

4. **headneck_bones_vessels**
   - saved under: `<case_id>_segmentations/larynx/`

5. **brain_structures**
   - saved under: `<case_id>_segmentations/brainstem/`

All runs use **GPU** via `--device gpu` and the script sets:
- `CUDA_VISIBLE_DEVICES=0`


## Usage

1. Put your `.nii.gz` files in:
   - `/usagers3/shsar/code/TotalSegmentator/data`

2. Run:
   ```bash
   python TotalSeg.py
