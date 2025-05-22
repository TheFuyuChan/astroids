{
  description = "Python development setup with Nix";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, flake-utils, nixpkgs, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python313;
        project = "Astroids";
      in
      {
        devShells.default = pkgs.mkShell {
          name = project;
          packages = [
           python
          ];

          shellHook = ''
            set -e
            if [ -d .venv ]; then
               source .venv/bin/activate
               pip install -r requirements.txt
            else
              echo "Creating Python virtual environment..."
              python -m venv .venv
              echo "Done. Activate it with 'source .venv/bin/activate'"
            fi
            clear
            python --version
            echo "Welcome Back Fuyu"
          '';
        };

      }
    );
}
