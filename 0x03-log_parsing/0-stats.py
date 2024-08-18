#!/usr/bin/python3
import sys
import signal
import re

# Global variables to keep track of file sizes and status codes
total_size = 0  # Total accumulated file size
status_counts = {}  # Dictionary to count occurrences of each status code
line_counter = 0  # Counter to track the number of lines processed

def show_stats():
    """Print the statistics about file sizes and status codes."""
    global total_size, status_counts
    
    # Print the total accumulated file size
    print(f"File size: {total_size}")
    
    # Print the count of each status code in ascending order
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
    
    # Reset the totals for the next batch
    total_size = 0
    status_counts.clear()

def handle_interrupt(signal, frame):
    """Handle the keyboard interruption signal (CTRL + C)."""
    show_stats()
    sys.exit(0)

def main():
    global line_counter, total_size
    
    # Register the function to handle keyboard interrupts (CTRL + C)
    signal.signal(signal.SIGINT, handle_interrupt)
    
    # Regular expression pattern to match the log line format
    log_pattern = re.compile(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    )
    
    try:
        for line in sys.stdin:
            line_counter += 1
            match = log_pattern.match(line.strip())
            
            if match:
                status_code = match.group(3)  # Extract the status code
                file_size = int(match.group(4))  # Extract and convert the file size
                
                # Update the total file size
                total_size += file_size
                
                # Update the count for the status code
                if status_code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                    if status_code not in status_counts:
                        status_counts[status_code] = 0
                    status_counts[status_code] += 1
            
            # Print statistics every 10 lines
            if line_counter % 10 == 0:
                show_stats()

    except BrokenPipeError:
        # Handle broken pipe error if the generator script is interrupted
        show_stats()

if __name__ == "__main__":
    main()
