Abstract
================================================================================



-   Give a brief overview of all the things that we will be going over in this
paper.



Introduction
================================================================================



-   Write about what is computer vision, and more specifically, image classification
    tasks
    -   Consider giving an example of an image classification task with an image
        of a cat or something like that.
-   Write about the lack of foresight in current computer vision research only
    focusing on "tangible objects"
-   Finally, mention what the alternative to researching tangible objects would
    be i.e predicting whether or not something is an object or a "concept"



Motivation
================================================================================



-   Reiterate the lack of research of "concepts" and its dichotomy with the
    abundant research on computer vision tasks with "tangible objects"
-   To provide clarity, provide a set definition that the paper will use for the
    definition of a "concept"
    -   Consider providing an example of a concept that can be visually
        represented. An image of a number would be the go-to.
-   To provide clarity, provide a set definition that the paper will use for the
    definition of a "tangible [object]"


-   Finally, lead into your initial proposing question that the paper will try
    to answer.
-   Mention how that this paper will also attempt at seeing the feasibility of
    utilizing computationally light network designed to see the effectiveness
    for such a task to be handled.
        - Clearly update your initial question with this computationally aware
            approach into the original question

-   Finally, provide a basic outline of what the rest of the paper will discuss
    i.e. the following sections in the some summary form



Related Works
================================================================================

-   Briefly mention the 3 neural network models that we will be examining over
    and why their particular design will aid in ensuring we fit the necessary
    criteria to answer our question.


ResNet V2 (ResNet 50)
--------------------------------------------------------------------------------


-   (Max I need you to do this section since you are probably more familiar with
    the network than I am). For this particular one talk about the original
    version. We can mention the modifications that we had to make for the model
    to be compatible with our given dataset.


MobileNet V2
--------------------------------------------------------------------------------


-   Give a brief overview of what brought out its claim to fame
    -   Check the original paper's abstract and results to get an idea of what
        to say
-   Discuss the original paper's architecture innovations
    -   Give table of encoder (tail and body. Can be 2 separate tables)
    -   Give table of decoder (head)
-   Discuss the following layer components:
    -   ReLU6 and why it is being used
    -   Depth-wise  Convolutions
    -   Inverted Residual Bottlenecks

-   Finally, mention how it will be used as the most "lightweight" model based
    on the number of MACs and parameters it should have in comparison to the
    other neural network designs that the paper is alluding to.


MobileNet V3
--------------------------------------------------------------------------------


-   Give a brief overview of what brought out its claim to fame
    -   Check the original paper's abstract and results to get an idea of what
        to say
-   Compare the paper's architecture to MobileNet V2
    -   Give table of encoder (tail and body. Can be 2 separate tables)
    -   Give table of decoder (head)
-   Discuss the following layer components:
    -   H-Swish and H-sigmoid
    -   The squeeze-and-excite layer included in the residual layer of the
        inverted residual bottleneck

-   Finally, mention how it will be used as the model that is
    on the number of MACs and parameters it should have in comparison to the
    other neural network designs that the paper is alluding to.



Proposed Approach
================================================================================



Dataset
--------------------------------------------------------------------------------


-   Discuss what criteria needs to be satisfied for us to be able to utilize the
    dataset
-   Talk about the chosen dataset(s) and why they were chosen for this paper.

-   **"Perform Exploratory Data Analysis"**
    -   This could be in t he form of pulling up random images and discussing
        anything about how different the image layout, the image dimensions in
        comparison to what was used in the original papers used, and most likely
        the need to change the given network architectures to be compatible with
        our input image dimensions
    -   *Optional(?):* Mention any particular pitfalls that may arise (for
        MNIST, mention how there is a lot of unused pixels that could have been
        used for a more "zoomed in" number of a "larger font size" version of
        the image)
        -   This one is kinda mentioned in the results shortcomings so I'm not
            100% certain if we need it.


Preprocessing
--------------------------------------------------------------------------------


### Stratified Sampling (70 train - 10 validation - 20 test)

-   Discuss what it is
-   Explain the difference between "standard" random sampling and
    "stratified" random sampling
-   To prove the point made above, show a graph of the entire dataset
    label distribution
-   Show what happens when using standard random sampling (the
    distribution should be slightly different)
-   Show what happens when using stratified random sampling (the
    distribution should be more or less the same)


### Super-labels for the dataset

-   Describe what it is
    -   Mapping all MNIST images into the "concept" bucket (let's say label 0) and
        1 for the fashion MNIST images
    -   We do this because our original question is in the form of a binary
        classification task.
    -   It is important to remember that we perform this step after stratified
        sampling to ensure that we still have equal representation of the
        various shapes that still correspond to either a "concept" or a
        "tangible object"

### Image Cropping

-   Discuss what it is
-   What type of cropping for the training set (again, to prevent "memorizing")
    -   Give an example of the random cropping that will be done on the training
        dataset
-   What type of cropping for the validation/test set? Why? (Still want to crop
    to be consistent with training set, but do not want to be random as that
    would introduce unnecessary variance)
    -   Give an example of the center cropping that will be done on the
        validation/test dataset
-   Why do we need it (to prevent the model from "memorizing" pixel values
    and simply mapping it to a particular label without needing to look at the
    whole picture for a proper classification)
    -   For training, prevent "memorizing"
    -   For validation,test, want to be consistent and crop, but only a
        deterministic center crop to avoid introducing variance in results from
        random cropping


Modifying ResNet V2
--------------------------------------------------------------------------------


-   Provide the modified encoder and (possibly) modified decoder structure
    -   Feel free to break up encoder into head and body tables if you have
        modified the body as well
    -   Mention any possible hiccups you faced while you were implementing the
        model


Modifying MobileNet V2
--------------------------------------------------------------------------------

-   Provide the modified encoder and (possibly) modified decoder structure
    -   Feel free to break up encoder into head and body tables if you have
        modified the body as well
    -   Mention any possible hiccups you faced while you were implementing the
        model


Modifying MobileNet V3
--------------------------------------------------------------------------------


-   Provide the modified encoder and (possibly) modified decoder structure
    -   Feel free to break up encoder into head and body tables if you have
        modified the body as well
    -   Mention any possible hiccups you faced while you were implementing the
        model



Results
================================================================================



ResNet V2
--------------------------------------------------------------------------------


-   Show the tables of the various possible hyper parameter error values mapped
    over the 10 epochs
-   Discuss any oddities that were noticed for any hyper parameter setup
-   Determine the best hyper parameter setup for this network
-   **(Stretch Goal)** Also perform a fine-grained hyper-parameter search around
    the best hyper-parameters found in the coarse-grained search
-   At the bear minimum, show classification report & confusion matrix of the
    best hyper-parameter model.


MobileNet V2
--------------------------------------------------------------------------------


-   Show the tables of the various possible hyper parameter error values mapped
    over the 10 epochs
-   Discuss any oddities that were noticed for any hyper parameter setup
-   Determine the best hyper parameter setup for this network
-   **(Stretch Goal)** Also perform a fine-grained hyper-parameter search around
    the best hyper-parameters found in the coarse-grained search
-   At the bear minimum, show classification report & confusion matrix of the
    best hyper-parameter model.



MobileNet V3
--------------------------------------------------------------------------------


-   Show the tables of the various possible hyper parameter error values mapped
    over the 10 epochs
-   Discuss any oddities that were noticed for any hyper parameter setup
-   Determine the best hyper parameter setup for this network
-   **(Stretch Goal)** Also perform a fine-grained hyper-parameter search around
    the best hyper-parameters found in the coarse-grained search
-   At the bear minimum, show classification report & confusion matrix of the
    best hyper-parameter model.



Comparing the best versions of the 3 models
--------------------------------------------------------------------------------


-   Show the tables of the various  error values mapped over the 10 epochs
-   Discuss any oddities or similarities between the models.
-   Make a statement about what attributes of each model represents their strong
    points and weak points.



Potential Points of Criticism
================================================================================



-   Briefly mention that there are multiple points of attack to our findings and
    our results. The next couple of sections should address these points in some
    way shape or form.


Dataset
--------------------------------------------------------------------------------


-   Discuss how that while we did choose MNIST and Fashion MNIST primarily for
    format consistency, we could have tried other potential datasets like
    ImageNet and CIFAR 10. The main reason for this potential change is that
    color could play a role in how one interprets the underlying classification
    behind a certain image.
    -   A potential example is how food companies like to use red, orange, and
        yellow to help encourage people to be hungry or maybe even excitement
    -   Another one is how blue can represent sadness or calmness depending on
        the situation.

-   A question on the amount of preprocessing is also up for debate.
    -   We could have possibly rotated the image to create a more varied and
        larger dataset, but the problem with that is the meaning behind the
        numbers may be lost due to the rotation away from its original
        orientation.
        -   Example: Rotating a "1" 90 degrees may now look like a dash ("-"),
            which has a different meaning entirely


Our Representation of "Concepts"
--------------------------------------------------------------------------------

-   Finally, there is our choice in what we used to represent what a "concept"
    is.
    -   Provide an example of an image of a tangible object (the fruit apple)
        and some company logo (Apple Company) where the company logo can be used
        for non-commercial purposes to explain the premise



Future Endeavours
================================================================================

-   While our results were good, statistics can be misleading. They only showed
    a feasibility in a very narrow on-look into the original question. When
    considering how to re-asses and re-approach this problem, a few notable
    changes are up for consideration.


Alternative Network Architectures
--------------------------------------------------------------------------------

-   Computationally demanding yet possible more accurate models such as NASNet
    or Inception V2 could provide a loss reduction that networks such as the
    MobileNet family, which were designed for embedded systems, could not
    achieve.


Color Datasets
--------------------------------------------------------------------------------

-   Initially, our biggest issue was trying to find a colored dataset for
    representing images of "concepts"
-   The Street View House Numbers dataset could possibly fill in that void.
-   By using this dataset, we could now utilize the colored datasets mentioned
    above like ImageNet or CIFAR 10/100.
-   This would also allow us to determine the importance that color may have on
    making an accurate prediction given a random image.


(Optional) "MobileNet 2.5"
--------------------------------------------------------------------------------

-   **DISCLAIMER**: This should only be necessary if we have the time to talk
    about it and the time to implement the code and show results
-   Bring MobileNet V2's low requirement design and MobileNet V3's superior
    activation functions together
-   Could provide a prototype implementation and run it with the best hyper
    parameters from MobileNet V2 and MobileNet V3




Conclusion/Recap
================================================================================

-   Restate original question and the process we undertook to answer the
    question.
-   Mention that further research needs to be done to fully answer even the
    original question
-   State that a new, just as interesting if not more interesting, question has
    developed over our time conducting our findings over defining a mapping of
    the literal representation of what a image corresponds to and its underlying
    connotation and context to what may or may not necessarily associate with
    the given image.



References
================================================================================

-   Just use LaTeX
