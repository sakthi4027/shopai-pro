import React from 'react';
import { ExternalLink } from 'lucide-react';
import { isProperProductLink } from '../../utils/linkUtils';

interface MarkdownContentProps {
  content: string;
}

export function MarkdownContent({ content }: MarkdownContentProps) {
  if (!content) return null;

  // Split into lines or paragraphs
  const lines = content.split('\n');

  // Helper to parse inline markdown: links [text](url), bold **text**, and bare URLs
  const renderInlineFormatted = (text: string) => {
    // Regex for:
    // 1. Markdown link: \[([^\]]+)\]\((https?:\/\/[^\s\)]+)\)
    // 2. Bold text: \*\*([^*]+)\*\*
    // 3. Bare URL: (https?:\/\/[^\s]+)
    const combinedRegex = /(\[[^\]]+\]\(https?:\/\/[^\s\)]+\)|\*\*[^*]+\*\*|https?:\/\/[^\s\)]+)/g;
    const parts = text.split(combinedRegex);

    return parts.map((part, index) => {
      if (!part) return null;

      // Check for Markdown Link: [Title](URL)
      const linkMatch = part.match(/^\[([^\]]+)\]\((https?:\/\/[^\s\)]+)\)$/);
      if (linkMatch) {
        const [, label, url] = linkMatch;
        // Strictly avoid unwanted links (search queries, homepages, generic listings)
        if (!isProperProductLink(url)) {
          return (
            <span key={index} className="font-semibold text-slate-800 mx-0.5">
              {label}
            </span>
          );
        }

        return (
          <a
            key={index}
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            onClick={(e) => {
              e.stopPropagation();
              window.open(url, '_blank');
            }}
            className="inline-flex items-center gap-1 font-bold text-indigo-600 hover:text-indigo-800 underline hover:no-underline transition-all cursor-pointer bg-indigo-50 hover:bg-indigo-100/80 px-2 py-0.5 rounded-md border border-indigo-200/70 shadow-2xs mx-1"
            title={`Open official product listing on store`}
          >
            <span>{label}</span>
            <ExternalLink className="w-3 h-3 inline text-indigo-600" />
          </a>
        );
      }

      // Check for Bold text: **bold**
      const boldMatch = part.match(/^\*\*([^*]+)\*\*$/);
      if (boldMatch) {
        return (
          <strong key={index} className="font-bold text-slate-900">
            {boldMatch[1]}
          </strong>
        );
      }

      // Check for bare URL: https://...
      const urlMatch = part.match(/^https?:\/\/[^\s]+$/);
      if (urlMatch) {
        return (
          <a
            key={index}
            href={part}
            target="_blank"
            rel="noopener noreferrer"
            onClick={(e) => {
              e.stopPropagation();
              window.open(part, '_blank');
            }}
            className="inline-flex items-center gap-1 font-semibold text-indigo-600 hover:text-indigo-800 underline transition-all cursor-pointer mx-1"
            title={`Open ${part} in a new window`}
          >
            <span className="truncate max-w-xs">{part}</span>
            <ExternalLink className="w-3 h-3 inline" />
          </a>
        );
      }

      return <span key={index}>{part}</span>;
    });
  };

  return (
    <div className="space-y-2.5 text-slate-800 leading-relaxed text-xs sm:text-sm">
      {lines.map((line, idx) => {
        const trimmed = line.trim();

        if (!trimmed) {
          return <div key={idx} className="h-1.5" />;
        }

        // Section Heading: ### Title
        if (trimmed.startsWith('### ')) {
          return (
            <h4
              key={idx}
              className="text-sm sm:text-base font-bold text-slate-900 mt-3 mb-1 flex items-center gap-2 border-b border-slate-100 pb-1"
            >
              <span>{trimmed.replace('### ', '')}</span>
            </h4>
          );
        }

        // Sub-heading: ## Title
        if (trimmed.startsWith('## ')) {
          return (
            <h3 key={idx} className="text-base sm:text-lg font-extrabold text-slate-900 mt-4 mb-1">
              {trimmed.replace('## ', '')}
            </h3>
          );
        }

        // Bullet point: - text
        if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
          const itemText = trimmed.replace(/^[-*]\s+/, '');
          return (
            <div key={idx} className="flex items-start gap-2 ml-1 text-slate-700">
              <span className="text-indigo-500 font-bold text-xs mt-0.5">•</span>
              <div className="flex-1 leading-relaxed">{renderInlineFormatted(itemText)}</div>
            </div>
          );
        }

        // Standard paragraph
        return (
          <p key={idx} className="leading-relaxed">
            {renderInlineFormatted(trimmed)}
          </p>
        );
      })}
    </div>
  );
}
