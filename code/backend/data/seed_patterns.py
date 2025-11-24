"""
Seed design patterns for the DELM knowledge base
"""

SEED_PATTERNS = [
    # Component Patterns
    {
        "pattern_id": "comp-001",
        "name": "Button Component",
        "category": "components",
        "tags": ["button", "interactive", "form"],
        "content": """
import React from 'react';
import { clsx } from 'clsx';

interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  disabled = false,
  onClick,
  className
}) => {
  const baseStyles = 'inline-flex items-center justify-center font-medium rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2';

  const variants = {
    primary: 'bg-primary-600 text-white hover:bg-primary-700 focus:ring-primary-500',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500',
    outline: 'border-2 border-primary-600 text-primary-600 hover:bg-primary-50 focus:ring-primary-500',
    ghost: 'text-gray-600 hover:bg-gray-100 focus:ring-gray-500'
  };

  const sizes = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };

  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={clsx(
        baseStyles,
        variants[variant],
        sizes[size],
        disabled && 'opacity-50 cursor-not-allowed',
        className
      )}
    >
      {children}
    </button>
  );
};
"""
    },
    {
        "pattern_id": "comp-002",
        "name": "Card Component",
        "category": "components",
        "tags": ["card", "container", "content"],
        "content": """
import React from 'react';
import { clsx } from 'clsx';

interface CardProps {
  children: React.ReactNode;
  title?: string;
  subtitle?: string;
  image?: string;
  footer?: React.ReactNode;
  className?: string;
  hoverable?: boolean;
}

export const Card: React.FC<CardProps> = ({
  children,
  title,
  subtitle,
  image,
  footer,
  className,
  hoverable = false
}) => {
  return (
    <div
      className={clsx(
        'bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden',
        'border border-gray-200 dark:border-gray-700',
        hoverable && 'hover:shadow-lg transition-shadow cursor-pointer',
        className
      )}
    >
      {image && (
        <img
          src={image}
          alt={title || 'Card image'}
          className="w-full h-48 object-cover"
        />
      )}
      <div className="p-6">
        {title && (
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
            {title}
          </h3>
        )}
        {subtitle && (
          <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
            {subtitle}
          </p>
        )}
        <div className="mt-4">{children}</div>
      </div>
      {footer && (
        <div className="px-6 py-4 bg-gray-50 dark:bg-gray-700 border-t border-gray-200 dark:border-gray-600">
          {footer}
        </div>
      )}
    </div>
  );
};
"""
    },
    {
        "pattern_id": "comp-003",
        "name": "Input Component",
        "category": "components",
        "tags": ["input", "form", "text"],
        "content": """
import React from 'react';
import { clsx } from 'clsx';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helperText?: string;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

export const Input: React.FC<InputProps> = ({
  label,
  error,
  helperText,
  leftIcon,
  rightIcon,
  className,
  id,
  ...props
}) => {
  const inputId = id || label?.toLowerCase().replace(/\\s+/g, '-');

  return (
    <div className="w-full">
      {label && (
        <label
          htmlFor={inputId}
          className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
        >
          {label}
        </label>
      )}
      <div className="relative">
        {leftIcon && (
          <div className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400">
            {leftIcon}
          </div>
        )}
        <input
          id={inputId}
          className={clsx(
            'w-full px-4 py-2 border rounded-lg',
            'bg-white dark:bg-gray-800',
            'text-gray-900 dark:text-white',
            'focus:outline-none focus:ring-2 focus:ring-primary-500',
            'transition-colors',
            error
              ? 'border-red-500 focus:ring-red-500'
              : 'border-gray-300 dark:border-gray-600',
            leftIcon && 'pl-10',
            rightIcon && 'pr-10',
            className
          )}
          {...props}
        />
        {rightIcon && (
          <div className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400">
            {rightIcon}
          </div>
        )}
      </div>
      {error && (
        <p className="mt-1 text-sm text-red-500">{error}</p>
      )}
      {helperText && !error && (
        <p className="mt-1 text-sm text-gray-500">{helperText}</p>
      )}
    </div>
  );
};
"""
    },
    # Layout Patterns
    {
        "pattern_id": "layout-001",
        "name": "Sidebar Layout",
        "category": "layouts",
        "tags": ["sidebar", "dashboard", "navigation"],
        "content": """
import React from 'react';

interface SidebarLayoutProps {
  sidebar: React.ReactNode;
  children: React.ReactNode;
  sidebarWidth?: string;
}

export const SidebarLayout: React.FC<SidebarLayoutProps> = ({
  sidebar,
  children,
  sidebarWidth = 'w-64'
}) => {
  return (
    <div className="min-h-screen flex">
      <aside className={`${sidebarWidth} bg-gray-900 text-white flex-shrink-0`}>
        {sidebar}
      </aside>
      <main className="flex-1 overflow-auto bg-gray-50 dark:bg-gray-900">
        {children}
      </main>
    </div>
  );
};
"""
    },
    {
        "pattern_id": "layout-002",
        "name": "Grid Layout",
        "category": "layouts",
        "tags": ["grid", "responsive", "columns"],
        "content": """
import React from 'react';
import { clsx } from 'clsx';

interface GridLayoutProps {
  children: React.ReactNode;
  cols?: 1 | 2 | 3 | 4 | 6 | 12;
  gap?: 'sm' | 'md' | 'lg';
  className?: string;
}

export const GridLayout: React.FC<GridLayoutProps> = ({
  children,
  cols = 3,
  gap = 'md',
  className
}) => {
  const colClasses = {
    1: 'grid-cols-1',
    2: 'grid-cols-1 md:grid-cols-2',
    3: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    4: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-4',
    6: 'grid-cols-2 md:grid-cols-3 lg:grid-cols-6',
    12: 'grid-cols-4 md:grid-cols-6 lg:grid-cols-12'
  };

  const gapClasses = {
    sm: 'gap-2',
    md: 'gap-4',
    lg: 'gap-6'
  };

  return (
    <div className={clsx('grid', colClasses[cols], gapClasses[gap], className)}>
      {children}
    </div>
  );
};
"""
    },
    # Style Patterns
    {
        "pattern_id": "style-001",
        "name": "Design Tokens",
        "category": "styles",
        "tags": ["tokens", "colors", "spacing"],
        "content": """
// Design Tokens - Tailwind CSS Configuration

const colors = {
  primary: {
    50: '#f0f9ff',
    100: '#e0f2fe',
    200: '#bae6fd',
    300: '#7dd3fc',
    400: '#38bdf8',
    500: '#0ea5e9',
    600: '#0284c7',
    700: '#0369a1',
    800: '#075985',
    900: '#0c4a6e',
  },
  gray: {
    50: '#f9fafb',
    100: '#f3f4f6',
    200: '#e5e7eb',
    300: '#d1d5db',
    400: '#9ca3af',
    500: '#6b7280',
    600: '#4b5563',
    700: '#374151',
    800: '#1f2937',
    900: '#111827',
  },
  success: '#10b981',
  warning: '#f59e0b',
  error: '#ef4444',
  info: '#3b82f6',
};

const spacing = {
  xs: '0.25rem',
  sm: '0.5rem',
  md: '1rem',
  lg: '1.5rem',
  xl: '2rem',
  '2xl': '3rem',
};

const typography = {
  fontFamily: {
    sans: ['Inter', 'system-ui', 'sans-serif'],
    mono: ['Fira Code', 'monospace'],
  },
  fontSize: {
    xs: '0.75rem',
    sm: '0.875rem',
    base: '1rem',
    lg: '1.125rem',
    xl: '1.25rem',
    '2xl': '1.5rem',
    '3xl': '1.875rem',
  },
};

export { colors, spacing, typography };
"""
    },
    {
        "pattern_id": "style-002",
        "name": "Animation Utilities",
        "category": "styles",
        "tags": ["animation", "transitions", "motion"],
        "content": """
// Animation and Transition Utilities

// Tailwind CSS animations
const animations = {
  // Fade animations
  fadeIn: 'animate-[fadeIn_0.3s_ease-in-out]',
  fadeOut: 'animate-[fadeOut_0.3s_ease-in-out]',

  // Slide animations
  slideUp: 'animate-[slideUp_0.3s_ease-out]',
  slideDown: 'animate-[slideDown_0.3s_ease-out]',
  slideLeft: 'animate-[slideLeft_0.3s_ease-out]',
  slideRight: 'animate-[slideRight_0.3s_ease-out]',

  // Scale animations
  scaleIn: 'animate-[scaleIn_0.2s_ease-out]',
  scaleOut: 'animate-[scaleOut_0.2s_ease-in]',

  // Spin and pulse
  spin: 'animate-spin',
  pulse: 'animate-pulse',
  bounce: 'animate-bounce',
};

// Transition classes
const transitions = {
  default: 'transition-all duration-200 ease-in-out',
  fast: 'transition-all duration-100 ease-in-out',
  slow: 'transition-all duration-500 ease-in-out',
  colors: 'transition-colors duration-200',
  transform: 'transition-transform duration-200',
  opacity: 'transition-opacity duration-200',
};

// Keyframes for tailwind.config.js
const keyframes = {
  fadeIn: {
    '0%': { opacity: '0' },
    '100%': { opacity: '1' },
  },
  slideUp: {
    '0%': { transform: 'translateY(10px)', opacity: '0' },
    '100%': { transform: 'translateY(0)', opacity: '1' },
  },
  scaleIn: {
    '0%': { transform: 'scale(0.95)', opacity: '0' },
    '100%': { transform: 'scale(1)', opacity: '1' },
  },
};

export { animations, transitions, keyframes };
"""
    },
    # Accessibility Pattern
    {
        "pattern_id": "a11y-001",
        "name": "Accessible Modal",
        "category": "accessibility",
        "tags": ["modal", "dialog", "a11y", "focus-trap"],
        "content": """
import React, { useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}

export const Modal: React.FC<ModalProps> = ({
  isOpen,
  onClose,
  title,
  children
}) => {
  const modalRef = useRef<HTMLDivElement>(null);
  const previousFocus = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      previousFocus.current = document.activeElement as HTMLElement;
      modalRef.current?.focus();

      const handleKeyDown = (e: KeyboardEvent) => {
        if (e.key === 'Escape') onClose();
      };
      document.addEventListener('keydown', handleKeyDown);
      return () => document.removeEventListener('keydown', handleKeyDown);
    } else {
      previousFocus.current?.focus();
    }
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return createPortal(
    <div
      className="fixed inset-0 z-50 flex items-center justify-center"
      role="presentation"
    >
      <div
        className="absolute inset-0 bg-black/50"
        onClick={onClose}
        aria-hidden="true"
      />
      <div
        ref={modalRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        tabIndex={-1}
        className="relative bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-lg w-full mx-4 p-6"
      >
        <h2 id="modal-title" className="text-xl font-semibold mb-4">
          {title}
        </h2>
        {children}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 text-gray-400 hover:text-gray-600"
          aria-label="Close modal"
        >
          ×
        </button>
      </div>
    </div>,
    document.body
  );
};
"""
    },
]


def seed_database(rag_pipeline):
    """Seed the database with initial design patterns"""
    print(f"Seeding database with {len(SEED_PATTERNS)} patterns...")

    for pattern in SEED_PATTERNS:
        rag_pipeline.add_pattern(
            pattern_id=pattern['pattern_id'],
            content=pattern['content'],
            category=pattern['category'],
            name=pattern['name'],
            tags=pattern.get('tags', [])
        )

    print(f"Database seeded successfully! Total patterns: {rag_pipeline.vector_store.count()}")


if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from src.rag import RAGPipeline

    pipeline = RAGPipeline()
    seed_database(pipeline)
