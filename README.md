This repository contains the code for the final steps
of the NIRCam Data Simulator.

This step takes as input a seed image (with segmentation
map), which is a countrate image generated by (for example)
catalog_seed_image. It also takes a linearized dark current
exposure created by dark_prep.

This step converts the seed image into a 4d signal ramp,
adds poisson noise, cosmic rays, and other detector effects.

The ramp is then reorganized into the requested readout
pattern and added to the dark current ramp.
