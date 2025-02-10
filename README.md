# Mask Polygon Manipulations

A toolkit for post-processing of instance segmentation masks

## Overview

This repository provides tools for refining and manipulating mask outputs from instance segmentation models. While most models rely on Non-Maximum Suppression (NMS) for basic post-processing, certain applications require additional manipulation techniques to achieve optimal results.

## Background

### Traditional NMS Approach

Non-Maximum Suppression (NMS) is a widely used technique that works by:
1. Sorting detected objects by their confidence scores
2. For each class:
   - Selecting the detection with highest confidence score
   - Computing IoU (Intersection over Union) with remaining detections
   - Removing detections whose IoU exceeds a predefined threshold
3. Repeating until no detections remain above the IoU threshold

While NMS is effective for basic overlap removal, it has limitations:
- Relies solely on confidence scores and IoU
- May not handle complex spatial relationships
- Cannot address class-specific shape requirements
- Doesn't consider domain-specific constraints

## Features

This toolkit extends beyond NMS by providing:
- Advanced polygon manipulation methods
- Custom mask refinement algorithms
- Tools for structured output generation
- Class-specific processing options

## Use Cases

Ideal for scenarios where:
- Masks require geometric refinement
- Class-specific shape constraints exist
- Output structure needs customization


## Usage

[Coming Soon] Implementation examples and usage instructions will be provided in Jupyter Notebooks demonstrating:
- Basic mask manipulation
- Advanced polygon operations
- Integration with common segmentation models
- Custom post-processing pipelines


## Future Work

- [ ] Add Jupyter Notebook examples
- [ ] Implement additional manipulation methods
- [ ] Provide benchmarking tools
- [ ] Add visualization utilities
