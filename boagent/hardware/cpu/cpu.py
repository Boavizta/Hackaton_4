#!/usr/bin/env python3

from cpuinfo import get_cpu_info
from cpuid import cpuid, cpu_microarchitecture, cpu_name, cpu_vendor

CpuInfo = list[dict[str, str | tuple | dict[str, str] | dict]]

def get_socket_number_linux(location: str = "/sys/devices/system/node/possible") -> int:
    with open(location, 'r') as f:
        data = f.read()
    return int(data.split('-')[-1])+1


def is_set(id: int, reg_idx: int, bit: int) -> str:
    regs = cpuid(id)

    if (1 << bit) & regs[reg_idx]:
        return "Yes"
    else:
        return "--"

def get_cpus() -> CpuInfo:
    cpu_info = []
    for cpu_socket in range(get_socket_number_linux()):
        cpu_info.append({
            "vendor": cpu_vendor(),
            "name": cpu_name(),
            "microarch": cpu_microarchitecture(),
            "vector_instructions": {
                "sse": is_set(1, 3, 25),
                "sse2": is_set(1, 3, 26),
                "sse3": is_set(1, 2, 0),
                "ssse3": is_set(1, 2, 9),
                "sse4.1": is_set(1, 2, 19),
                "sse4.2": is_set(1, 2, 20),
                "sse4a": is_set(0x80000001, 2, 6),
                "avx": is_set(1, 2, 28),
                "avx2": is_set(7, 1, 5),
                "bmi1": is_set(7, 1, 3),
                "bmi2": is_set(7, 1, 8),
            },
            "cpu_info": get_cpu_info(),
        })
    return cpu_info
