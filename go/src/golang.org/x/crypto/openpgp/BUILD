# @generated: This file was generated by bzl. Do not modify!
# Argument overrides and custom targets should be specified in BUILD.in.

load("//build_tools/go:go.bzl", "dbx_go_library")

dbx_go_library(
    name = "openpgp",
    srcs = [
        "canonical_text.go",
        "keys.go",
        "read.go",
        "write.go",
    ],
    visibility = [
        "//go/src:__subpackages__",
    ],
    deps = [
        "//go/src/golang.org/x/crypto/openpgp/armor",
        "//go/src/golang.org/x/crypto/openpgp/errors",
        "//go/src/golang.org/x/crypto/openpgp/packet",
        "//go/src/golang.org/x/crypto/openpgp/s2k",
    ],
)
