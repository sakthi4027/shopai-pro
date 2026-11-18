import React from 'react';

interface RobotAvatarProps {
  className?: string;
  size?: number;
}

export function RobotAvatar({ className = '', size = 64 }: RobotAvatarProps) {
  return (
    <div
      className={`relative inline-flex items-center justify-center select-none ${className}`}
      style={{ width: size, height: size }}
    >
      <svg
        viewBox="0 0 120 120"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="w-full h-full drop-shadow-md"
      >
        <defs>
          <linearGradient id="headGrad" x1="20" y1="20" x2="100" y2="100" gradientUnits="userSpaceOnUse">
            <stop stopColor="#FFFFFF" />
            <stop offset="0.7" stopColor="#EEF2FF" />
            <stop offset="1" stopColor="#C7D2FE" />
          </linearGradient>
          <linearGradient id="earGrad" x1="0" y1="0" x2="30" y2="30" gradientUnits="userSpaceOnUse">
            <stop stopColor="#6366F1" />
            <stop offset="1" stopColor="#4338CA" />
          </linearGradient>
          <linearGradient id="visorGrad" x1="30" y1="35" x2="90" y2="70" gradientUnits="userSpaceOnUse">
            <stop stopColor="#1E1B4B" />
            <stop offset="1" stopColor="#0F172A" />
          </linearGradient>
          <linearGradient id="eyeGrad" x1="0" y1="0" x2="10" y2="10" gradientUnits="userSpaceOnUse">
            <stop stopColor="#38BDF8" />
            <stop offset="1" stopColor="#0284C7" />
          </linearGradient>
          <linearGradient id="antennaGrad" x1="0" y1="0" x2="10" y2="15" gradientUnits="userSpaceOnUse">
            <stop stopColor="#818CF8" />
            <stop offset="1" stopColor="#4F46E5" />
          </linearGradient>
        </defs>

        {/* Antenna */}
        <circle cx="60" cy="12" r="5" fill="url(#earGrad)" />
        <rect x="58" y="16" width="4" height="10" rx="2" fill="url(#antennaGrad)" />

        {/* Ears / Headphone Cuffs */}
        <rect x="14" y="38" width="12" height="26" rx="6" fill="url(#earGrad)" />
        <rect x="94" y="38" width="12" height="26" rx="6" fill="url(#earGrad)" />

        {/* Main Head Base */}
        <rect x="22" y="24" width="76" height="54" rx="24" fill="url(#headGrad)" stroke="#E0E7FF" strokeWidth="1.5" />

        {/* Face Visor */}
        <rect x="30" y="34" width="60" height="34" rx="14" fill="url(#visorGrad)" />

        {/* Glowing Digital Eyes */}
        <ellipse cx="46" cy="51" rx="5.5" ry="7" fill="url(#eyeGrad)" />
        <circle cx="48" cy="48" r="2" fill="#FFFFFF" opacity="0.9" />

        <ellipse cx="74" cy="51" rx="5.5" ry="7" fill="url(#eyeGrad)" />
        <circle cx="76" cy="48" r="2" fill="#FFFFFF" opacity="0.9" />

        {/* Friendly Blush or Visor Highlight */}
        <ellipse cx="36" cy="59" rx="3" ry="1.5" fill="#38BDF8" opacity="0.4" />
        <ellipse cx="84" cy="59" rx="3" ry="1.5" fill="#38BDF8" opacity="0.4" />

        {/* Torso / Body Peek */}
        <path d="M34 82 C34 76, 86 76, 86 82 L90 106 C90 112, 30 112, 30 106 Z" fill="url(#headGrad)" stroke="#E0E7FF" strokeWidth="1" />

        {/* Chest Star Emblem */}
        <path
          d="M60 88 L62 93 L67 93.5 L63 97 L64.5 102 L60 99 L55.5 102 L57 97 L53 93.5 L58 93 Z"
          fill="#6366F1"
        />

        {/* Floating Hands */}
        <ellipse cx="26" cy="95" rx="6" ry="7" fill="url(#headGrad)" stroke="#E0E7FF" strokeWidth="1" />
        <ellipse cx="94" cy="95" rx="6" ry="7" fill="url(#headGrad)" stroke="#E0E7FF" strokeWidth="1" />
      </svg>
    </div>
  );
}
