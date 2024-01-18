import machine
import gc

total_memory = 4194304 # bytes

def getPercentageMemoryFree():
    # Get the amount of free memory (bytes)
    free_memory = gc.mem_free()

    # Calculate the percentage of free memory
    percentage_free = (free_memory / total_memory) * 100

    return percentage_free

def getMemoryUsage():
    # Get the amount of free memory (bytes)
    free_memory = gc.mem_free()

    # Calculate the percentage of free memory
    memory_bytes = total_memory - free_memory

    memory_percentage = (memory_bytes / total_memory) * 100

    return memory_bytes, memory_percentage
