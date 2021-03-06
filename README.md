[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/258219170.svg)](https://zenodo.org/badge/latestdoi/258219170)

# Polytype

This repository contains a set of tools and crystal structures for the description of perovskite polytypes in general, but halide perovskites in particular.  It is structured as follows:

## Structure generator (Ji-Sang Park)

A python code to generate arbitrary perovskite stacking sequences to access complex polytypes and stacking faults.  

## Structure collections
 
3D structure models that have been generated for various perovskites. They may be in VASP format (POSCAR) or Crystallographic Information File (CIF). Both can be opened using [VESTA](http://jp-minerals.org/vesta/en/).
 
## Structure analysis (Zhenzhu Li)
 
Scripts for electrostatic analysis. 

Requirements
------------

The main language is Python 3 and has been tested using Python 3.6+. Basic requirements are Numpy and Scipy. [pymatgen](www.pymatgen.org) is also required for some of the tools.

Useful links
------------

* [Ramsdell notation for polytypes](https://www.tf.uni-kiel.de/matwis/amat/semi_en/kap_a/basics/ba_1_1.html)

* [The Many Faces of Mixed Ion Perovskites: Unraveling and Understanding the Crystallization Process](https://pubs.acs.org/doi/abs/10.1021/acsenergylett.7b00981)
