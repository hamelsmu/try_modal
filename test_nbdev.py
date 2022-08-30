import modal
import subprocess, os

m = modal.Stub("ci")
img = (modal.DebianSlim()
    .apt_install(["git"])
    .pip_install(["git+https://github.com/fastai/fastcore.git", 
                  "git+https://github.com/fastai/execnb.git"]))

@m.function(image=img, mounts=[modal.Mount(local_dir="./nbdev", remote_dir="/root/nbdev")])
def ci():
    os.chdir('nbdev')
    subprocess.call(["pip", "install", "-q", ".[dev]"])
    subprocess.call(["nbdev_test", "--do_print"])

if __name__ == '__main__':
    with m.run(): ci()