import os
import subprocess

os.environ['CUDA_VISIBLE_DEVICES'] = '0'


add = '/path/to/TotalSegmentator/data' 

for im in sorted(os.listdir(add)):
    if not im.endswith('.nii.gz'):
        continue  # Skip non-NIfTI files

    image = os.path.join(add, im)
    pn_b = im.split('.')[0]
    out = os.path.join(add, pn_b + '_segmentations')
    out2 = os.path.join(out, 'oropharynx')
    out3 = os.path.join(out, 'mandible')
    out4 = os.path.join(out, 'larynx')
    out5 = os.path.join(out, 'brainstem')

    # Ensure output directories exist
    os.makedirs(out, exist_ok=True)
    os.makedirs(out2, exist_ok=True)

    # Run TotalSegmentator for skull and spinal cord from total task
    subprocess.run([
        "TotalSegmentator",
        "-i", image,
        "-o", out,
        "-ta", "total",
        "--roi_subset", "skull", "spinal_cord", "esophagus", "trachea",
        "--device", "gpu"
    ])

    # Run head_glands_cavities (full task, no roi_subset)
    subprocess.run([
        "TotalSegmentator",
        "-i", image,
        "-o", out2,
        "-ta", "head_glands_cavities",
        "--device", "gpu",
        #"--ml"
    ])

    subprocess.run([
        "TotalSegmentator",
        "-i", image,
        "-o", out3,
        "-ta", "craniofacial_structures",
        "--device", "gpu",
        #"--ml"
    ])

    
    subprocess.run([
        "TotalSegmentator",
        "-i", image,
        "-o", out4,
        "-ta", "headneck_bones_vessels",
        "--device", "gpu",
        #"--ml"
    ])

    subprocess.run([
        "TotalSegmentator",
        "-i", image,
        "-o", out5,
        "-ta", "brain_structures",
        "--device", "gpu",
        #"--ml"
    ])
