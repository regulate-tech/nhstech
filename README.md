# nhstech

UK health and care sector ICT survey tools

This repository hosts a project set up by RTFM Club to map out information and communications technologies (ICTs) being used within the UK health and care sectors.

The goal of this project is to provide useful information for people making decisions about which ICTs to buy and deploy in these sectors.

## Structure

The repository contains some tools for sourcing and manipulating information about the UK health and care system. 

These folders will be prefixed with 'tools-', eg 'tools-geospatial'.

It also contains code for pulling and analysing particular datasets, organised into folders with the prefix 'subject-', eg 'subject-paper'.

## Setup

We want to make it as simple as possible for people to replicate the analyses carried within the project.

We will generally keep data in .csv files and use Python for processing it as this is human-readable and a widely-known approach.

Development will often be done in Jupyter notebooks and before moving routines into separate Python files as necessary.

We will look at using other data storage systems, like Postgresql, where this seems necessary for a particular form of analysis.

### Prerequisites

You will want to have access to the following software -

Jupyter Notebook editor - [Google Colab](https://colab.research.google.com/) is a no-install option.

Git for your platform - (https://github.com/git-guides/install-git)

Python for your platform - https://www.python.org/downloads/

### Configuration

Once you have Git installed, you can clone this repository:
git clone https://github.com/regulate-tech/nhstech

You will now have a local copy of the file structure in the directory where you ran the 'git clone' command.

You can navigate to each sub-directory to run any python scripts they contain following any setup instructions in a config.md file.

In most cases, it is a good idea to setup a virtual environment that has been configured to run a set of scripts. https://docs.python.org/3/tutorial/venv.html

## Usage

If you are interested in carrying out your own analysis of new datasets then you can use our tools for this.

We would recommend following our structure for setting up a new 'Subject' area by looking at the README.md files in the 'subject-...' folders.

## Design

We are focused on producing good, replicable analyses that will then be used by other people in articles, policy papers etc.

Most of the direct output from the project will be 'low production value' as our focus is on the analysis but be would like to see good design in any derived works.

## Contributing

We would welcome any new analyses that fit within our overall aims, either fully coded or as ideas for us to work on.

## Contacts

You can get in touch on Github by creating an issue and tagging @regulate-tech

## Licence

We are using GNU General Public License v3.0.
