# Automake Settings
# Copyright (C) 2019-2024 kaoru  https://www.tetengo.org/

script_files = \
    check_file_name_lengths.py \
    filter_iwyuout.py \
    list_sources.py \
    make_precompiled_h.py

EXTRA_DIST = \
    ${script_files} \
    call_clang-format.sh \
    iwyu_mappings.imp


mypy: ${script_files}
	${MYPY} ${MYPY_OPTS} ${srcdir}

format: ${EXTRA_DIST}
	${BLACK} ${srcdir}
	${ISORT} ${ISORT_OPTS} ${srcdir}
