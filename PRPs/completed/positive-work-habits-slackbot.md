name: "Positive Work Habits Slackbot with Google Docs Integration"
description: |
  Create a custom Slackbot designed to promote positive work habits through automated reminders, 
  tips, and fun activities. The bot reads work habits from a Google Doc and provides personalized 
  reminders, tracking, and team engagement features. No database required - uses Google Docs as 
  the data source and local storage for state management.

## Purpose

Build a production-ready Slackbot that helps teams maintain positive work habits through automated 
reminders, progress tracking, and team engagement features, using Google Docs as the habit configuration 
source and Slack as the primary interface.

## Core Principles

1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance

---

## Goal

Build a comprehensive Slackbot that:
- Reads work habits from a Google Doc with structured format
- Sends personalized reminders based on configurable schedules
- Tracks habit completion and provides progress updates
- Engages teams with fun activities and challenges
- Provides slash commands for manual interactions
- Handles real-time conversations and responses
- Supports multiple teams and channels
- Includes comprehensive logging and error handling

## Why

- **Business value**: Improves team productivity and wellness through consistent habit reinforcement
- **User impact**: Reduces burnout, increases engagement, and builds positive team culture
- **Problems solved**: Manual habit tracking, forgotten wellness breaks, team disconnect
- **Integration**: Seamlessly fits into existing Slack workflows without disrupting productivity
- **Scalability**: Works for small teams to large organizations with minimal setup

## What

### User-visible behavior:
- **Automated Reminders**: Scheduled messages for habits like "Take a 5-minute break", "Hydrate", "Stretch"
- **Interactive Tracking**: Users can mark habits as complete with emoji reactions or commands
- **Progress Reports**: Daily/weekly summaries of habit completion rates
- **Team Challenges**: Group goals and friendly competition features
- **Slash Commands**: `/habits status`, `/habits add`, `/habits config` for manual interaction
- **Fun Activities**: Random wellness tips, motivational quotes, and team building prompts
- **Personalization**: Custom schedules per user/team based on Google Doc configuration

### Technical requirements:
- Python 3.9+ with Slack Bolt framework
- Google Docs API integration for habit configuration
- APScheduler for automated reminders and tasks
- Socket Mode for real-time Slack communication
- Environment-based configuration (12-factor app)
- Comprehensive logging and error handling
- Support for multiple deployment options (Heroku, AWS Lambda, Docker)

### Success Criteria

- [ ] Bot successfully reads habits from Google Doc with proper error handling
- [ ] Automated reminders sent on schedule without duplication
- [ ] Users can interact with bot via reactions, commands, and conversations
- [ ] Progress tracking works across multiple users and teams
- [ ] All slash commands respond within 3 seconds
- [ ] Bot handles Slack API rate limits gracefully
- [ ] Comprehensive logging for monitoring and debugging
- [ ] Zero-downtime deployment with health checks
- [ ] Documentation for team configuration and deployment

## All Needed Context

### Documentation & References

```yaml
# MUST READ - Include these in your context window
- url: https://tools.slack.dev/bolt-python/tutorial/getting-started
  why: Official Slack Bolt framework setup and basic patterns
  critical: Socket Mode configuration for internal apps

- url: https://tools.slack.dev/bolt-python/concepts/event-listening
  why: Event handling patterns for messages, reactions, and commands
  critical: Middleware patterns and context handling

- url: https://developers.google.com/docs/api/quickstart/python
  why: Google Docs API authentication and basic document reading
  critical: Service account setup and OAuth flow

- url: https://googleapis.github.io/google-api-python-client/docs/start.html
  why: Google API client library patterns and best practices
  critical: Authentication handling and error management

- url: https://betterstack.com/community/guides/scaling-python/apscheduler-scheduled-tasks/
  why: APScheduler comprehensive guide for task scheduling
  critical: Persistent job stores and error handling

- url: https://api.slack.com/apps/new
  why: Slack app creation and configuration
  critical: Socket Mode setup and bot token generation

- url: https://developers.google.com/workspace/guides/create-credentials
  why: Google Cloud service account creation
  critical: JSON credentials and scopes configuration
```

### Google Docs API Patterns

```python
# PATTERN: Service account authentication
from google.oauth2 import service_account
from googleapiclient.discovery import build

def authenticate_google_docs():
    """Authenticate with Google Docs API using service account"""
    # CRITICAL: Use service account for production, not OAuth flow
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(os.environ['GOOGLE_CREDENTIALS_JSON']),
        scopes=['https://www.googleapis.com/auth/documents.readonly']
    )
    return build('docs', 'v1', credentials=credentials)

# PATTERN: Extract text from Google Doc
def extract_habits_from_doc(service, document_id):
    """Extract structured habit data from Google Doc"""
    # GOTCHA: Document structure is hierarchical, need to traverse properly
    doc = service.documents().get(documentId=document_id).execute()
    return parse_document_content(doc.get('body').get('content'))
```

### Slack Bolt Patterns

```python
# PATTERN: Slack Bolt app setup with Socket Mode
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

# PATTERN: Event listeners
@app.event("app_mention")
def handle_mention(event, say):
    """Handle when bot is mentioned"""
    # CRITICAL: Always acknowledge events within 3 seconds
    say(f"Hello <@{event['user']}>!")

# PATTERN: Slash commands
@app.command("/habits")
def handle_habits_command(ack, respond, command):
    """Handle /habits slash command"""
    ack()  # CRITICAL: Must acknowledge immediately
    # Process command logic here
    respond("Habit command processed!")
```

### APScheduler Patterns

```python
# PATTERN: Persistent scheduler setup
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

scheduler = BackgroundScheduler(jobstores=jobstores)

# PATTERN: Schedule with error handling
def schedule_habit_reminder(user_id, habit_name, cron_expression):
    """Schedule habit reminder with proper error handling"""
    try:
        scheduler.add_job(
            send_habit_reminder,
            'cron',
            args=[user_id, habit_name],
            **parse_cron_expression(cron_expression),
            id=f"habit_{user_id}_{habit_name}",
            replace_existing=True
        )
    except Exception as e:
        logger.error(f"Failed to schedule habit reminder: {e}")
```

### Configuration Management

```python
# PATTERN: Environment-based configuration
import os
from typing import Dict, Any

class Config:
    """Application configuration from environment variables"""
    
    # CRITICAL: All secrets must be environment variables
    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
    GOOGLE_CREDENTIALS_JSON = os.environ.get("GOOGLE_CREDENTIALS_JSON")
    GOOGLE_DOC_ID = os.environ.get("GOOGLE_DOC_ID")
    
    # PATTERN: Provide defaults for non-sensitive config
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    SCHEDULER_TIMEZONE = os.environ.get("SCHEDULER_TIMEZONE", "UTC")
    
    @classmethod
    def validate(cls) -> bool:
        """Validate all required environment variables are set"""
        required = ["SLACK_BOT_TOKEN", "SLACK_APP_TOKEN", "GOOGLE_CREDENTIALS_JSON", "GOOGLE_DOC_ID"]
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing required environment variables: {missing}")
        return True
```

### Error Handling Patterns

```python
# PATTERN: Comprehensive error handling
import logging
from functools import wraps
from typing import Callable, Any

def handle_errors(func: Callable) -> Callable:
    """Decorator for comprehensive error handling"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            # CRITICAL: Always provide user-friendly error messages
            if hasattr(args[0], 'respond'):
                args[0].respond("Something went wrong. Please try again later.")
            raise
    return wrapper

# PATTERN: Slack API rate limiting
import time
from slack_sdk.errors import SlackApiError

def handle_rate_limit(func):
    """Handle Slack API rate limiting with exponential backoff"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except SlackApiError as e:
                if e.response["error"] == "rate_limited":
                    delay = int(e.response.headers.get("Retry-After", 1))
                    time.sleep(delay * (2 ** attempt))  # Exponential backoff
                    continue
                raise
        raise Exception("Max retries exceeded for rate limiting")
    return wrapper
```

### Google Docs Data Structure

```yaml
# EXAMPLE: Expected Google Doc structure for habits
# Document should contain structured sections like:

# DAILY HABITS
- Drink water reminder: 09:00, 13:00, 17:00
- Stand up break: every 2 hours during 09:00-17:00
- Take a walk: 12:00
- Deep breathing: 10:00, 15:00

# WEEKLY HABITS
- Team check-in: Monday 09:00
- Week planning: Monday 08:00
- Retrospective: Friday 16:00

# MONTHLY CHALLENGES
- Step counter challenge: 1st of month
- Healthy lunch week: 2nd Monday
- Meeting-free Friday: Last Friday

# MOTIVATIONAL QUOTES
- "Success is the sum of small efforts repeated day in and day out."
- "Take care of your body. It's the only place you have to live."

# TEAM ACTIVITIES
- Virtual coffee break: random between 14:00-16:00
- Show and tell: Friday 15:00
- Gratitude sharing: random 3 times per week
```

### Deployment Patterns

```python
# PATTERN: Health check endpoint
@app.route("/health")
def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Check Google Docs API
        service = authenticate_google_docs()
        service.documents().get(documentId=Config.GOOGLE_DOC_ID).execute()
        
        # Check Slack API
        app.client.api_test()
        
        # Check scheduler
        if not scheduler.running:
            raise Exception("Scheduler not running")
            
        return {"status": "healthy", "timestamp": time.time()}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {"status": "unhealthy", "error": str(e)}, 500

# PATTERN: Graceful shutdown
import signal
import sys

def signal_handler(sig, frame):
    """Handle graceful shutdown"""
    logger.info("Shutting down gracefully...")
    scheduler.shutdown()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
```

### Critical Gotchas

```python
# GOTCHA: Slack Socket Mode requires specific token types
# App-level token (xapp-) for Socket Mode connection
# Bot token (xoxb-) for API calls
# NEVER mix these up or connection will fail

# GOTCHA: Google Docs API document structure is hierarchical
# Must recursively traverse paragraph elements
# Tables and nested structures require special handling

# GOTCHA: APScheduler timezone handling
# Always specify timezone explicitly
# UTC for storage, local timezone for display

# GOTCHA: Slack API rate limits
# 1 request per second for Web API
# Must implement exponential backoff
# Use response headers for rate limit info

# GOTCHA: Environment variables in production
# Multi-line JSON credentials need proper escaping
# Use single quotes for multi-line env vars
# Never commit credentials to version control
```

## Implementation Blueprint

### Data models and structure

Create the core data models for habit management and user interactions.

```python
# Core data structures
from dataclasses import dataclass
from datetime import datetime, time
from typing import List, Dict, Optional, Any
from enum import Enum

class HabitType(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    CHALLENGE = "challenge"

@dataclass
class Habit:
    name: str
    type: HabitType
    schedule: str  # Cron expression or interval
    message: str
    channel: Optional[str] = None
    users: Optional[List[str]] = None
    active: bool = True

@dataclass
class HabitCompletion:
    user_id: str
    habit_name: str
    completed_at: datetime
    channel_id: str

@dataclass
class UserProgress:
    user_id: str
    habit_completions: List[HabitCompletion]
    streak_count: int
    last_activity: datetime

class HabitManager:
    """Manages habit lifecycle and user interactions"""
    
    def __init__(self, google_doc_service, slack_app):
        self.google_service = google_doc_service
        self.slack_app = slack_app
        self.habits: Dict[str, Habit] = {}
        self.user_progress: Dict[str, UserProgress] = {}
    
    def load_habits_from_doc(self, doc_id: str) -> None:
        """Load habits from Google Doc with error handling"""
        pass
    
    def schedule_habit_reminders(self) -> None:
        """Schedule all habit reminders using APScheduler"""
        pass
    
    def track_completion(self, user_id: str, habit_name: str) -> None:
        """Track habit completion and update progress"""
        pass
```

### List of tasks to be completed to fulfill the PRP in the order they should be completed

```yaml
Task 1:
CREATE project structure:
  - INITIALIZE Python project with pyproject.toml
  - INSTALL dependencies: slack-bolt, google-api-python-client, apscheduler
  - CREATE src/slackbot/ directory structure
  - SETUP logging configuration
  - CONFIGURE environment variable loading

Task 2:
CREATE src/slackbot/config.py:
  - IMPLEMENT Config class with environment variable loading
  - ADD validation for required environment variables
  - INCLUDE Google Docs API scopes and credentials handling
  - ADD Slack API token configuration
  - IMPLEMENT configuration validation

Task 3:
CREATE src/slackbot/google_docs.py:
  - IMPLEMENT GoogleDocsService class
  - ADD service account authentication
  - IMPLEMENT document reading with recursive text extraction
  - ADD habit parsing from structured document format
  - INCLUDE error handling for API failures and document structure

Task 4:
CREATE src/slackbot/habit_manager.py:
  - IMPLEMENT HabitManager class with habit lifecycle management
  - ADD habit loading from Google Docs
  - IMPLEMENT habit parsing and validation
  - ADD habit scheduling with APScheduler integration
  - INCLUDE user progress tracking and persistence

Task 5:
CREATE src/slackbot/slack_handlers.py:
  - IMPLEMENT Slack event handlers for mentions and messages
  - ADD slash command handlers (/habits status, /habits config)
  - IMPLEMENT reaction handlers for habit completion tracking
  - ADD interactive message handlers for habit management
  - INCLUDE error handling and user-friendly responses

Task 6:
CREATE src/slackbot/scheduler.py:
  - IMPLEMENT SchedulerService class with APScheduler
  - ADD persistent job store configuration
  - IMPLEMENT habit reminder scheduling
  - ADD job management (add, remove, update)
  - INCLUDE error handling and job persistence

Task 7:
CREATE src/slackbot/bot.py:
  - IMPLEMENT main SlackBot class orchestrating all components
  - ADD application initialization and configuration
  - IMPLEMENT health check endpoint
  - ADD graceful shutdown handling
  - INCLUDE comprehensive logging and monitoring

Task 8:
CREATE src/slackbot/utils.py:
  - IMPLEMENT utility functions for time handling
  - ADD message formatting helpers
  - IMPLEMENT user progress calculation
  - ADD error handling decorators
  - INCLUDE validation functions

Task 9:
CREATE main.py:
  - IMPLEMENT application entry point
  - ADD signal handling for graceful shutdown
  - IMPLEMENT health check server
  - ADD command line argument parsing
  - INCLUDE deployment configuration

Task 10:
CREATE deployment configuration:
  - ADD Dockerfile for containerization
  - CREATE docker-compose.yml for local development
  - ADD Heroku deployment configuration (Procfile, runtime.txt)
  - INCLUDE environment variable templates
  - ADD deployment documentation

Task 11:
CREATE comprehensive tests:
  - ADD unit tests for all components
  - IMPLEMENT integration tests with mocked APIs
  - ADD test fixtures for Google Doc parsing
  - INCLUDE Slack interaction testing
  - ADD performance and load testing

Task 12:
CREATE documentation:
  - ADD README with setup instructions
  - CREATE deployment guide
  - ADD user manual for habit configuration
  - INCLUDE troubleshooting guide
  - ADD API documentation and examples
```

### Per task pseudocode with critical details

```python
# Task 1: Project structure
# CRITICAL: Use pyproject.toml for modern Python dependency management
# PATTERN: Follow src/ layout for better imports and testing

# Task 2: Configuration management
def load_config():
    """Load and validate configuration from environment"""
    # CRITICAL: Validate all required environment variables on startup
    # PATTERN: Use dataclass for type safety and validation
    # GOTCHA: Multi-line JSON credentials need special handling
    
    config = Config()
    config.validate()
    return config

# Task 3: Google Docs integration
async def load_habits_from_doc(doc_id: str) -> List[Habit]:
    """Load habits from Google Doc with proper error handling"""
    # CRITICAL: Use service account authentication for production
    # PATTERN: Recursive document traversal for structured content
    # GOTCHA: Document structure can be nested and complex
    
    try:
        service = authenticate_google_docs()
        doc = service.documents().get(documentId=doc_id).execute()
        content = extract_structured_content(doc)
        return parse_habits_from_content(content)
    except Exception as e:
        logger.error(f"Failed to load habits from doc: {e}")
        raise

# Task 4: Habit management
def schedule_habit_reminder(habit: Habit):
    """Schedule habit reminder with APScheduler"""
    # CRITICAL: Use persistent job store for reliability
    # PATTERN: Include timezone handling for global teams
    # GOTCHA: Cron expressions must be validated before scheduling
    
    scheduler.add_job(
        send_habit_reminder,
        trigger=CronTrigger.from_crontab(habit.schedule),
        args=[habit],
        id=f"habit_{habit.name}",
        replace_existing=True,
        timezone=Config.SCHEDULER_TIMEZONE
    )

# Task 5: Slack integration
@app.command("/habits")
def handle_habits_command(ack, respond, command):
    """Handle /habits slash command"""
    # CRITICAL: Must acknowledge within 3 seconds
    # PATTERN: Use threaded responses for complex operations
    # GOTCHA: Slack has specific message formatting requirements
    
    ack()
    
    try:
        action = command['text'].split()[0] if command['text'] else 'status'
        
        if action == 'status':
            progress = get_user_progress(command['user_id'])
            respond(format_progress_message(progress))
        elif action == 'config':
            # Show configuration options
            respond(build_config_blocks())
        else:
            respond("Unknown command. Use: status, config")
            
    except Exception as e:
        logger.error(f"Command error: {e}")
        respond("Sorry, something went wrong. Please try again.")

# Task 6: Scheduler service
class SchedulerService:
    """Manages APScheduler for habit reminders"""
    
    def __init__(self):
        # CRITICAL: Use SQLAlchemy job store for persistence
        # PATTERN: Configure timezone and error handling
        
        self.scheduler = BackgroundScheduler(
            jobstores={
                'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
            },
            executors={
                'default': ThreadPoolExecutor(20)
            },
            timezone=Config.SCHEDULER_TIMEZONE
        )
    
    def start(self):
        """Start scheduler with error handling"""
        try:
            self.scheduler.start()
            logger.info("Scheduler started successfully")
        except Exception as e:
            logger.error(f"Failed to start scheduler: {e}")
            raise

# Task 7: Main bot orchestration
class SlackBot:
    """Main bot class orchestrating all components"""
    
    def __init__(self):
        # CRITICAL: Initialize all components in correct order
        # PATTERN: Dependency injection for testability
        
        self.config = Config()
        self.google_service = GoogleDocsService(self.config)
        self.scheduler = SchedulerService()
        self.habit_manager = HabitManager(self.google_service, self.scheduler)
        self.slack_app = App(token=self.config.SLACK_BOT_TOKEN)
        
    async def start(self):
        """Start bot with full initialization"""
        try:
            # Load habits from Google Doc
            await self.habit_manager.load_habits()
            
            # Schedule all habit reminders
            self.habit_manager.schedule_reminders()
            
            # Start scheduler
            self.scheduler.start()
            
            # Start Slack Socket Mode
            handler = SocketModeHandler(self.slack_app, self.config.SLACK_APP_TOKEN)
            handler.start()
            
            logger.info("SlackBot started successfully")
            
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")
            raise

# Task 8: Utility functions
def format_progress_message(progress: UserProgress) -> Dict[str, Any]:
    """Format user progress as Slack blocks"""
    # CRITICAL: Use Slack Block Kit for rich formatting
    # PATTERN: Include visual progress indicators
    
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Your Habit Progress*\n\n"
                       f"🔥 Current Streak: {progress.streak_count} days\n"
                       f"✅ Completed Today: {progress.completed_today}\n"
                       f"📊 Weekly Success Rate: {progress.weekly_rate}%"
            }
        }
    ]
    
    return {"blocks": blocks}

def parse_cron_expression(schedule_text: str) -> Dict[str, Any]:
    """Parse human-readable schedule to cron parameters"""
    # CRITICAL: Handle various schedule formats
    # PATTERN: Support both cron and natural language
    # GOTCHA: Validate cron expressions before use
    
    if schedule_text.startswith("every"):
        return parse_interval_schedule(schedule_text)
    elif ":" in schedule_text:
        return parse_time_schedule(schedule_text)
    else:
        return parse_cron_schedule(schedule_text)
```

### Integration Points

```yaml
GOOGLE_DOCS_API:
  - authentication: "Service account with documents.readonly scope"
  - document_format: "Structured headings and bullet points"
  - refresh_strategy: "Periodic reload every 6 hours"
  - error_handling: "Graceful fallback to cached habits"

SLACK_API:
  - socket_mode: "Internal app configuration with app-level token"
  - event_subscriptions: "app_mention, message.im, reaction_added"
  - slash_commands: "/habits with subcommands"
  - interactive_components: "Buttons and select menus for habit management"

SCHEDULER:
  - persistence: "SQLite job store for reliability"
  - timezone: "UTC for storage, user timezone for display"
  - error_handling: "Retry logic with exponential backoff"
  - monitoring: "Job execution logging and failure alerts"

DEPLOYMENT:
  - container: "Docker with multi-stage build"
  - environment: "12-factor app with environment variables"
  - health_check: "HTTP endpoint for monitoring"
  - scaling: "Horizontal scaling support with shared job store"
```

## Validation Loop

### Level 1: Syntax & Style

```bash
# Run these FIRST - fix any errors before proceeding
python -m ruff check src/ --fix
python -m ruff format src/
python -m mypy src/
python -m bandit -r src/

# Expected: No errors. If errors, READ the error and fix.
```

### Level 2: Unit Tests

```python
# CREATE tests/test_habit_manager.py with comprehensive test coverage
import pytest
from unittest.mock import Mock, patch
from src.slackbot.habit_manager import HabitManager, Habit, HabitType

class TestHabitManager:
    @pytest.fixture
    def habit_manager(self):
        mock_google_service = Mock()
        mock_slack_app = Mock()
        return HabitManager(mock_google_service, mock_slack_app)
    
    def test_load_habits_from_doc_success(self, habit_manager):
        """Test successful habit loading from Google Doc"""
        # Test implementation
        pass
    
    def test_schedule_habit_reminder_success(self, habit_manager):
        """Test successful habit reminder scheduling"""
        # Test implementation
        pass
    
    def test_handle_habit_completion(self, habit_manager):
        """Test habit completion tracking"""
        # Test implementation
        pass

# CREATE tests/test_google_docs.py for Google Docs integration
# CREATE tests/test_slack_handlers.py for Slack interaction testing
```

```bash
# Run comprehensive test suite
python -m pytest tests/ -v --cov=src --cov-report=html
python -m pytest tests/integration/ -v --slow

# Expected: All tests pass with >90% coverage
# If failing: Debug specific test, fix implementation, re-run
```

### Level 3: Integration Tests

```bash
# Start local test environment
docker-compose up -d

# Test Google Docs API integration
python -m pytest tests/integration/test_google_docs_integration.py -v

# Test Slack API integration with mock
python -m pytest tests/integration/test_slack_integration.py -v

# Test scheduler integration
python -m pytest tests/integration/test_scheduler_integration.py -v

# Expected: All integration tests pass
# If failing: Check API credentials, network connectivity, service availability
```

### Level 4: End-to-End Validation

```bash
# Start the application
python main.py

# Test health check endpoint
curl -f http://localhost:8000/health

# Test Slack integration (requires actual Slack workspace)
# Send test message to bot in Slack
# Use /habits status command
# React to habit reminder message
# Verify habit completion tracking

# Test Google Docs integration
# Update habits in Google Doc
# Verify bot picks up changes within refresh interval

# Test scheduler functionality
# Verify habit reminders are sent on schedule
# Check job persistence after restart

# Expected: All functionality works end-to-end
```

### Level 5: Performance & Load Testing

```bash
# Install performance testing tools
pip install locust pytest-benchmark

# Run performance tests
python -m pytest tests/performance/ -v --benchmark-only

# Run load tests
locust -f tests/load/test_slack_load.py --host=http://localhost:8000

# Expected: 
# - Response time < 3 seconds for Slack commands
# - Bot handles 100+ concurrent users
# - Memory usage stable over 24 hours
```

### Level 6: Security & Deployment Validation

```bash
# Security checks
python -m bandit -r src/
python -m safety check

# Docker build and test
docker build -t slackbot .
docker run --env-file .env.test slackbot

# Environment validation
python -c "from src.slackbot.config import Config; Config.validate()"

# Deployment smoke test
# Deploy to staging environment
# Run basic functionality tests
# Check logs for errors
# Verify monitoring and alerting

# Expected: No security vulnerabilities, successful deployment
```

### Level 7: Documentation & User Acceptance

```bash
# Validate documentation
python -m sphinx-build docs/ docs/_build/html
python -m doctest src/slackbot/*.py

# User acceptance testing
# Create test Google Doc with sample habits
# Invite test users to Slack workspace
# Walk through all user flows
# Collect feedback and iterate

# Expected: Documentation complete, users can successfully use the bot
```

### Debug Patterns

```bash
# DEBUG: Google Docs API issues
python -c "from src.slackbot.google_docs import GoogleDocsService; service = GoogleDocsService(); print(service.test_connection())"

# DEBUG: Slack API connection
python -c "from src.slackbot.config import Config; from slack_bolt import App; app = App(token=Config.SLACK_BOT_TOKEN); print(app.client.api_test())"

# DEBUG: Scheduler issues
python -c "from src.slackbot.scheduler import SchedulerService; s = SchedulerService(); s.start(); print(s.get_jobs())"

# DEBUG: Environment configuration
python -c "from src.slackbot.config import Config; Config.validate(); print('Configuration valid')"

# DEBUG: Habit parsing
python -c "from src.slackbot.habit_manager import HabitManager; hm = HabitManager(); print(hm.parse_test_doc())"
```

This comprehensive PRP provides all the necessary context, patterns, and validation steps needed to implement a production-ready Slackbot for promoting positive work habits. The implementation follows established patterns from the codebase while incorporating best practices for Slack bot development, Google API integration, and scheduled task management.

**Confidence Score: 9/10** - This PRP contains comprehensive context for one-pass implementation success with detailed patterns, gotchas, and validation loops. 