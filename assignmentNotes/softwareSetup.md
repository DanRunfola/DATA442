The assignments in this course can be done in any operating environment you are comfortable with, so long as it is capable of using an NVIDIA GPU with CUDA drivers.  
Generally, we expect most students will complete this course using a local anaconda environment.  If you do not have access to a computer with a dedicated GPU, Google Colaboratory (https://research.google.com/colaboratory/faq.html) provides free cloud-based GPUs in a Jupyter environment very similar to what we will be using; however, we cannot offer support for this option as online services change to rapidly for us to maintain expertise in all of them!

The instructions presented here are for Linux (Ubuntu), and based on Anaconda 3-2020.11 (Python 3.8); however, most notes should be applicable to all operating systems.  We do not support Python 2 in this course.

Please note that the final steps of this tutorial are only relevant for the first lab, and serve as an example for how to get started with your labs.

<b>Step 1: Downloading and Installing Anaconda</b>
Go to https://www.anaconda.com/products/individual and download the appropriate anaconda installer for your system.

<i>Ubuntu Note:</i> By default, the installation for Ubuntu is downloaded as a shell (*.sh) file.  Open your terminal, navigate to where you downloaded it, and run "sudo bash Anaconda*****.sh", where you replace the *s with your version of Anaconda.

<i> General Note:</i> It is helpful for conda to be added to your environment and initialzed.  If the installer prompts you, say yes to these questions.

<b> Step 2: Check the Installation worked </b>
Once you've installed Anaconda, you will have access to the Anaconda Navigator.  On Windows and Mac you should see a link to Anaconda Navigator in the start menu or launchpad, respectively.  In Linux, open a terminal and type "anaconda-navigator".

Once anaconda-navigator is running, click on "JupyerLab" (or Jupter Notebook, if you prefer).  If the interface pops up, it worked!

<i>Ubuntu Note:</i> The rights in your folders may not be correct by default, preventing the browser from opening.  If this happens, the following changes may help:
sudo chmod -R 777 ~/.local/share/jupyter/*

<i>Ubuntu Note:</i> Chromium, if you are using it, has default security restrictions that prevent Jupyter from launching in the browser.  To fix this:
jupyter notebook --generate-config
nano /home/[yourUserName]/.jupyter.jupyter_notebook_config.py
Set c.NotebookApp.use_redirect_file to False


<b> Step 3: Setup your Virtual Environment </b>
Anaconda virtual environments are a tool designed to help you handle package dependencies.  While you can create environments from the command line (if you prefer), you can also use the Anaconda Navigator interface to do so.  If you are using the Anaconda Navigator, you can click the "Environments" tab to create a new environment.  Create an environment with Pyhton 3.* (3.8 at the time of this writing); we named our environment data442, but you can name it anything you would like.  We do not recommend installing both R and Python in the same environment.  Once you have configured your environment, you can choose the default environment for Anaconda in the Anaconda Navigator preferences. Note that you will need to install the applications (i.e., JupyterLab) in this new environment as well; you can do this through the Anaconda Navigator interface.

<b> Step 4: Confirm Your Virtual Environment is Working </b>
After you install Jupyter or JupyterLab (We generally recommend JupyterLab), start a new notebook and type in:
import sys
print(sys.path)

You should see your environment name in the path for python3.  For example, our path includes:
'/home/dan/.conda/envs/<b>data442</b>/lib/python3.8'


<b> (LAB ONE EXAMPLE) Step 5: ... </b>




