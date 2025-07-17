name: "Tic Tac Toe JavaScript Web App"
description: |
  Create a modern, responsive tic tac toe web application using vanilla JavaScript, HTML5, and CSS3 with clean architecture, AI opponent, and mobile-friendly design.

## Purpose

Build a production-ready tic tac toe game that demonstrates modern JavaScript game development patterns, clean code architecture, and responsive design principles suitable for both desktop and mobile devices.

## Core Principles

1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance

---

## Goal

Create a complete tic tac toe web application featuring:
- Modern JavaScript ES6+ syntax with clean architecture
- Responsive design that works on desktop and mobile
- AI opponent with multiple difficulty levels
- Smooth animations and visual feedback
- Score tracking and game state management
- Touch-friendly interface for mobile devices

## Why

- **Business value**: Demonstrates modern web development skills and game development patterns
- **User experience**: Provides an engaging, accessible game that works across all devices
- **Technical showcase**: Shows proficiency in vanilla JavaScript, CSS3, and responsive design
- **Learning opportunity**: Illustrates proper separation of concerns and modular design patterns

## What

### User-visible behavior:
- Clean, modern game board with hover effects and animations
- Click/touch to place X or O symbols
- AI opponent that provides challenging gameplay
- Score tracking across multiple games
- Responsive design that adapts to screen size
- Visual feedback for wins, losses, and draws
- Reset functionality for new games

### Technical requirements:
- Vanilla JavaScript (ES6+) with no dependencies
- HTML5 semantic structure
- CSS3 with modern features (flexbox, grid, transitions)
- Mobile-responsive design with touch support
- Modular architecture with separation of concerns
- Clean, maintainable code structure

### Success Criteria

- [ ] Game board renders correctly on all screen sizes
- [ ] Players can make moves by clicking/touching cells
- [ ] AI opponent provides challenging gameplay
- [ ] Win/loss/draw detection works correctly
- [ ] Score tracking persists across games
- [ ] Mobile touch interface works smoothly
- [ ] All animations and transitions are smooth
- [ ] Code follows modern JavaScript best practices

## All Needed Context

### Documentation & References

```yaml
# MUST READ - Include these in your context window
- url: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial
  why: HTML5 Canvas fundamentals and best practices for game development

- url: https://developer.mozilla.org/en-US/docs/Web/API/Touch_events
  why: Touch event handling for mobile devices, essential for mobile gameplay

- url: https://web.dev/responsive-web-design-basics/
  why: Responsive design principles for cross-device compatibility

- url: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
  why: Modern JavaScript module patterns for clean architecture

- doc: https://css-tricks.com/snippets/css/a-guide-to-flexbox/
  section: Complete flexbox guide for layout
  critical: Essential for responsive game board layout

- doc: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout
  section: CSS Grid for game board structure
  critical: Grid system for perfect 3x3 game board

- url: https://javascript.info/object-oriented-programming
  why: Object-oriented patterns for game entity management

- url: https://www.smashingmagazine.com/2015/09/principles-of-html5-game-design/
  why: Game design principles and architecture patterns
```

### Current Codebase tree

```bash
PRPs-Cursor/
├── cursor_workflows/
├── PRPs/
│   ├── templates/
│   ├── scripts/
│   ├── completed/
│   └── tic-tac-toe-javascript-app.md (this file)
├── README.md
└── pyproject.toml
```

### Desired Codebase tree with files to be added

```bash
PRPs-Cursor/
├── tic-tac-toe-app/
│   ├── index.html              # Main HTML structure
│   ├── css/
│   │   └── styles.css          # All CSS styles and responsive design
│   ├── js/
│   │   ├── game.js             # Main game controller
│   │   ├── board.js            # Game board logic
│   │   ├── player.js           # Player and AI logic
│   │   ├── ui.js               # User interface management
│   │   └── utils.js            # Utility functions
│   └── README.md               # Project documentation
└── [existing files...]
```

### Known Gotchas of our codebase & Library Quirks

```javascript
// CRITICAL: Touch events require preventDefault() to avoid scrolling
// Example: Always call e.preventDefault() in touch handlers

// CRITICAL: CSS Grid requires explicit grid-template-areas for accessibility
// Example: Use named grid areas for screen readers

// CRITICAL: Modern JavaScript requires modules or proper script loading
// Example: Use ES6 modules or ensure proper script order

// CRITICAL: Mobile browsers have 300ms click delay
// Example: Use touchstart/touchend instead of click for mobile

// CRITICAL: CSS transforms can cause layout issues
// Example: Use transform3d() for hardware acceleration

// CRITICAL: Event delegation needed for dynamically generated content
// Example: Attach event listeners to parent container, not individual cells
```

## Implementation Blueprint

### Data models and structure

Create clean, maintainable data structures with proper encapsulation:

```javascript
// Game state management
class GameState {
  constructor() {
    this.board = Array(9).fill(null);
    this.currentPlayer = 'X';
    this.gameActive = true;
    this.score = { X: 0, O: 0, ties: 0 };
  }
}

// Player management
class Player {
  constructor(symbol, isHuman = true) {
    this.symbol = symbol;
    this.isHuman = isHuman;
  }
}

// AI opponent with difficulty levels
class AIPlayer extends Player {
  constructor(symbol, difficulty = 'medium') {
    super(symbol, false);
    this.difficulty = difficulty;
  }
}
```

### List of tasks to be completed to fulfill the PRP in order

```yaml
Task 1: Create HTML structure and basic CSS
CREATE index.html:
  - FOLLOW semantic HTML5 structure
  - INCLUDE meta viewport tag for mobile
  - MIRROR responsive design patterns
  - PRESERVE accessibility requirements

CREATE css/styles.css:
  - IMPLEMENT CSS Grid for game board
  - FOLLOW mobile-first responsive design
  - INCLUDE smooth transitions and animations
  - PRESERVE touch-friendly sizing (44px minimum)

Task 2: Implement core game logic
CREATE js/game.js:
  - PATTERN: Main game controller with state management
  - IMPLEMENT game loop and event handling
  - FOLLOW modular architecture principles
  - PRESERVE separation of concerns

CREATE js/board.js:
  - PATTERN: Game board representation and manipulation
  - IMPLEMENT win condition checking
  - FOLLOW immutable state patterns where possible
  - PRESERVE data integrity

Task 3: Add player and AI systems
CREATE js/player.js:
  - PATTERN: Player abstraction with AI inheritance
  - IMPLEMENT minimax algorithm for AI
  - FOLLOW strategy pattern for different difficulties
  - PRESERVE extensibility for future AI types

Task 4: Implement user interface
CREATE js/ui.js:
  - PATTERN: UI state management separate from game logic
  - IMPLEMENT touch and mouse event handling
  - FOLLOW responsive interaction patterns
  - PRESERVE accessibility features

Task 5: Add utilities and mobile support
CREATE js/utils.js:
  - PATTERN: Utility functions for common operations
  - IMPLEMENT mobile detection and touch handling
  - FOLLOW helper function patterns
  - PRESERVE code reusability

Task 6: Final integration and optimization
INTEGRATE all modules:
  - FOLLOW proper module loading patterns
  - IMPLEMENT error handling and validation
  - PRESERVE performance optimizations
  - COMPLETE responsive testing
```

### Per task pseudocode with CRITICAL details

```javascript
// Task 1: HTML Structure
// CRITICAL: Use semantic HTML5 elements for accessibility
// CRITICAL: Include proper meta tags for mobile optimization
// CRITICAL: Structure for CSS Grid implementation

// Task 2: Game Logic
// PATTERN: Modular architecture with clear separation
class Game {
  constructor() {
    this.state = new GameState();
    this.players = [new Player('X'), new AIPlayer('O')];
    // CRITICAL: Initialize event listeners properly
    this.initializeEventListeners();
  }

  makeMove(cellIndex) {
    // PATTERN: Input validation before state changes
    if (!this.isValidMove(cellIndex)) return false;
    
    // CRITICAL: Update state immutably where possible
    this.state.board[cellIndex] = this.state.currentPlayer;
    
    // PATTERN: Check win conditions after each move
    const winner = this.checkWinner();
    if (winner) {
      this.endGame(winner);
      return;
    }
    
    this.switchPlayer();
  }

  // CRITICAL: Efficient win detection algorithm
  checkWinner() {
    const winPatterns = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
      [0, 4, 8], [2, 4, 6] // diagonals
    ];
    
    for (const pattern of winPatterns) {
      const [a, b, c] = pattern;
      if (this.state.board[a] && 
          this.state.board[a] === this.state.board[b] && 
          this.state.board[a] === this.state.board[c]) {
        return this.state.board[a];
      }
    }
    return null;
  }
}

// Task 3: AI Implementation
// CRITICAL: Minimax algorithm with alpha-beta pruning for performance
class AIPlayer {
  getBestMove(board, isMaximizing, depth = 0) {
    // PATTERN: Minimax with optimizations
    const winner = this.evaluateBoard(board);
    
    if (winner === this.symbol) return 10 - depth;
    if (winner === this.opponentSymbol) return -10 + depth;
    if (this.isBoardFull(board)) return 0;
    
    // CRITICAL: Limit search depth for performance
    if (depth > 6) return 0;
    
    let bestScore = isMaximizing ? -Infinity : Infinity;
    
    for (let i = 0; i < 9; i++) {
      if (board[i] === null) {
        board[i] = isMaximizing ? this.symbol : this.opponentSymbol;
        const score = this.getBestMove(board, !isMaximizing, depth + 1);
        board[i] = null;
        
        bestScore = isMaximizing ? 
          Math.max(score, bestScore) : 
          Math.min(score, bestScore);
      }
    }
    
    return bestScore;
  }
}

// Task 4: UI Implementation
// CRITICAL: Handle both mouse and touch events
class UI {
  initializeEventListeners() {
    // PATTERN: Event delegation for efficiency
    this.gameBoard.addEventListener('click', this.handleCellClick.bind(this));
    
    // CRITICAL: Touch support for mobile
    this.gameBoard.addEventListener('touchstart', this.handleTouchStart.bind(this));
    this.gameBoard.addEventListener('touchend', this.handleTouchEnd.bind(this));
  }

  handleTouchStart(e) {
    // CRITICAL: Prevent default to avoid scrolling
    e.preventDefault();
    this.touchStartTarget = e.target;
  }

  handleTouchEnd(e) {
    e.preventDefault();
    // PATTERN: Only trigger if touch started and ended on same element
    if (e.target === this.touchStartTarget) {
      this.handleCellClick(e);
    }
  }

  updateCell(cellIndex, symbol) {
    // PATTERN: Smooth animations for better UX
    const cell = this.cells[cellIndex];
    cell.textContent = symbol;
    cell.classList.add('animate-in');
    
    // CRITICAL: Clean up animation classes
    setTimeout(() => {
      cell.classList.remove('animate-in');
    }, 300);
  }
}
```

### Integration Points

```yaml
HTML:
  - structure: "Semantic HTML5 with proper accessibility attributes"
  - meta: "Viewport meta tag for mobile optimization"
  - grid: "CSS Grid container for game board"

CSS:
  - grid: "CSS Grid for perfect 3x3 layout"
  - responsive: "Mobile-first responsive design"
  - animations: "Smooth transitions and hover effects"
  - accessibility: "Focus states and high contrast support"

JavaScript:
  - modules: "ES6 modules or proper script loading order"
  - events: "Event delegation and touch support"
  - state: "Immutable state management where possible"
  - performance: "Efficient algorithms and DOM manipulation"

Mobile:
  - touch: "Touch event handling with preventDefault()"
  - sizing: "44px minimum touch targets"
  - performance: "Hardware acceleration with CSS transforms"
```

## Validation Loop

### Level 1: Syntax & Style

```bash
# HTML validation
# Expected: Valid HTML5 structure
npx html-validate index.html

# CSS validation  
# Expected: Valid CSS3, no errors
npx stylelint css/styles.css

# JavaScript validation
# Expected: ES6+ syntax, no errors
npx eslint js/*.js --fix
```

### Level 2: Unit Tests

```javascript
// Create test file: test/game.test.js
describe('Game Logic', () => {
  test('should detect horizontal wins', () => {
    const game = new Game();
    game.state.board = ['X', 'X', 'X', null, null, null, null, null, null];
    expect(game.checkWinner()).toBe('X');
  });

  test('should detect vertical wins', () => {
    const game = new Game();
    game.state.board = ['X', null, null, 'X', null, null, 'X', null, null];
    expect(game.checkWinner()).toBe('X');
  });

  test('should detect diagonal wins', () => {
    const game = new Game();
    game.state.board = ['X', null, null, null, 'X', null, null, null, 'X'];
    expect(game.checkWinner()).toBe('X');
  });

  test('should detect draws', () => {
    const game = new Game();
    game.state.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O'];
    expect(game.checkWinner()).toBe(null);
    expect(game.isDraw()).toBe(true);
  });
});

describe('AI Player', () => {
  test('should make optimal moves', () => {
    const ai = new AIPlayer('O', 'hard');
    const board = ['X', null, null, null, 'X', null, null, null, null];
    const move = ai.getBestMove(board);
    expect(move).toBe(8); // Block the diagonal win
  });
});
```

```bash
# Run tests
npx jest test/game.test.js
# Expected: All tests pass
```

### Level 3: Integration Test

```bash
# Start a local server
npx http-server . -p 8080

# Manual testing checklist:
# - Game loads without errors
# - Can click cells to make moves
# - AI responds appropriately
# - Win/loss detection works
# - Score updates correctly
# - Mobile touch works
# - Responsive design functions
```

### Level 4: Performance & Accessibility

```bash
# Performance testing
npx lighthouse http://localhost:8080 --output=json

# Accessibility testing
npx axe-cli http://localhost:8080

# Mobile testing
# Test on actual mobile devices or use browser dev tools
# Check touch targets are at least 44px
# Verify no horizontal scrolling
# Test orientation changes
```

## Final validation Checklist

- [ ] All tests pass: `npx jest test/`
- [ ] No linting errors: `npx eslint js/`
- [ ] No CSS errors: `npx stylelint css/`
- [ ] HTML validates: `npx html-validate index.html`
- [ ] Game functions correctly on desktop
- [ ] Game functions correctly on mobile
- [ ] AI provides challenging gameplay
- [ ] Responsive design works on all screen sizes
- [ ] Touch interactions work smoothly
- [ ] Accessibility features work properly
- [ ] Performance is acceptable (Lighthouse score > 90)

---

## Anti-Patterns to Avoid

- ❌ Don't use jQuery or other libraries - use vanilla JavaScript
- ❌ Don't mix game logic with UI code - maintain separation
- ❌ Don't ignore mobile users - implement proper touch handling
- ❌ Don't use table layouts for game board - use CSS Grid
- ❌ Don't forget accessibility - include proper ARIA labels
- ❌ Don't use global variables - use proper module patterns
- ❌ Don't ignore performance - optimize DOM manipulation
- ❌ Don't skip validation - test on real devices 