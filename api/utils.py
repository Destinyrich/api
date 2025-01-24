import subprocess

def generate_video_resolutions(video_file_path):
    """
    Generates different resolutions of a given video file using FFmpeg.
    Returns a dictionary of resolutions and their corresponding file paths.
    """
    resolutions = ['360p', '480p', '720p', '1080p']
    output_files = {}

    for resolution in resolutions:
        output_file = f'{video_file_path}_{resolution}.mp4'
        # Construct FFmpeg command for each resolution
        command = [
            'ffmpeg',
            '-i', video_file_path,
            '-s', resolution,
            '-c:a', 'copy',  # Audio stream copy
            output_file
        ]
        try:
            # Run FFmpeg command to generate the video at the specified resolution
            subprocess.run(command, check=True)
            output_files[resolution] = output_file
        except subprocess.CalledProcessError as e:
            print(f"Error processing resolution {resolution}: {e}")

    return output_files
