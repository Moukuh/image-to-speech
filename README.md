# Image to Speech
This project uses a combination of machine learning and natural language processing to convert images to speech. 

#### The project is written in Python and uses the following libraries:

* TensorFlow
* Hugging Face Transformers
* OpenAI
* Streamlit

#### The project works as follows:

* The user uploads an image to the project.
* The project uses the TensorFlow image-to-text model to extract text from the image.
* The project uses the Hugging Face Transformers LLMChain model to generate a short story based on the extracted text.
* The project uses the OpenAI GPT-3.5-turbo model to convert the generated story to speech.
* The project plays the generated speech back to the user.
The project is still under development, but it is already able to generate realistic and engaging speech from images. The project is also able to generate stories that are relevant to the content of the image.

#### Getting Started

- To get started with the project, you will need to install the following dependencies:

  `pip install tensorflow transformers openai streamlit`


  Also you can run: 

  `pip install -r requirements.txt`

- Then in the `.env` file paste your respective api keys

- Then you can run the project by running the following command:

  `streamlit run image_to_speech.py`


#### Usage

To use the project, simply upload an image to the project. 
The project will then extract text from the image, generate a short story based on the extracted text, convert the generated story to speech, and play the generated speech back to you.

#### Examples

One the Streamlit UI, upload any image

<img width="721" alt="Screenshot 2023-06-12 at 11 34 46 PM" src="https://github.com/Moukuh/image-to-speech/assets/72088794/3728f4a0-101c-4b19-a815-f41288ffd32b">


The result:

<img width="744" alt="Screenshot 2023-06-12 at 11 33 47 PM" src="https://github.com/Moukuh/image-to-speech/assets/72088794/07b05372-d342-4e01-ae4f-25f659449698">



#### Future Work

The project is still under development, and there are a number of things that I plan to add to it in the future. 

Some of the things that I plan to add include:

* The ability to generate longer stories
* The ability to generate stories in different languages
* The ability to generate stories in different styles
* The ability to generate stories that are more creative and engaging

I am also open to suggestions for other features that you would like to see added to the project. 
If you have any suggestions, please feel free to let me know.
