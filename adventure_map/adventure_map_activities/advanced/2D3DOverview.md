---
title: "Field Test: Creating 2D and 3D Tactile Math - Overview"
description: Tangible Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB
---

# Field Test: Creating 2D and 3D Tactile Math - Overview

[Print this page](https://www.printfriendly.com/print?url=https://github.com/aabdurmohammed-source/TADA/blob/main/embeds/adventure_map_activities/advanced/2D3DOverview.md)

*© 2025 Joan Horvath and Rich Cameron, [Nonscriptum LLC](http://nonscriptum.com) May 7, 2025*
*Released under a [Creative Commons CC-BY International 4.0 License](https://creativecommons.org/licenses/by/4.0/deed.en). You may freely share and adapt as long as you keep this notice and attribution to the authors. Supported by a grant from the Northwest Center for Technology Training (CATT-NW) at Washington State School for the Blind.*

## Introduction

Creating tactile mathematics drawings requires a precision that is challenging to achieve in freehand sketches. In these Activity Plans, we will describe how to use the open-source program OpenSCAD to create 2D and 3D graphics. We also describe how to access our library of over 100 3D printable models which we have created in OpenSCAD to support our science and mathematics books.

OpenSCAD is a computer-aided design (CAD) program that allows a user to create objects with a text-based interface. It is a free, open-source program downloadable from [openscad.org.](https://openscad.org) OpenSCAD runs on MacOS, Windows and Linux computers, but not on tablets, phones or Chromebooks. It needs to be installed on the computer (it is not web based). There are various commercial derivatives that have different features, but these are not compatible with the models in our repository and often are adding visual coding features.

Objects are designed in OpenSCAD with text, in a custom language very similar to the C, Java, or Python coding languages. This means that Blind and Low Vision (BLV) users can own the entire workflow, although they will need to wait for the end product to be able to check their design. (Unless they use an AI chatbot or colleague to check the design before committing it to swell paper or a 3D printer.)

OpenSCAD is a good tool to draw precise shapes and show relationships among different shapes, for example in teaching and learning geometry. We do not cover the mathematics behind our models here. We are more focused on the mechanics of drawing rather than why one might want to draw a particular curve or create a 3D model. For the math background, refer to our books and associated model repositories in the Resource section of TADA! There are two main sections to the TADA! Activities about 3D printing and OpenSCAD:

- Section A: Making SVG Shapes in OpenSCAD
  * Examples of creating 2D mathematical shapes and exporting them to SVG
- Section B: Programming in OpenSCAD
  * A discussion of text coding in general and using OpenSCAD to create 2D and 3D models in particular
- Section C: Guide to Published 3D Printable STEM Models
  * An overview of the 100+ models in our Github repositories, other free community resources, and our books.

### Graphics in this Guide

We have a [folder of 2D Graphics in SVG format](https://drive.google.com/drive/folders/1maTKpTq4_aMJYr_7CuFTkt3jby-zGjrA?usp=sharing) that are created in these activities, for readers who want tactile versions. For that reason we have not included any screenshots and have kept code samples as just indented plaintext for maximum accessibility. We note the .svg filename for each of the line graphics in this guide.

Rather than alt text, which in most cases will be redundant with the name of the simple 2D graphic, we have a short descriptive title (in italics) for each inline figure in this document and note the name of the corresponding svg for a tactile version.
We assume that the reader is familiar with making tactile diagrams from svg files.

For the 3D models we discuss, we will have OpenSCAD screenshots or other photographs with alt text.

### Other Tools for Tactile Graphs

Other tools exist for creating tactile graphs, notably [Desmos](https://www.desmos.com/). There are articles on their site about [Desmos accessibility](https://www.desmos.com/accessibility) (including generating Braille equations) and [exporting Desmos graphs for embossing](https://help.desmos.com/hc/en-us/articles/4407851291149-Embossing-Graphs-with-Desmos). We will not discuss creating accessible graphs here since that territory is well-served by Desmos.

### Screen-Readable Equations

If you want to create materials for publication using equations (as opposed to drawings) several tools and workflows exist, although all of them have some drawbacks and challenges in their relationships with authoring tools and then their screen-reader interfaces. We will discuss this in more detail in our Guide to published STEM models and books. Some publishers change equations into images and provide alt text, but this is cumbersome and error prone, and we hope that there are ways to automate the process of creating readable equations.

[Lake Pine Braille's Equalize Editor](https://www.lakepinesbraille.com/) for equations is another free tool to write math equations, but is not a graphics program.

### 3D Printing

The 3D examples in Activities B.2, B.3 and C are intended to be created by a 3D printer. 3D printing is a complex subject, and we have covered it in depth elsewhere. It is a three-step process:

- Creating a model (the focus of these activities)
- Running a "slicing" program to turn the model into command for the printer
- Actually printing the model.

We developed a [guide and lesson plans for 3D geometry objects](https://www.nonscriptum.com/geometry) for another project. Check out the "[Teacher's Guide](https://docs.google.com/document/d/1ZAU2O2-d_gNAvh3ypucrAjGNVBshgS0-ZhNkeehTwXQ/edit?tab=t.0#heading=h.5dyffe5uaypz)" there, which has an extensive introduction to 3D printing aimed at TVIs as well as links to other resources.

Our book Mastering 3D Printing, 2nd Edition (2020) from Apress (available on Amazon and other resellers) is a more comprehensive guide. The examples in this document were designed to print well on a standard consumer-grade 3D printer without support material or other challenging features. We discuss design decisions for our published models in Section C of this guide.

### Tip: 3D Printing for BLV

3D printing can be challenging for anyone, but more so for BLV users since some key parts of the software development chain have limited accessibility. There are several open source slicing programs (called "Slicers") to do the second step, and this requires some knowledge of a 3D printer.

There are some efforts in the community (like [3D Make](https://github.com/tdeck/3dmake)) to automate some of these away from the user, but it is still early days. Anecdotally we hear that BLV slicer users get by with a mix of AI or colleague review of screenshots during the process of slicing and printing. The group at "3d-Printing-Access" has been sharing practical tips and tricks for non-visual 3D printing, and you might want to check them out. To join, make an account at [groups.io](https://groups.io/) and then search on "3d-Printing-Access" to find the group.

---

**Previous:** [Activity 3: Iterating on SVG Drawings & Beyond](3_advanced.md) · **Next:** [Section A: Making 2D Shapes](2DIntro.md) · **Back to:** [Adventure Map](../../04_ADVENTURE_MAP.md)
