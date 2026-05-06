import pandas as pd
from google_play_scraper import reviews_all, Sort
import argparse
from datetime import datetime

def scrape_reviews(app_id='com.tiket.gits', lang='id', country='id', max_samples=20000):
    print(f"Starting scraping for app: {app_id}")
    print(f"Language: {lang}, Country: {country}")
    print("This may take several minutes...\n")
    
    try:
        scrapreview = reviews_all(
            app_id,
            lang=lang,
            country=country,
            sort=Sort.MOST_RELEVANT
        )
        
        df = pd.DataFrame(scrapreview)
        print(f"✓ Total reviews scraped: {len(df)}")
        
        if max_samples and len(df) > max_samples:
            df = df.sample(n=max_samples, random_state=42).reset_index(drop=True)
            print(f"✓ Sampled to: {len(df)} reviews")
        
        return df
        
    except Exception as e:
        print(f"✗ Error during scraping: {e}")
        return None

def save_reviews(df, output_file='raw_reviews.csv'):
    if df is not None and not df.empty:
        df.to_csv(output_file, index=False)
        print(f"\n✓ Reviews saved to: {output_file}")
        print(f"  Total rows: {len(df)}")
        print(f"  Columns: {', '.join(df.columns.tolist())}")
        
        print("\n=== Basic Statistics ===")
        print(f"Date range: {df['at'].min()} to {df['at'].max()}")
        print(f"\nScore distribution:")
        print(df['score'].value_counts().sort_index())
        print(f"\nReviews with content: {df['content'].notna().sum()}")
        print(f"Reviews with reply: {df['replyContent'].notna().sum()}")
    else:
        print("✗ No data to save")

def main():
    parser = argparse.ArgumentParser(description='Scrape Google Play Store reviews')
    parser.add_argument('--app-id', type=str, default='com.tiket.gits',
                        help='Package name of the app (default: com.tiket.gits)')
    parser.add_argument('--lang', type=str, default='id',
                        help='Language code (default: id)')
    parser.add_argument('--country', type=str, default='id',
                        help='Country code (default: id)')
    parser.add_argument('--max-samples', type=int, default=20000,
                        help='Maximum number of samples (default: 20000, use 0 for all)')
    parser.add_argument('--output', type=str, default='raw_reviews.csv',
                        help='Output CSV file name (default: raw_reviews.csv)')
    
    args = parser.parse_args()
    
    max_samples = None if args.max_samples == 0 else args.max_samples
    
    print("="*60)
    print("Google Play Store Review Scraper")
    print("="*60)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    df = scrape_reviews(
        app_id=args.app_id,
        lang=args.lang,
        country=args.country,
        max_samples=max_samples
    )

    if df is not None:
        save_reviews(df, args.output)
        print("\n" + "="*60)
        print("✓ Scraping completed successfully!")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("✗ Scraping failed!")
        print("="*60)

if __name__ == "__main__":
    main()
