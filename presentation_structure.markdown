Title Page
================================================================================
Include name, title of research, etc.


Outline
================================================================================
(Write a table of contents for all of the following slides)


Motivation
================================================================================
-   Explain why having a model between differentiating images of concepts and
    images of tangible objects is an interesting field of study.
-   As with any image task, if a human being is able to differentiate between
    images, the question is can a machine do the same?
-   More importantly, can a machine segregate the labels in an efficient manner
    (ie minimize the amount of MACs) to get to an accurate, and precise answer?

In most of the papers mentioned above, their dataset only consisted of 1 type of
images. it was exclusively either images of a concept (ie numbers) or images of
tangible objects (ie clothing).

For our ressearch, we wanted to examine the performance of well established
models on the combination of the two.

More importantly, we will see how well these models can distinguish between an
image of a concept and an image of a tangible object.


Related Works
================================================================================
-   Talk about the design of MobileNet V2, MobileNet V3, and ResNet
-   Talk about what image data they tested the results of the models upon.
-   Of course, mention any of them that only tested 1 type of image structure
    (be it of concepts or tangible objects)

Proposed Approach
================================================================================
-   Talk about how you went with the code
    -   Mention which datasets were used in the research (ie MNIST and fashion
        MSNIT).
    -   Mention any and all data preprocessing done on the dataset(s)
        -   TODO: Image Flipping
        -   TODO: Zoom in
    -   Display the results of our image preprocessing
    -   Perform stratified sampling to ensure the same distribution of image
        types exist in both the train and test split.
    -   Implement MobileNet V2, MobileNet V3, and RESNet and measure performance
        between them.


Results
================================================================================
-   Lots of tables. This is our padding point
-   Classification Reports
-   Precision-Recall Curves
-   ROC Curve


Limitations
================================================================================
-   A concept can be more than a number. Just like how a number can represent
    more than what it is, the general notion of how we define a "concept"
    applies to more than just arabic numerals. For example, when one thinks of
    "computer science", there is no general consensus on what it can be
    constructed to accurately portray and itemize the topic. On the other hand,
    there is a notion of what a car looks like even though our dataset did not
    contain any images of a car.


Future Endeavors
================================================================================
-   Our research's biggest bottlenecks are the quantity and variance of the
    images labeled as "concepts". A more robust approach would be to incorporate
    images with a transitive relationship between what it actually looks like
    and its underlying, indirect connocation. For example, the image of a
    company's logo can signify a level of quality in a product depending on who
    manufactured it. While the logo itself does not necessarily mean much, the
    value that the comapny or the company's clout that corresponds to the logo
    gives more meaning than what the image is at face value.


Recap and Conclusion
================================================================================
-   Give a brief summary of what we have talked about and the results.
-   In conclusion, it works, but the sample size might be too small the variance
    may be too high to construct a solid examination how one can segregate the
    two cleanly.


References
================================================================================
-   Works Cited Page (LaTeX makes this easy to generate)
