# Magic Eye
This application use to detect the faces in the video or a streaming camera and get the faces from this video or stream.
The example we tried is a magic eye detects who is infront of your door so if this person is illagable to enter or not. We used an openvino pre trained model  	face-detection-adas-0001 and a CNN model to detect if this person can entered this place or not.

# Process Flow:
# Now

    Now, we are testing the main idea.
    1. we take all the video recorded and classify this video to images.
    2. those images we identify the faces in them
    3. We save those images in a folder called 'media/unknown'
    4. We use to enter a CNN Classifier phase that use to detect if this person is illagble or not by search if this person is allowed in 'media/allowed' which contained the allowed people(half way their)
    5. The application contains a detailed description about each one whom is allowed to enter the home and from here we take all the new data set of the people whom are illagable or not based on the owner's needs
    6. The application contains charts and diagrams to show some statistics as a monitoring services
    7. The application contains an sms service used to generate a new sms when someone newly come using twillio.

# Future Plan
    1. Make a job dynamically detects when  something new happened
    2. Integrate the Systems together (Front end, Backend, Models, etc.)
    3. Run this project on AWS
    4. Optimize our model and flow to detect people in less processing time.
