# HANDS-ON 9: Web Accessibility (a11y) & Cross-Browser Compatibility

## Digital Nurture 5.0 - Module 2: Frontend Development

---

## 📌 Project Title

**Student Portal - Accessibility Enhancement and Cross-Browser Compatibility**

---

# 📖 Overview

This hands-on focuses on improving the accessibility and browser compatibility of the Student Portal web application.

Accessibility (a11y) ensures that websites are usable by everyone, including users with disabilities who depend on assistive technologies such as screen readers and keyboard navigation.

The Student Portal was audited using **Lighthouse** and **axe DevTools** based on **WCAG 2.1 guidelines**. Identified accessibility issues were fixed by improving semantic HTML, adding ARIA attributes, implementing keyboard navigation, improving colour contrast, and testing browser compatibility.

---

# 🎯 Objectives

The main objectives of this hands-on are:

- Perform accessibility audit using Lighthouse
- Identify and fix WCAG 2.1 violations
- Improve semantic HTML structure
- Add ARIA attributes for assistive technologies
- Implement complete keyboard navigation
- Validate colour contrast ratios
- Perform cross-browser testing
- Use feature detection and polyfills for compatibility

---

# 🛠️ Tools Used

| Tool | Usage |
|---|---|
| Google Chrome Lighthouse | Accessibility audit |
| axe DevTools Extension | Detailed accessibility testing |
| Chrome DevTools | Debugging and colour testing |
| WebAIM Contrast Checker | Colour contrast validation |
| Can I Use | Browser compatibility checking |
| Firefox | Cross-browser testing |
| Microsoft Edge | Cross-browser testing |

---

# 📂 Project Structure

```
Student-Portal/
│
├── index.html
├── style.css
├── script.js
│
└── README.md
```

---

# TASK 1: Accessibility Audit & Semantic Fixes

## 1. Lighthouse Accessibility Audit

### Initial Audit

The Student Portal application was tested using:

```
Chrome DevTools
      ↓
Lighthouse
      ↓
Accessibility Audit
```

### Initial Accessibility Score

```
Accessibility Score: 100 / 100
```

---

## 2. Accessibility Issues Checked

The following accessibility areas were audited:

- Missing image alternative text
- Missing form labels
- Incorrect heading hierarchy
- Non-semantic interactive elements
- Screen reader compatibility

---

# Accessibility Fixes Implemented

## 1. Adding Alternative Text for Images

### Problem:

Images without `alt` attributes cannot be understood by screen readers.

### Solution:

Added descriptive alternative text.

Example:

```html
<img 
src="student.png" 
alt="Student profile image">
```

For decorative images:

```html
<img 
src="design.png" 
alt="">
```

---

# 2. Form Label Improvements

### Problem:

Input fields without labels create accessibility issues.

### Solution:

Associated every input field with a label.

Example:

```html
<label for="search">
Search Courses
</label>

<input 
id="search"
type="text">
```

Benefits:

- Screen readers can identify fields
- Improves usability
- Follows WCAG guidelines

---

# 3. Heading Hierarchy Correction

### Problem:

Skipped heading levels make navigation difficult for screen reader users.

### Updated Structure:

```
h1
 |
 ├── h2
      |
      └── h3
```

Example:

```html
<h1>Student Portal</h1>

<h2>Courses</h2>

<h3>Java Full Stack</h3>
```

---

# 4. Semantic HTML Improvements

### Problem:

Using `<div>` and `<span>` for interactive elements reduces accessibility.

### Solution:

Replaced with semantic elements.

Before:

```html
<div>
Login
</div>
```

After:

```html
<button>
Login
</button>
```

Used semantic elements:

- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<button>`
- `<footer>`

---

# TASK 2: ARIA & Keyboard Navigation

## 1. Navigation ARIA Attributes

Added navigation label:

```html
<nav aria-label="Main navigation">
```

Added active page indication:

```html
<a 
href="index.html"
aria-current="page">
Home
</a>
```

Purpose:

- Helps screen readers understand navigation
- Identifies current page

---

# 2. Keyboard Accessible Course Cards

## Implementation

Course cards were made keyboard accessible.

Added:

```html
tabindex="0"
```

Example:

```html
<div 
class="course-card"
tabindex="0">

Java Full Stack

</div>
```

---

## Keyboard Event Handling

Added JavaScript:

```javascript
courseCard.addEventListener(
"keydown",
function(event){

if(event.key==="Enter"){
    courseCard.click();
}

});
```

Now users can:

```
Press TAB → Focus Card

Press ENTER → Open Card
```

---

# 3. Search Result Live Announcement

Added ARIA live region:

```html
<div
role="status"
aria-live="polite">

5 courses found

</div>
```

Purpose:

- Announces dynamic content changes
- Helps screen reader users

---

# 4. Expandable Menu Accessibility

Added:

```html
aria-expanded="false"
```

Example:

Closed state:

```html
<button aria-expanded="false">
Menu
</button>
```

Opened state:

```html
<button aria-expanded="true">
Menu
</button>
```

The value changes dynamically using JavaScript.

---

# 5. Keyboard Navigation Testing

Verified using keyboard:

```
TAB
↓
SHIFT + TAB
↓
ENTER
```

Checked:

✅ All buttons accessible  
✅ Navigation links reachable  
✅ Course cards focusable  
✅ No keyboard traps  
✅ Visible focus indicator available  

---

# TASK 3: Colour Contrast & Cross-Browser Testing

# 1. Colour Contrast Testing

Tool Used:

```
WebAIM Contrast Checker
```

WCAG AA Requirement:

```
Normal Text:
Minimum Ratio = 4.5:1

Large Text:
Minimum Ratio = 3:1
```

---

# 2. Contrast Improvement

## Before Fix

```
Text Colour:
#777777

Background:
#FFFFFF

Contrast Ratio:
4.48:1

Status:
Failed
```

---

## After Fix

```
Text Colour:
#333333

Background:
#FFFFFF

Contrast Ratio:
12.63:1

Status:
Passed
```

---

# 3. Cross-Browser Testing

Application tested on:

| Browser | Result |
|---|---|
| Google Chrome | Passed |
| Firefox | Passed |
| Microsoft Edge | Passed |

---

## Tested Features

- Page layout
- CSS Flexbox
- CSS Grid
- Font rendering
- Buttons and forms
- JavaScript functionality

---

# 4. Browser Feature Compatibility

## Feature Tested

```
CSS Flexbox gap property
```

Tool:

```
https://caniuse.com/
```

Findings:

| Browser | Support |
|---|---|
| Chrome | Supported |
| Firefox | Supported |
| Edge | Supported |
| Older Browsers | Limited Support |

---

# 5. Feature Detection

Used CSS feature detection instead of browser detection.

Example:

```css
@supports (display:flex){

.container{

display:flex;

}

}
```

Benefits:

- Reliable across browsers
- Checks actual feature availability

---

# 6. Polyfill Implementation

Added CSS variables polyfill:

```html
<script src=
"https://cdn.jsdelivr.net/npm/css-vars-ponyfill@2">
</script>
```

Purpose:

- Provides support for CSS variables in older browsers
- Improves compatibility

---

# 📊 Final Accessibility Checklist

| Requirement | Status |
|---|---|
| Lighthouse Audit Completed | ✅ |
| Images have alt attributes | ✅ |
| Form labels added | ✅ |
| Heading hierarchy corrected | ✅ |
| Semantic HTML implemented | ✅ |
| ARIA labels added | ✅ |
| Keyboard navigation supported | ✅ |
| Course cards accessible | ✅ |
| aria-live implemented | ✅ |
| Colour contrast improved | ✅ |
| Browser testing completed | ✅ |
| Feature detection added | ✅ |
| Polyfill included | ✅ |

---

# 🎓 Learning Outcomes

After completing this hands-on, the following concepts were learned:

- WCAG 2.1 accessibility principles
- Importance of semantic HTML
- Role of ARIA attributes
- Screen reader support
- Keyboard-only navigation
- Accessibility testing tools
- Colour contrast standards
- Browser compatibility testing
- Feature detection and polyfills

---

# ✅ Conclusion

The Student Portal application was successfully improved according to accessibility and cross-browser compatibility standards.

The final implementation provides:

- Better experience for users with disabilities
- Improved screen reader support
- Complete keyboard accessibility
- Better visual readability
- Consistent behaviour across browsers

The application now follows professional frontend development accessibility practices.