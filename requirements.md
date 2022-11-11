# Software Requirements
 
## Vision

To help people bringing their photos back to life. We can obtain resulting biomedical images with natural and sightly color appearance which looks like the reference images', and meanwhile make the whole procedure quite convenient and efficient.
 
## Scope (In/Out)
 
- IN - What will your product do
    - Describe the individual features that your product will do.
    - The model will take as input a grayscale image and process it to try to colorize it.
    - It will be available as a desktop application.
    
- OUT - What will your product not do.
  - It will not turn out to be a web application.
  - It can't crop the images.
 
### Minimum Viable Product vs
 
What will your MVP functionality be?

- Input button to upload grayscale image.

- Review panel for the outputted colored image.

- Download colored image button.

What are your stretch goals?

- Make the program convert a colored image into a grayscale image.

### Stretch
 
What stretch goals are you going to aim for?

- Make the program convert a colored image into a grayscale image.
 
## Functional Requirements
 
List the functionality of your product. This will consist of tasks such as the following:
 
1. The user can press on an input button to upload grayscale image.

2. The user can review the outputted colored image.

3. The user can download colored image button.
 
### Data Flow
 
The model will be trained enough so that once the user uploads an image of his/her choice, the program will take it and render it as a colorized image. After that the user will have a choice to download the image on his/her personal device.
 
## Non-Functional Requirements
 
Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.
 
Examples include:
1. Security; The provided images from the user will only be accessed by the user and the model it self.
2. Usability; We will create a GUI that will help the user easily upload and download images and view them.
