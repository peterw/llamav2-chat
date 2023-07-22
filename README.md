# Streamlit Chat Application with Replicate LlamaV2 Model

This is a simple, interactive chat application powered by Streamlit and the Replicate LlamaV2 model. It uses Streamlit for the front end interface and Replicate's LlamaV2 model for generating responses based on user input.

## Prerequisites:

- Python 3.6 or higher
- Streamlit
- Python-dotenv
- Replicate

## Quickstart

1. Clone the repository

```bash
git clone <repo-url>
cd <repo-dir>
```

2. Install the dependencies 

```bash
pip install -r requirements.txt
```

3. Set the environment variables 

Create a `.env` file in the root of your project and add the following environment variables. 

```bash
# .env
REPLICATE_API_TOKEN=<Your Replicate LlamaV2 Key>
```

4. Run the Streamlit app

```bash
streamlit run main.py
```

## Usage

Just type your message in the text input box and press Enter. The AI model will generate a response that will be displayed on the screen.

## How it Works

The `generate_response` function takes the user's input, sends it to the Replicate LlamaV2 model, and then receives the model's response. The response is then displayed on the Streamlit interface.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE.md) file. 

## Sponsors

✨ Learn to build projects like this one (early bird discount): [BuildFast Course](https://www.buildfastcourse.com/)
