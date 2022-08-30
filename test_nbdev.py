import modal
import os, subprocess

stub = modal.Stub("ci")
image_with_model = (
    modal.DebianSlim()
    .apt_install(["git"])
    .pip_install(["git+https://github.com/fastai/fastcore.git",
                 "git+https://github.com/fastai/execnb.git"])  
)

@stub.function(image=image_with_model,
               mounts=[modal.Mount(local_dir="./nbdev", remote_dir="~/")])
def ci():
    print('hello')

if __name__ == '__main__':
    with stub.run():
        os.chdir('nbdev')
        subprocess.call(["pip", "install", ".[dev]"])
        subprocess.call(["nbdev_test", "--do_print"])