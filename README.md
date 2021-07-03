# HC Tech Systems Candidate Test

Welcome to HC Tech's testing repo, please complete the following tasks:

1. Log into the IP with the credentials provided in the email
2. After initially connecting, setup a SSH key
3. Install nano (some config files may need to be fixed first)
4. Clone this repo into your home folder (`https://github.com/HC-Technologies/systems-test.git`)
5. Create a new text file at the root of the cloned repo named "answers"
6. Install numpy for python2.7 in the `/opt/rh/` directory (specifically NOT the OS's instance which is python3)
7. Run `script1.py` in this repo, if you were to take the output of that command and sort it alphabetically what would be the first and last numbers? (put them in `./answers` file)
8. Find a cat picture on google (any as long as its work appropriate), download it into this repo, find the sha256 of the photo and add the hash to your `./answers` file
9. run `script2.py` in the background, and then kill the backgrounded process.
10. run `script3.py` and redirect `stderr` and `stdout` to different files.
11. use the VM to determin the ephemeral port that your SSH connection is running on, add this to your `./answers` file.
12. After you have established that your SSH key works, disable password login in the sshd config and test that the change has been implemented.
13. Find the log in which you first logged into the box with your new SSH key, add that line to your `./answers` file.
14. add your `./answers` file to the git repo and commit (do not push changes as you do not have access)
