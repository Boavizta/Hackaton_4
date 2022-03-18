import json
import subprocess

from typing import List


CONVERT_B_IN_GB = 9.313e-10
CONVERT_KB_IN_GB = 9.536e-7


def get_ram_info():
    try:
        return get_ram_info_with_lshw()
    except (PermissionError, KeyError):
        print('cannot access lshw without super-user using meminfo as fallback method')
        return get_ram_info_with_meminfo()


def get_ram_info_with_lshw() -> List[dict]:
    lshw_out = exec_lshw()
    memory_banks = parse_lshw_for_memory_components(lshw_out)
    memory_banks_info = parse_memory_children(memory_banks)
    return memory_banks_info


def exec_lshw() -> dict:
    proc = subprocess.Popen(['lshw', '-json'], stdout=subprocess.PIPE)
    out = proc.stdout.read()
    return json.loads(out)


def parse_lshw_for_memory_components(lshw_output: dict) -> List[dict]:
    if isinstance(lshw_output, list):
        assert len(lshw_output) == 1
        node = lshw_output[0]
    else:
        node = lshw_output
    for node_child in node['children']:
        if node_child['id'] == 'core':
            for core_child in node_child['children']:
                if core_child['id'] == 'memory':
                    return core_child['children']


def parse_memory_children(memory_children: List[dict]) -> List[dict]:
    memory_banks_info = []
    for mem_bank in memory_children:
        memory_banks_info.append({
            'manufacturer': mem_bank['vendor'],
            'model': mem_bank['product'],
            'capacity': convert_bytes_in_gb(mem_bank['size'])
        })
    return memory_banks_info


def get_ram_info_with_meminfo() -> List[dict]:
    memory_size_kb = get_total_memory_in_kb()
    memory_size_gb = convert_kb_in_gb(memory_size_kb)
    return [{
        'capcity': memory_size_gb
    }]


def get_total_memory_in_kb() -> int:
    with open('/proc/meminfo', 'r') as f:
        for line in f.readlines():
            if 'MemTotal' in line:
                mem_total_line = line.strip()
                break
    total_size_kb = int(mem_total_line.split()[0])
    return total_size_kb


def convert_kb_in_gb(value: int) -> float:
    return round(value * CONVERT_KB_IN_GB, 2)


def convert_bytes_in_gb(value: int) -> float:
    return round(value * CONVERT_B_IN_GB, 2)


if __name__ == '__main__':
    print(get_ram_info())
