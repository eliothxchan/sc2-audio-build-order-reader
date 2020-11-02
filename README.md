# StarCraft 2 Audio Build Order Reader

This project takes in a build order and reads it using text-to-speech based on the timestamps included in the build order itself. The supply markers, currently, are purely cosmetic.

This does not work without timestamps.

# Requirements and Running the Application

This project requires Python 3. Install the necessary requirements using `pip3 install -r requirements.txt`.

Place a file into the `builds` folder with the build order. Run `python3 ./main.py --build=name-of-build.txt --shorthand=True`. An example is included in this repo. Copying and pasting a build from SpawningTool should be good enough, but make sure there aren't empty lines at the start or at the end of the file.

# License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.