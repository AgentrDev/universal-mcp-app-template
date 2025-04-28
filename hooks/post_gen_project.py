import os
import shutil

def main():
    package_name = "{{ cookiecutter.package_name }}"
    # Define paths - reference the generated file names directly
    push_sh = "push_on_agentr.sh" # Path in generated project root

    # Make push_on_agentr.sh executable - This is the *only* thing the hook needs to do now
    if os.path.exists(push_sh):
        os.chmod(push_sh, 0o755)


if __name__ == "__main__":
    main()