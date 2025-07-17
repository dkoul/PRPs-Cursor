name: "Green Flag Quiz App PRP - Comedy Quiz with Instagram Integration"
description: |
  A comprehensive PRP for building a hilarious React-based quiz app that determines if someone is a "green flag" or "red flag" in friendship, with Instagram story sharing capabilities.

## Goal

Build a lightweight, hilarious React web application called "Green Flag Quiz" that:
- Presents 6 funny multiple-choice questions about friendship behavior
- Calculates a score-based result (green flag vs red flag) 
- Displays results with color-coded shading from red-green spectrum
- Provides hilarious advice based on the result
- Enables Instagram login and story sharing with user tagging
- Focuses on comedy and shareability for viral potential

## Why

- **Viral Content Potential**: Comedy quizzes perform exceptionally well on social media
- **Social Engagement**: Instagram story sharing with tagging creates organic reach
- **User Retention**: Hilarious content encourages repeat visits and friend sharing
- **Brand Building**: Memorable, shareable content builds audience and recognition
- **Low Barrier Entry**: Simple 6-question format ensures high completion rates

## What

### User-Visible Behavior
- **Homepage**: Eye-catching title, brief description, "Start Quiz" button
- **Quiz Flow**: 6 hilarious multiple-choice questions with smooth transitions
- **Results Page**: 
  - Score-based green flag/red flag determination
  - Color-coded result display (spectrum from red to green)
  - Hilarious personalized advice based on score
  - Instagram story sharing with friend tagging capability
  - "Take Again" and "Share" buttons

### Technical Requirements
- Responsive React SPA optimized for mobile
- Instagram Basic Display API integration
- Score calculation with color spectrum mapping
- Smooth animations and transitions
- Share functionality with custom Instagram story formats

### Success Criteria
- [ ] 6 hilarious quiz questions that users want to share
- [ ] Accurate scoring system with color-coded results
- [ ] Functional Instagram login and story sharing
- [ ] Mobile-optimized responsive design
- [ ] Fast loading and smooth user experience
- [ ] Viral-worthy comedic content that encourages sharing

## All Needed Context

### Documentation & References

```yaml
# React Quiz Implementation Patterns
- url: https://www.codevertiser.com/quiz-app-using-reactjs/
  why: Complete React quiz implementation with state management patterns
  critical: Use useState for currentQuestion, score, selectedAnswer, and results

- url: https://dev.to/oyegoke/state-control-in-react-behind-the-scenes-of-our-quiz-app-4acd
  why: Advanced state management patterns for quiz apps
  critical: Implement proper answer selection and validation patterns

- url: https://www.geeksforgeeks.org/create-a-quiz-app-using-react-hooks-and-timer-based-state-management/
  why: Modern React hooks patterns for quiz applications
  critical: Use useEffect for animations and state transitions

# Instagram API Integration
- url: https://medium.com/the-balancing-act/how-to-add-instagram-photos-to-your-nextjs-site-using-the-official-api-74eb4ca034a0
  why: Instagram Basic Display API authentication and integration
  critical: Requires Facebook Developer Account and app configuration

- url: https://developers.facebook.com/docs/instagram-basic-display-api
  why: Official Instagram API documentation for auth and story sharing
  critical: Use access tokens for API calls, implement proper error handling

# Color Spectrum Generation
- url: https://gist.github.com/mlocati/7210513
  why: JavaScript function for red-to-green color spectrum based on percentage
  critical: perc2color() function for mapping scores to colors

- url: https://javascript.plainenglish.io/creating-color-gradients-for-heat-maps-with-vanilla-javascript-c8d62bdd648e
  why: Advanced color gradient calculations for score visualization
  critical: RGB component calculations for smooth color transitions

# Comedy Quiz Content Patterns
- url: https://www.buzzfeed.com/suditiisocool/red-flag-or-green-flag-quiz
  why: Successful comedy quiz format and question patterns
  critical: Use relatable scenarios with humorous multiple choice options

- url: https://www.buzzfeed.com/ellierosetearle/are-you-a-red-flag-or-a-green-flag-quiz
  why: Viral quiz structure and result delivery patterns
  critical: Results should be shareable and encourage tagging friends
```

### Current Codebase Structure

```bash
green-flag-quiz/
├── public/
│   ├── index.html
│   └── manifest.json
├── src/
│   ├── components/
│   │   ├── Quiz.js          # Main quiz component
│   │   ├── Question.js      # Individual question display
│   │   ├── Results.js       # Results with color coding
│   │   └── InstagramAuth.js # Instagram login/sharing
│   ├── data/
│   │   └── questions.js     # Quiz questions data
│   ├── utils/
│   │   ├── colorUtils.js    # Color spectrum calculations
│   │   ├── scoreUtils.js    # Score calculation logic
│   │   └── instagramUtils.js# Instagram API helpers
│   ├── styles/
│   │   └── App.css         # Responsive styling
│   ├── App.js              # Main app component
│   └── index.js            # Entry point
├── package.json
└── README.md
```

### Desired Codebase Structure with Files to be Added

```bash
green-flag-quiz/
├── public/
│   ├── index.html          # Updated with meta tags for sharing
│   ├── manifest.json       # PWA configuration
│   └── og-images/          # Open Graph images for sharing
├── src/
│   ├── components/
│   │   ├── HomePage.js     # Landing page component
│   │   ├── Quiz.js         # Main quiz logic and state
│   │   ├── Question.js     # Question display with animations
│   │   ├── Results.js      # Results page with color coding
│   │   ├── InstagramAuth.js# Instagram login component
│   │   └── ShareStory.js   # Instagram story sharing
│   ├── data/
│   │   ├── questions.js    # 6 hilarious quiz questions
│   │   └── responses.js    # Score-based advice responses
│   ├── utils/
│   │   ├── colorSpectrum.js# Red-to-green color calculations
│   │   ├── scoreCalculator.js# Score-based result logic
│   │   └── instagramAPI.js # Instagram API integration
│   ├── hooks/
│   │   ├── useQuiz.js      # Custom hook for quiz state
│   │   └── useInstagram.js # Custom hook for Instagram API
│   ├── styles/
│   │   ├── global.css      # Global styles and animations
│   │   ├── Quiz.module.css # Quiz component styles
│   │   └── Results.module.css# Results page styles
│   ├── App.js              # Main app router
│   └── index.js            # Entry point
├── .env                    # Instagram API credentials
├── package.json            # Dependencies
└── README.md               # Setup instructions
```

### Known Gotchas & Library Quirks

```javascript
// CRITICAL: Instagram API requires HTTPS for authentication
// Use ngrok or deploy to test Instagram integration locally

// CRITICAL: Instagram Story sharing requires specific image dimensions
// Stories must be 1080x1920 pixels for proper display

// CRITICAL: React useState updates are asynchronous
// Use useEffect to handle state changes, not immediate access

// CRITICAL: Color spectrum calculation edge cases
// Handle division by zero when min/max scores are identical

// CRITICAL: Instagram API rate limiting
// Implement exponential backoff for failed requests

// CRITICAL: Mobile Safari quirks with CSS animations
// Use transform3d for hardware acceleration on mobile

// CRITICAL: Instagram API access token expires
// Implement refresh token flow for long-term access
```

## Implementation Blueprint

### Data Models and Structure

```javascript
// Quiz Question Structure
const questionStructure = {
  id: 1,
  question: "Your friend texts you at 3 AM with 'EMERGENCY' and it's about...",
  options: [
    { text: "A genuine crisis that needs immediate help", points: 5 },
    { text: "Drama about their crush not texting back", points: 2 },
    { text: "They're drunk and want to order pizza together", points: 3 },
    { text: "They found a spider and need emotional support", points: 4 }
  ],
  category: "crisis_response"
};

// Score Result Structure
const resultStructure = {
  score: 28,
  percentage: 93,
  flag: "green",
  color: "#22C55E",
  title: "You're a Green Flag Legend! 🌟",
  advice: "You're the friend everyone needs...",
  shareText: "I'm officially a Green Flag friend! 🌟"
};

// Instagram API Response Structure
const instagramAuthResponse = {
  access_token: "IGQVJXa...",
  user_id: "12345678",
  permissions: ["user_profile", "user_media"]
};
```

### List of Tasks to Complete

```yaml
Task 1: Project Setup and Dependencies
MODIFY package.json:
  - ADD react, react-dom, react-router-dom
  - ADD axios for API calls
  - ADD styled-components for styling
  - ADD framer-motion for animations

CREATE .env file:
  - ADD Instagram App ID and Secret
  - ADD Instagram redirect URI
  - ADD API base URLs

Task 2: Quiz Data and Logic
CREATE src/data/questions.js:
  - DEFINE 6 hilarious friendship scenarios
  - STRUCTURE multiple choice with point values
  - ENSURE comedy focus with relatable situations

CREATE src/utils/scoreCalculator.js:
  - IMPLEMENT point-based scoring system
  - CALCULATE percentage from total possible points
  - DETERMINE green/red flag threshold logic

Task 3: Color Spectrum System
CREATE src/utils/colorSpectrum.js:
  - IMPLEMENT red-to-green color calculation
  - MIRROR pattern from: perc2color() function
  - HANDLE edge cases for score boundaries

Task 4: React Components
CREATE src/components/HomePage.js:
  - DESIGN eye-catching landing page
  - ADD start quiz button with animation
  - IMPLEMENT responsive mobile design

CREATE src/components/Quiz.js:
  - MANAGE quiz state with useState hooks
  - HANDLE answer selection and progression
  - IMPLEMENT smooth transitions between questions

CREATE src/components/Question.js:
  - DISPLAY question with animated options
  - HANDLE answer selection highlighting
  - IMPLEMENT next button with validation

CREATE src/components/Results.js:
  - CALCULATE and display color-coded results
  - SHOW hilarious advice based on score
  - IMPLEMENT share functionality

Task 5: Instagram Integration
CREATE src/components/InstagramAuth.js:
  - IMPLEMENT Instagram OAuth flow
  - HANDLE access token management
  - PROVIDE user authentication UI

CREATE src/components/ShareStory.js:
  - GENERATE story-formatted result image
  - IMPLEMENT Instagram Story API calls
  - HANDLE friend tagging functionality

CREATE src/utils/instagramAPI.js:
  - IMPLEMENT Instagram API wrapper
  - HANDLE authentication and errors
  - PROVIDE story sharing methods

Task 6: Styling and Animations
CREATE src/styles/global.css:
  - IMPLEMENT responsive mobile-first design
  - ADD smooth animations for transitions
  - ENSURE accessibility compliance

CREATE component-specific CSS modules:
  - STYLE quiz flow with engaging visuals
  - IMPLEMENT color-coded result display
  - ADD Instagram-style UI elements

Task 7: Error Handling and Validation
IMPLEMENT comprehensive error handling:
  - HANDLE Instagram API failures gracefully
  - VALIDATE user inputs and selections
  - PROVIDE fallback sharing options

Task 8: Performance Optimization
OPTIMIZE for mobile performance:
  - IMPLEMENT lazy loading for components
  - MINIMIZE bundle size with code splitting
  - OPTIMIZE images and animations
```

### Integration Points

```yaml
INSTAGRAM_API:
  - endpoint: "https://api.instagram.com/oauth/authorize"
  - scope: "user_profile,user_media"
  - redirect_uri: "YOUR_DOMAIN/auth/instagram/callback"

STORY_SHARING:
  - endpoint: "https://graph.instagram.com/v12.0/{user-id}/media"
  - image_url: "REQUIRED - Story background image"
  - media_type: "STORIES"

COLOR_CALCULATION:
  - input: "Score percentage (0-100)"
  - output: "Hex color code from red (#FF0000) to green (#00FF00)"
  - formula: "perc2color(percentage) function"

SCORING_SYSTEM:
  - total_possible: 30 points (6 questions × 5 max points)
  - green_threshold: 70% (21+ points)
  - red_threshold: 40% (12- points)
  - yellow_zone: 41-69% (13-20 points)
```

## Validation Loop

### Level 1: Syntax & Style

```bash
# Install dependencies and setup
npm install react react-dom react-router-dom axios styled-components framer-motion
npm install --save-dev @testing-library/react @testing-library/jest-dom

# Check for syntax errors
npm run build
# Expected: Successful build with no errors

# Lint and format code
npx eslint src/ --fix
npx prettier src/ --write
# Expected: Clean, formatted code with no linting errors
```

### Level 2: Unit Tests

```javascript
// CREATE src/utils/__tests__/scoreCalculator.test.js
import { calculateScore, determineFlag } from '../scoreCalculator';

describe('Score Calculator', () => {
  test('calculates correct score from answers', () => {
    const answers = [3, 4, 5, 2, 4, 5]; // Sample answers
    const result = calculateScore(answers);
    expect(result.totalScore).toBe(23);
    expect(result.percentage).toBe(77);
  });

  test('determines green flag for high scores', () => {
    const result = determineFlag(25, 30);
    expect(result.flag).toBe('green');
    expect(result.color).toMatch(/^#[0-9A-F]{6}$/i);
  });

  test('determines red flag for low scores', () => {
    const result = determineFlag(10, 30);
    expect(result.flag).toBe('red');
  });
});

// CREATE src/utils/__tests__/colorSpectrum.test.js
import { perc2color, getColorForScore } from '../colorSpectrum';

describe('Color Spectrum', () => {
  test('returns red for 0% score', () => {
    expect(perc2color(0)).toBe('#FF0000');
  });

  test('returns green for 100% score', () => {
    expect(perc2color(100)).toBe('#00FF00');
  });

  test('returns yellow for 50% score', () => {
    const color = perc2color(50);
    expect(color).toBe('#FFFF00');
  });
});
```

```bash
# Run unit tests
npm test
# Expected: All tests pass with good coverage

# Test component rendering
npm test -- --coverage
# Expected: >80% test coverage for utility functions
```

### Level 3: Integration Testing

```bash
# Start development server
npm start
# Expected: App loads at http://localhost:3000

# Test quiz flow manually
# 1. Navigate to homepage
# 2. Click "Start Quiz"
# 3. Answer all 6 questions
# 4. Verify results page displays with correct color
# 5. Test Instagram auth flow (requires HTTPS)

# Test Instagram integration (requires deployed app)
# 1. Deploy app to Netlify/Vercel with HTTPS
# 2. Configure Instagram app with redirect URI
# 3. Test Instagram login flow
# 4. Test story sharing functionality
```

### Level 4: User Experience Testing

```bash
# Test mobile responsiveness
# Use Chrome DevTools to test various screen sizes
# Expected: App works smoothly on mobile devices

# Test sharing functionality
# 1. Complete quiz and get results
# 2. Test Instagram story sharing
# 3. Verify friend tagging works
# 4. Test fallback sharing options

# Performance testing
npm run build
npx serve -s build
# Test loading speeds and user experience
```

## Final Validation Checklist

- [ ] All 6 quiz questions are hilarious and relatable
- [ ] Score calculation works correctly with color coding
- [ ] Instagram authentication flow completes successfully
- [ ] Instagram story sharing works with friend tagging
- [ ] Mobile responsive design works on all devices
- [ ] Color spectrum accurately represents score ranges
- [ ] Error handling provides good user experience
- [ ] App loads quickly and animations are smooth
- [ ] Results are shareable and encourage viral spread
- [ ] All tests pass with good coverage

## Anti-Patterns to Avoid

- ❌ Don't create boring, generic quiz questions - comedy is key
- ❌ Don't ignore Instagram API rate limits - implement proper handling
- ❌ Don't skip mobile optimization - most users will be on mobile
- ❌ Don't hardcode Instagram credentials - use environment variables
- ❌ Don't forget HTTPS requirement for Instagram integration
- ❌ Don't overcomplicate scoring - keep it simple and fun
- ❌ Don't ignore accessibility - ensure keyboard navigation works
- ❌ Don't skip error states - handle API failures gracefully

## Confidence Score: 9/10

**High confidence due to:**
- Comprehensive research on React quiz patterns
- Clear Instagram API integration path
- Proven color spectrum calculation methods
- Strong comedy quiz content examples
- Well-defined scoring and result system
- Mobile-first responsive design approach

**Risk mitigation:**
- Instagram API complexity handled with thorough documentation
- Color calculations tested with proven algorithms
- React patterns validated with multiple tutorial sources
- Error handling planned for all integration points 