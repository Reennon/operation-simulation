### Operation Simulation LLM Bot (SimBot)

The simulation bot is intended to serve as a mediator between an end user and simulation environment for military
oprations using RL.

User can either make a conversation with LLM about the documentation of the API, to clarify further requst or to learn more about the operation sumulation.
Or, straightforwardly prompt an LLM to request the API to make a specific operation, for example you may ask it to execute simulation with default parameters.  

![image](https://github.com/Reennon/operation-simulation/assets/37474734/be47dbe3-390b-4802-ba19-e66d41e13338)

## Prerequisites
1. Install Llama-cpp for M1 Mac:

`CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python`
`CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir`

2. Install redis on Mac:

`brew install redis`

3. Run redis locally:

`brew start-service redis`
`redis-cli`

4. Download NeuralHermes LLM from HuggingFace:

https://huggingface.co/TheBloke/NeuralHermes-2.5-Mistral-7B-GGUF

5. Put it into model directory, and specify the name in `models.yml` file inside of parameters directory.

6. Specify environment variables:
```
PROJECT_PATH=/path/to/project/folder;
REDIS_HOST=127.0.0.1;
REDIS_PORT=6379
```
7. If needed specify API url and API documentation in `src/packages/constants` package

8. Download dependency of RL operation simulator:

https://github.com/yvoievid/intro-to-data-science

9. Install python dependecies for OpSim (this project)
`pip install -f dependenices.m1.txt` or `requirements.txt` for not Apple M1 users
11. Run debug.py script from `src/bin/debug.py` with working directory set equal to the `PROJECT_PATH`

![image](https://github.com/Reennon/operation-simulation/assets/37474734/ca695198-0fa5-455a-9956-fea4d1a0cd26)

 
