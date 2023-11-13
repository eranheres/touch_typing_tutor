## Original Requirements

Create a console application for practicing touch typing. The application should store the user's progress and collect statistics on the user's progress. The statistics should be collected historically and should be as extensive as possible including timing and performance. The application should have the option to decide the language of the text to be typed English or Hebrew (RTL).

## Product Goals

- Create an engaging touch typing practice tool
- Provide comprehensive progress tracking and statistics
- Support multiple languages including English and Hebrew

## User Stories

- As a user, I want to practice touch typing in a console application
- As a user, I want to track my progress over time
- As a user, I want to see detailed statistics about my typing performance
- As a user, I want to choose the language of the text I am typing
- As a user, I want my progress to be saved so I can continue where I left off

## Competitive Analysis

- TypingMaster: Offers comprehensive courses but lacks console application
- Ratatype: Provides detailed statistics but does not support Hebrew
- Typing.com: Supports multiple languages but lacks historical tracking
- Keybr: Offers console application but lacks language selection
- TypingClub: Provides progress tracking but lacks extensive statistics

## Competitive Quadrant Chart

quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    TypingMaster: [0.3, 0.6]
    Ratatype: [0.45, 0.23]
    Typing.com: [0.57, 0.69]
    Keybr: [0.78, 0.34]
    TypingClub: [0.40, 0.34]
    Our Target Product: [0.5, 0.6]

## Requirement Analysis

The product needs to be a console application that allows users to practice touch typing. It should track user's progress and provide detailed statistics. It should also support multiple languages including English and Hebrew.

## Requirement Pool

- ['Create a console application for touch typing practice', 'P0']
- ['Implement progress tracking', 'P0']
- ['Collect and display detailed statistics', 'P0']
- ['Support English and Hebrew languages', 'P0']
- ["Implement a system to save and load user's progress", 'P1']

## UI Design draft

The console application will have a clean and minimalistic design. It will display the text to be typed at the top, the user's input at the bottom, and the progress and statistics on the side. The language selection will be available in the settings menu.

## Anything UNCLEAR

The specific statistics to be collected are not specified. Assuming it includes typing speed, accuracy, and time spent practicing.

