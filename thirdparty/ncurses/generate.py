#!/usr/bin/python3

# Create generated_files.tar, which contains output from ncureses
# configure as well as a bunch of files generated by shell, awk, and
# native programs. Expects ncurses tarball in the cwd.

# Run in a container for approximate reproducibility:
# $ wget https://forge-magic-mirror.awsvip.dbxnw.net/archives/ncurses/ncurses-6.1.tar.gz
# $ wget https://forge-magic-mirror.awsvip.dbxnw.net/archives/drte-v3/drte-v3-build-sysroot_1.0.0.tar.xz
# $ bzl --build-image build_tools/docker/drbe-v1-xenial cexec ./generate.py

import os
import shutil
import subprocess

NCURSES_VERSION="ncurses-6.1"
DRTE_BUILD_SYSROOT = 'drte-v3-build-sysroot_1.0.0.tar.xz'
SRC_DIR = os.path.realpath(NCURSES_VERSION)
INCLUDE_MAKE = [
    "curses.h",
    "ncurses_def.h",
    "term.h",
    "parametrized.h",
    "hashsize.h",
]
INCLUDE_OUTS = [
    "curses.h",
    "ncurses_cfg.h",
    "ncurses_def.h",
    "ncurses_dll.h",
    "term.h",
    "termcap.h",
    "unctrl.h",
    "parametrized.h",
    "hashsize.h",
]
NCURCES_MAKE = NCURCES_OUTS = [
    "codes.c",
    "expanded.c",
    "fallback.c",
    "lib_gen.c",
    "unctrl.c",
    "init_keytry.h",
    "lib_keyname.c",
    "comp_captab.c",
    "names.c",
]
GENRULE_TEMPLATE = """
genrule(
    name = "{name}",
    outs = ["{filename}"],
    cmd = r\"\"\"
cat << 'EOF' > $@
{body}
EOF
\"\"\",
)
"""

if not os.path.exists('/dbxce'):
    os.exit('must run in container')

subprocess.check_call(['tar', 'xf', NCURSES_VERSION + ".tar.gz"])
subprocess.check_call(['tar', 'xf', DRTE_BUILD_SYSROOT])
CC = os.path.realpath('root/bin/gcc')

if os.path.exists('build'):
    shutil.rmtree('build')
os.mkdir('build')

os.chdir('build')

subprocess.check_call([
    os.path.join(SRC_DIR, 'configure'),
    "--without-debug",
    "--disable-rpath",
    "--disable-echo",
    "--enable-const",
    "--without-ada",
    "--without-tests",
    "--without-progs",
    "--with-chtype=long",
    "--with-mmask-t=long",
    "--disable-termcap",
    "--without-shared",
    "--enable-widec",
    "--without-cxx",
    '--with-terminfo-dirs=/etc/terminfo:/lib/terminfo:/usr/share/terminfo',
], env={'CC': CC})

subprocess.check_call(["make", "-C", "include"] + INCLUDE_MAKE)
subprocess.check_call(["make", "-C", "ncurses"] + NCURCES_MAKE)
with open('../BUILD.ncurses', 'w') as generated:

    with open('../BUILD.ncurses.head') as head:
        generated.write(head.read())

    for prefix, outs in (('include', INCLUDE_OUTS), ('ncurses', NCURCES_OUTS)):
        for out in outs:
            path = os.path.join(prefix, out)
            with open(path) as src:
                generated.write(GENRULE_TEMPLATE.format(
                    name=os.path.splitext(path)[0],
                    filename=path,
                    body=src.read().replace('$', '$$'),
                ))

print("Generated 'BUILD.ncureses'")
