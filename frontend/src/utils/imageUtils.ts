import React from 'react';
import { ExternalLink } from 'lucide-react';
import { ChatProductItem } from '../types';

export const CATEGORY_FALLBACK_IMAGES: Record<string, string> = {
  // Fashion & Clothing
  'womens-clothing': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=600&auto=format&fit=crop&q=80',
  'dress': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=600&auto=format&fit=crop&q=80',
  'dresses': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=600&auto=format&fit=crop&q=80',
  'clothing': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=600&auto=format&fit=crop&q=80',
  'fashion': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=600&auto=format&fit=crop&q=80',
  'footwear': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80',
  'shoes': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80',

  // Electronics & Computing
  'electronics': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80',
  'laptops': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80',
  'laptop': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80',
  'computers': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80',
  'mobile-phones': 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&auto=format&fit=crop&q=80',
  'smartphones': 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&auto=format&fit=crop&q=80',
  'audio': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80',
  'headphones': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80',
  'television': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=600&auto=format&fit=crop&q=80',

  // Home & Living
  'home-furniture': 'https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80',
  'kitchen-appliances': 'https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80',
  'airfryer': 'https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80',
  'home-appliances': 'https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&auto=format&fit=crop&q=80',
  'washing-machine': 'https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&auto=format&fit=crop&q=80',
  'office-chairs': 'https://images.unsplash.com/photo-1592078615290-033ee584e267?w=600&auto=format&fit=crop&q=80',
  'office-products': 'https://images.unsplash.com/photo-1592078615290-033ee584e267?w=600&auto=format&fit=crop&q=80',
  
  // Others
  'beauty-personal-care': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=600&auto=format&fit=crop&q=80',
  'skincare': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=600&auto=format&fit=crop&q=80',
  'health-fitness': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600&auto=format&fit=crop&q=80',
  'books-education': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&auto=format&fit=crop&q=80',
  'automotive': 'https://images.unsplash.com/photo-1508974239320-0a029497e820?w=600&auto=format&fit=crop&q=80',
  'jewellery-watches': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80',
  'travel-luggage': 'https://images.unsplash.com/photo-1565026057447-bc90a3dceb87?w=600&auto=format&fit=crop&q=80',
  'musical-instruments': 'https://images.unsplash.com/photo-1510915361894-db8b60106cb1?w=600&auto=format&fit=crop&q=80'
};

export const DEFAULT_FALLBACK_IMAGE = 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80';

export function getCategoryFallback(category?: string, subcategory?: string, name?: string): string {
  const text = `${category || ''} ${subcategory || ''} ${name || ''}`.toLowerCase();
  
  if (text.includes('dress') || text.includes('kurti') || text.includes('saree') || text.includes('clothing') || text.includes('women')) {
    return CATEGORY_FALLBACK_IMAGES['womens-clothing'];
  }
  if (text.includes('shoe') || text.includes('footwear') || text.includes('sneaker') || text.includes('running')) {
    return CATEGORY_FALLBACK_IMAGES['footwear'];
  }
  if (text.includes('air fryer') || text.includes('airfryer') || text.includes('cooker')) {
    return CATEGORY_FALLBACK_IMAGES['airfryer'];
  }
  if (text.includes('washing') || text.includes('front load') || text.includes('top load')) {
    return CATEGORY_FALLBACK_IMAGES['washing-machine'];
  }
  if (text.includes('chair') || text.includes('desk') || text.includes('ergonomic')) {
    return CATEGORY_FALLBACK_IMAGES['office-chairs'];
  }
  if (text.includes('phone') || text.includes('mobile') || text.includes('iphone') || text.includes('samsung galaxy') || text.includes('pixel')) {
    return CATEGORY_FALLBACK_IMAGES['mobile-phones'];
  }
  if (text.includes('earbud') || text.includes('headphone') || text.includes('airpod') || text.includes('audio')) {
    return CATEGORY_FALLBACK_IMAGES['audio'];
  }
  if (text.includes('watch') || text.includes('titan') || text.includes('smartwatch')) {
    return CATEGORY_FALLBACK_IMAGES['jewellery-watches'];
  }
  if (text.includes('skin') || text.includes('serum') || text.includes('cream') || text.includes('beauty')) {
    return CATEGORY_FALLBACK_IMAGES['beauty-personal-care'];
  }
  if (text.includes('laptop') || text.includes('notebook') || text.includes('macbook') || text.includes('asus') || text.includes('lenovo')) {
    return CATEGORY_FALLBACK_IMAGES['laptops'];
  }
  
  if (category && CATEGORY_FALLBACK_IMAGES[category.toLowerCase()]) {
    return CATEGORY_FALLBACK_IMAGES[category.toLowerCase()];
  }
  
  return DEFAULT_FALLBACK_IMAGE;
}

export function getSafeProductImage(product?: ChatProductItem | any): string {
  if (!product) return DEFAULT_FALLBACK_IMAGE;
  const rawUrl = product.image_url || product.image || (product.images && product.images[0]);
  if (rawUrl && typeof rawUrl === 'string' && rawUrl.startsWith('http')) {
    return rawUrl;
  }
  return getCategoryFallback(product.category, product.subcategory, product.name || product.product_name);
}

export function handleImageError(
  e: React.SyntheticEvent<HTMLImageElement, Event>,
  category?: string,
  subcategory?: string,
  name?: string
) {
  const target = e.currentTarget;
  const fallback = getCategoryFallback(category, subcategory, name);
  if (target.src !== fallback) {
    target.src = fallback;
  } else if (target.src !== DEFAULT_FALLBACK_IMAGE) {
    target.src = DEFAULT_FALLBACK_IMAGE;
  }
}
