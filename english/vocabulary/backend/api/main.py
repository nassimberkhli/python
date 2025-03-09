from cli import parse_arguments
from wordreference import fetch_translation
from presentation import print_translations, print_examples

def main():
    args = parse_arguments()
    translations, audio_links = fetch_translation(args.word, args.dictionary_code)
    if translations is None:
        print(f"Failed to fetch translations: {audio_links}")  # audio_links contains error message
        return

    if args.sentences:
        print_examples(translations)
    else:
        print_translations(translations)

    if args.audio:
        if audio_links:
            print("Downloading audio files...")
            download_audio(args.word, audio_links)
            print("Finished downloading audio files.")
        else:
            print("No audio files available for this word.")

if __name__ == '__main__':
    main()
