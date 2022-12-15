import subprocess


# bashCommand = "cd /home/pglolpi/Documents/Programs/Python/EDI/Cmd"
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()
# subprocess.run("cd /home/pglolpi/Documents/Programs/Python/EDI/Cmd", shell=True)
def gsearch():
    bashCommand = "python -m pushtotalk --device-id '6f114e88-77c4-11ed-85ee-e45f01d9349a' --device-model-id 'edi-ppr-80627-edi-ppr-j6h9i3'"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, cwd='/home/pglolpi/Documents/Programs/Python/EDI/Cmd')
    output, error = process.communicate()

# subprocess.run(["cd ..","home/pglolpi/Documents/Programs/Python/EDI/Cmd", "python -m pushtotalk --device-id '6f114e88-77c4-11ed-85ee-e45f01d9349a' --device-model-id 'edi-ppr-80627-edi-ppr-j6h9i3'"]) # shell=False

# this is written when I am talking to my 10th batchmates on call
