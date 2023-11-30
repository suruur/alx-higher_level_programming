#!/usr/bin/python3
import marshal


def print_m_names():
    with open('hidden_4.pyc', 'rb') as f:
        code = marshal.load(f)

    m_n_sp = {}
    exec(code, m_n_s)
    mod_names = dir(m_n_s)
    f_names = [name for name in mod_names if not name.startwith('__')]
    s_names = sorted(f_names)

    for name in s_names:
        print(name)


if __name__ == "__main__":
    print_m_names()
