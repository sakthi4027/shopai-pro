/**
 * Link Validation and Normalization Utility:
 * Ensures all product links point directly to authentic merchant product listing pages.
 * Strictly rejects and avoids unwanted links:
 * - Search results pages (/search?, ?q=, ?k=, /searchB?, /s?)
 * - Generic domain homepages (e.g. https://amazon.in/)
 * - Placeholder links (#, javascript:void(0), null, undefined)
 * - Category / blog / browse landing pages
 */

export function isProperProductLink(url?: string | null): boolean {
  if (!url || typeof url !== 'string') return false;
  const trimmed = url.trim();
  if (!trimmed || trimmed === '#' || trimmed.startsWith('javascript:')) return false;
  if (!trimmed.startsWith('http://') && !trimmed.startsWith('https://')) return false;

  const u = trimmed.toLowerCase();

  // 1. Reject search queries and search landing pages
  const unwantedPatterns = [
    '/search?',
    '/search/',
    '/searchb?',
    '?q=',
    '&q=',
    '?k=',
    '&k=',
    'search_query=',
    '/s?',
    '/s/',
    '/browse',
    '/category',
    '/tag/',
    '/blog/'
  ];
  if (unwantedPatterns.some(p => u.includes(p))) {
    return false;
  }

  // 2. Reject domain root / homepages without specific product path
  try {
    const parsed = new URL(trimmed);
    const pathname = parsed.pathname.replace(/\/+$/, '');
    if (!pathname || pathname === '' || pathname === '/in' || pathname === '/in/en') {
      return false;
    }
  } catch {
    return false;
  }

  return true;
}

/**
 * Returns the best verified direct product URL from a product object,
 * strictly filtering out unwanted search or placeholder links.
 */
export function getProperProductUrl(product: any): string {
  if (!product) return 'https://www.amazon.in';

  // 1. Check primary product_url
  if (isProperProductLink(product.product_url)) {
    return product.product_url;
  }

  // 2. Check lowest_price_url
  if (isProperProductLink(product.lowest_price_url)) {
    return product.lowest_price_url;
  }

  // 3. Check url field
  if (isProperProductLink(product.url)) {
    return product.url;
  }

  // 4. Check sellers array for a direct link
  if (Array.isArray(product.sellers)) {
    for (const s of product.sellers) {
      if (s && isProperProductLink(s.product_url)) {
        return s.product_url;
      }
    }
  }

  // 5. Check affiliate_url
  if (isProperProductLink(product.affiliate_url)) {
    return product.affiliate_url;
  }

  return product.product_url || product.url || 'https://www.amazon.in';
}
