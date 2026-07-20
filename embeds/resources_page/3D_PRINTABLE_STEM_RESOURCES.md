---
title: "Section C: 3D Printable STEM Resources"
description: Tangible Art & Design Adventures by the Center for Assistive Technology Training Northwest, WSSB
---

# Section C: 3D Printable STEM Resources

We have developed roughly 100 math and science models, associated with five of our books. This section discusses where to find the models and the books that describe them. All of the models are written in OpenSCAD and as such are mostly able to be altered. Our books describe how to alter each model for different cases. The models were designed to be relatively easy to 3D print on a school 3D printer that might have seen better days. If a print is challenging for some reason we note that in the relevant book.

The models were not really designed to stand alone. The books describe the science or math and how changing model parameters in OpenSCAD reflect different cases. We do not really recommend trying to use them without reviewing the background material. Some models, like the castle model in *Make: Geometry*, are evolved through several chapters while scaffolding different math concepts.

Some models are quite open-ended: for example, the botanical model in *Science Projects Volume 1* has many parameters and allows a user to play with creating an imaginary but plausible plant. Others are a bit more constrained, or are just one visualization of a particular mathematical point. We encourage you to download the models and, in conjunction with the books, play around to learn the math and science underlying them.

## Model Repositories

GitHub is a website that allows people to store open-source models like these so that they are freely available to anyone. Our models are available under a [Creative Commons Attribution 4.0 license](https://creativecommons.org/licenses/by/4.0/deed.en), which means that you can print them out, alter them, and do what you like as long as you reference that they are our models in any publication, and cite the original repository and book that they come from.

**Steps:**

First, download the desired repository from GitHub. All of our GitHub repositories are listed at the bottom of our [nonscriptum.com](http://nonscriptum.com) website. Those links take you directly to a download link for each repository. We have also repeated them here for convenience:

- [Make: Calculus Repository](https://github.com/whosawhatsis/Calculus/releases/latest)
- [Make: Trigonometry Repository](https://github.com/whosawhatsis/Trigonometry/releases/latest)
- [Make: Geometry Repository](https://github.com/whosawhatsis/Geometry/releases/latest)
- [3D Printed Science Projects Volume 1 Repository](https://github.com/whosawhatsis/3DP-Science-Projects/releases/latest)
- [3D Printed Science Projects Volume 2 Repository](https://github.com/whosawhatsis/3DP-Science-Projects-Volume-2/releases/latest)

Each of these sends you to the latest release of each repository.

Next, download the repository contents by clicking on the "Source Code (zip)" link on each page to get a zipped file. Unpack the zip file to get the files, which will be arranged into subfolders. In the case of our Science Projects books, the subfolders are arranged into chapters corresponding to the relevant book. In the math book repositories, the subfolders are arranged by topic. We have a list of the topics in each of the Science Projects books later in this document. All of the models per book will be downloaded all at once by this method.

If you are a sophisticated GitHub user, you can click on the "Code" top bar menu item on any of these download release pages and go back to the main repository page, where you can browse the individual files instead of doing a one-step download of everything.

The repositories contain two types of files: `.scad` files and `.stl` files. The `.scad` files are native OpenSCAD files, and can be edited in OpenSCAD as described in previous lessons. The `.stl` files can be imported into the slicer software for any filament-using 3D printer. (Technically they can be used on other types of printers, but they were not designed for that.) In a few cases, there are multiple sets of STL files; we will note those later in this document.

If there is not an `.stl` file for the particular model you want, you can start with any `.scad` file and create an `.stl` file from it as follows (assuming OpenSCAD is open):

1. Click to open one `.scad` file you have downloaded from the repository, which should open OpenSCAD. (The first time you do this you may need to tell your computer to open files ending in `.scad` with OpenSCAD going forward.)
2. In the Design menu, click Render. This creates an exportable version of the file.
3. In the File menu, select Export and then Export as STL.
4. The file should now be exported to a location you specify and ready to be sliced by your 3D printer's software.

If the `.stl` file for the model you want is in the repository, you can put that into your slicing software directly. Our repositories have representative cases included as `.stl` files, but many more variations are possible with some models. Refer to the respective book for details.

## Books

Our books describe the relevant models, how to modify them for different cases, and the math or science behind the models. Our books are not textbooks; they do not cover everything that one might expect to cover in a typical course. They focus on topics that benefit from hands-on models.

### Maker Shed Math Books

All our Make: math books are available in the Maker Shed, at the dedicated [Maker Shed link for Joan and Rich](https://www.makershed.com/collections/make-author-spotlights-joan-horvath-and-rich-cameron). The links change from time to time, so if any of these links do not work, just search on the [main Maker Shed link](https://www.makershed.com). There are epub versions of our *Make: Trigonometry* and [*Make: Calculus*](https://www.makershed.com/products/make-calculus-pdf) books which have equations in MathML, which can be translated into MathJax by appropriately-equipped readers and then read aloud. Note that these epub versions are only in the Maker Shed.

### Springer Link

If your institution has a subscription to [SpringerLink](https://link.springer.com), our Science Projects books are available there. Go into the search feature and type "Horvath Cameron 3D Printed Science Projects". This also brings up an older version of Volume 1, but just ignore that.

### Amazon

Print and Kindle versions are also available at other retailers like Amazon:

- [Make: Geometry on Amazon](https://www.amazon.com/Make-Geometry-coding-printing-building/dp/1680456717/) (2021, Make Community LLC)
- [Make: Trigonometry on Amazon](https://www.amazon.com/dp/1680457985) (2023, Make Community LLC)
- [Make: Calculus on Amazon](https://www.amazon.com/dp/168045739X) (2022, Make Community LLC)
- [Make: Math Teacher's Supplement on Amazon](https://www.amazon.com/dp/1680458302) (2024, Make Community LLC)

Our Science Projects books are best ordered from Amazon as follows:

- [3D Printed Science Projects Volume 1 on Amazon](https://www.amazon.com/3D-Printed-Science-Projects-Classroom/dp/B0CY1WQ633/), 2nd Ed. (Apress, 2024) — Paperback and Kindle
- [3D Printed Science Projects Volume 2 on Amazon](https://www.amazon.com/3D-Printed-Science-Projects-Engineering/dp/1484226941) (Apress, 2017) — Paperback and Kindle

## Accessibility Notes

The epub versions have been tested with the [Thorium epub reader](https://www.edrlab.org/software/thorium-reader/). After you have the book open in Thorium, turn on MathJax functionality, which in turn reads MathML. In the current version of Thorium (2.2.0) check the box to enable MathJax at Settings > Display > MathJax. These settings are only available after you have opened at least one book in Thorium. If you are using a separate screen reader program to interface with Thorium, you might need to add a plugin for it to be able to read MathML correctly. This epub file has been optimized for screen readers and accessibility for our visually impaired readers.

*Make: Geometry*, *Make: Trigonometry*, *Make: Calculus*, the second (2024) edition of *3D Printed Science Projects Volume 1*, and *Make: Math Teacher's Supplement* all have alt text on images. All of our books are available in print and Kindle.

## Grade Levels and Coverage

Our math books are not intended as primary textbooks. Rather, they are supplements that focus on concepts that benefit from a hands-on approach or 3D visualization model. Teaching geometry-first with models also means that it may make sense to teach topics in a different order than the standard, more algebra-oriented one.

With that said, our *Make: Geometry* book has a mix of topics typically taught in both middle and high school, plus some physics concepts (like determining one's latitude and longitude) which are fun ways of testing out the topics.

*Make: Trigonometry* covers many of the topics typically found in an algebra II/trig class or a precalculus course. As such, it is mostly aimed at a high school audience and above, and similarly with *Make: Calculus*.

*Make: Calculus* covers many (but not all) topics found in a traditional Calculus I course, covering both differential and integral topics. It starts off using LEGO bricks for core concepts and then moves to 3D prints, with a few small electronics excursions.

One benefit of this approach is that it is possible to teach material, particularly calculus, at a much younger age than can be done traditionally. We have taught gifted students as young as nine years old calculus basics with the techniques in our books. Our *Make: Math Teacher's Supplement* has longer discussions about assessment and what topics are covered in which book.

Our Science Projects books cross many disciplines. Volume 1 is aimed at middle/high school, and Volume 2, high school/college. Volume 1 has science fair ideas building on the models in every chapter. The topics in each science book (and the types of models contained in the per-chapter folders in the relevant repository) are:

**Science Projects Volume 1 (second edition, 2024)**

1. Math Modeling with 3D Prints
2. Light and Other Waves
3. Gravity
4. Airfoils
5. Simple Machines
6. Plants and their Ecosystems
7. Molecules
8. Trusses
9. Gears

**Science Projects Volume 2 (2017)**

1. Pendulums
2. Geology
3. Snow and Ice
4. Doppler and Mach
5. Moment of Inertia
6. Probability
7. Digital Logic
8. Gravitational Waves

## Learning More About OpenSCAD

All five of our books have an introduction to OpenSCAD. The most in-depth is in *Make: Geometry*, which goes the most deeply into the geometry of OpenSCAD, tying together the math and the program's capabilities. That is probably the best place to start.

OpenSCAD also has good documentation on the [OpenSCAD web page](https://openscad.org) under the "documentation" tab. They have links there to books, videos, and more.

## Special Cases

There are a few special cases in some of our repositories that might be a little confusing. Here is a summary of two of them.

### TPU for Nets

*Make: Geometry* Chapter 9, Surface Area and Nets, describes creating models with `platonic_net.scad` using regular PLA 3D printer filament. Subsequent to the publication of the book, we discovered that these fold-up models work much better if 3D printed in the flexible material TPU. The model needed a slight redesign to work well this way, however. If you look in the Geometry subfolder Nets, you will see a second folder named STL. In that folder there are `.stl` files that include "tpu" in the name. Use these to make flexible versions of the model. As an aside, printing in flexible material is challenging. Consult with your local expert before embarking!

### Electronics

There are programs for a few electronics projects in the *Make: Calculus* repository that are in a folder marked "arduino_demos". Similarly the *Make: Trigonometry* repository has a subfolder named "Robot Arm." This has both `.stl` files for creating a small robot arm as well as code to run it. You can just ignore those, unless you are also interested in learning electronics.

## Lesson Plans

Lesson plans for some of the materials in our Geometry book and, to a lesser degree, the Trigonometry book are available on our [Geometry Lesson Plan page](https://www.nonscriptum.com/geometry). This set of free lessons also includes a Teacher's Guide which has a fairly extensive getting-started 3D printing section. However, these lesson plans pre-date the books by a substantial period of time, and so there has been some evolution and they do not follow each other all that closely. However, you might find them a good backup resource for ideas.

## Classes

We have many video courses on LinkedIn Learning about 3D printing, and one that is a short version of *Make: Calculus* called *Assembling Calculus*. Your institution might have a subscription to LinkedIn Learning, or many public libraries allow you to watch classes in the library. All of these courses, as well as periodic in-person trainings, are linked on our [Nonscriptum classes page](https://www.nonscriptum.com/classes) under "classes for adults."

## Other Sources of STEM Models

There are many math and science models available on free model sites. The challenges are that anyone can post a model, and it is possible that the model is not actually printable or that the science or math might be incorrect. The site [printables.com](http://printables.com) is maintained by 3D printer manufacturer Prusa Research, is easy to search, and has models that are a little better to print on average compared to other fully-open repositories.

[The NASA 3D printable files repository](https://nasa3d.arc.nasa.gov/models/printable) has a fairly eclectic set of space-related models.

[The Smithsonian 3D model page](https://3d.si.edu/) has digital scans of a few items in Smithsonian museum collections. However, many linked files are not ready for consumer-level 3D printing. Some might require a resin (liquid) 3D printer or industrial laser sintering printer to support the complex fine detail of many of their models. Most are in a format (`.obj` file) that may cause issues in consumer-level slicing software, if it can be imported at all.

Finally, the nonprofit [See3D](https://www.see3d.org) is creating directories of tactile models and printing services to supply them for TVIs and others. They have a long list of other resources on their site.

---

*© 2025 Joan Horvath and Rich Cameron, Nonscriptum LLC. Released under a [Creative Commons CC-BY International 4.0 License](https://creativecommons.org/licenses/by/4.0/deed.en). You may freely share and adapt as long as you keep this notice and attribution to the authors. Supported by a grant from the Northwest Center for Assistive Technology Training (CATT-NW) at Washington State School for the Blind.*

**Back to:** [Resources](02_RESOURCES.md)
