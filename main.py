import yt_dlp

def download_bilibili_video(url):
    ydl_opts = {}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        
        # Display all available formats
        print("\nAvailable formats:")
        for i, f in enumerate(formats):
            format_id = f.get('format_id', 'unknown')
            ext = f.get('ext', 'unknown')
            resolution = f.get('resolution') or f'{f.get("height")}p'
            filesize = f.get('filesize', 'unknown')
            filesize_mb = filesize / 1024 / 1024 if isinstance(filesize, int) else 'unknown'
            tbr = f.get('tbr', 'unknown')
            proto = f.get('protocol', 'unknown')
            
            # Display format information
            print(f"{i}: Resolution: {resolution} - Format: {ext} - Filesize: {filesize_mb} MB - TBR: {tbr} kbps - Protocol: {proto}")

        # Filter formats to prioritize 1080p and 720p if available
        prioritized_formats = [f for f in formats if f.get('height') in [1080, 720]]
        
        if not prioritized_formats:
            print("\nNo 1080p or 720p formats found. You can still choose from other available formats.")

        # Ask the user to select a format
        selected_format_index = int(input("\nEnter the number of the format you want to download: "))
        selected_format_id = formats[selected_format_index].get('format_id')

        # Download the selected format
        ydl_opts['format'] = selected_format_id

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the Bilibili video URL: ")
    download_bilibili_video(video_url)
