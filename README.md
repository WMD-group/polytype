[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/258219170.svg)](https://zenodo.org/badge/latestdoi/258219170)

# Perovskite Polytype Predictions   

Polytypism, which is ubiquitous in oxide perovskites, also shows up in lead halide perovskites. Polytype structures have been experimentally observed using TEM recently and its influence on the carrier performance was also characterised (details can be found from the bottom reference papers). There are fansinating electronic and ionic phenomena to be expected in these materials. Typical lead halide polytypes can be seen from this figure:

![all_polytype_F1](https://user-images.githubusercontent.com/25340554/129134302-8d062153-55fe-4c4a-b642-4abf76af5481.png)

This repository contains a set of tools and crystal structures for the description of perovskite polytypes in general, but halide perovskites in particular. We provide a combined method of Ising-type model Hamiltonian and genetic algorithm, which can be used to identify low energy configurations.

It is structured as follows:

## Structure generator (Ji-Sang Park)

A python code to generate arbitrary perovskite stacking sequences to access complex polytypes and stacking faults.  
Tips for generating the disp for any polytypes: compare the sequence with a perfect 3C structure, if the positions of both AX3 and B remains the same, then the index is (0, 0); for movement of AX3 and B, moving towards left (index + 1), moving towards right (index -1).  
 
## Structure analysis (Zhenzhu Li)
 
Scripts for electrostatic analysis. 

## Ising model / Genetic algorithm (Zhenzhu Li)
 
Python codes to search for high or low energy stacking sequences. See the [IsingHamilotian_GA.ipynb](https://github.com/WMD-group/polytype/blob/master/IsingHamitonian_GA.ipynb) file.

![Picture 1](https://user-images.githubusercontent.com/25340554/129136868-16a4f03b-6266-4a4b-80b0-ba8b1033bbc8.png)

## Structure collections
 
3D structure models that have been generated for various perovskites. They may be in VASP format (POSCAR) or Crystallographic Information File (CIF). Both can be opened using [VESTA](http://jp-minerals.org/vesta/en/).

Requirements
------------

The main language is Python 3 and has been tested using Python 3.6+. Basic requirements are Numpy and Scipy. [pymatgen](www.pymatgen.org) is also required for some of the tools.

Useful links
------------

* [Ramsdell notation for polytypes](https://www.tf.uni-kiel.de/matwis/amat/semi_en/kap_a/basics/ba_1_1.html)

* [The Many Faces of Mixed Ion Perovskites: Unraveling and Understanding the Crystallization Process](https://pubs.acs.org/doi/abs/10.1021/acsenergylett.7b00981) 

Used in
------------

* [Hexagonal stacking faults act as hole-blocking layers in lead halide perovskites](https://pubs.acs.org/doi/10.1021/acsenergylett.0c01124) (ACS Energy Letters, 2020)

* [Evolutionary exploration of polytypism in lead halide perovskites](https://doi.org/10.1039/D1SC03098A) (Chemical Science, 2021)

