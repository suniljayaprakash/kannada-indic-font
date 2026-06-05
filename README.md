# Nanni Indic Font

**Nanni Indic Font** is a beautiful, modern handwriting font designed primarily for Indic scripts, with comprehensive support for Kannada, English, and Vedic Extended characters.

The font features precise typographic rules for complex text shaping, including support for multi-level _vattu_ (ಒತ್ತಕ್ಷರ), proper _halant_ rendering, and seamless _zwj_ interactions to ensure Kannada text is displayed elegantly and accurately.

## 🌟 Features

- **Indic Script Support:** Tailored specifically for Kannada, handling complex conjugations, _ottaksara_ (vattu), and halant interactions beautifully.
- **Vedic Extensions:** Full support for Vedic Extended characters and tone marks, making it ideal for ancient texts and mantras.
- **Broad Character Sets:** Includes standard and extended English characters, numerals, and an extensive array of global currency symbols.
- **Multi-format Delivery:** Available in `.ttf`, `.otf`, `.woff`, and `.woff2` formats for desktop and web use.
- **Open Source:** Licensed under the SIL Open Font License (OFL) v1.1.

## 👁️ Preview

You can try out the font and view character samples on the [Showcase Page](https://suniljayaprakash.github.io/nanni-indic-font/).

## 🔠 Supported Scripts & Characters

- **Kannada:** Vowels, consonants, numbers, symbols, and complex conjuncts (multi-level vattu). Includes special handling for characters like ಱ, ೞ, ಞ, and ಝ.
- **English:** Basic Latin uppercase, lowercase, numbers, and common punctuation.
- **Vedic Extended:** Mantras and Vedic tone marks.
- **Currency Symbols:** Extensive support (e.g., ₹, $, €, £, ₪, ฿, ₿).

## 📥 Installation

1. Go to the [`docs/builds`](./docs/builds) directory in this repository.
2. Download the font format of your choice:
   - `Nanni-Regular.ttf` (Standard for most OS and apps)
   - `Nanni-Regular.otf` (Best for professional typography)
   - `Nanni-Regular.woff` / `Nanni-Regular.woff2` (Best for web development)
3. **Windows:** Double-click the downloaded file and click "Install".
4. **macOS:** Double-click the downloaded file and click "Install Font" in Font Book.
5. **Linux:** Copy the font files to `~/.local/share/fonts/` or `/usr/share/fonts/` and run `fc-cache -f -v`.

## 🌐 Web Usage

To use Nanni Indic Font on your website, include the WOFF or WOFF2 files in your CSS via `@font-face`:

```css
@font-face {
  font-family: "Nanni";
  src:
    url("path/to/Nanni-Regular.woff2") format("woff2"),
    url("path/to/Nanni-Regular.woff") format("woff");
  font-weight: normal;
  font-style: normal;
}

body {
  font-family: "Nanni", sans-serif;
}
```

## 📄 License

This Font Software is licensed under the **SIL Open Font License, Version 1.1**.
This license is copied below, and is also available with a FAQ at:
[http://scripts.sil.org/OFL](http://scripts.sil.org/OFL)

## 💬 Support & Feedback

If you find this font useful, run into rendering issues, or have suggestions for improvements, please don't hesitate to reach out. Love to hear from you!

- **Author:** Sunil Jayaprakash
- **Email:** [sunil.jayaprakash@gmail.com](mailto:sunil.jayaprakash@gmail.com)
