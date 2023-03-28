'''
Goal: 
- Make a function that takes ~docs/skills.md (or .txt if I change it later) and plots it like a video game skill tree. 

Needs:
- a dataframe containing the following collumns:
    - Index id
    - General Tree Name (Group skills by the big over terms data scientist are expected to have ('math', 'programming', 'commincation', etc.))
    - The skill's name itself
    - A list of skills you believe were prerequisite for it
    - Date you believe the skill was learned
    - Date skill was actually documented as learned (in case you don't know when you learned the skill)
 - it needs to be able to parse the list of skills and remove skills that were needed for other skills (show only the end most skills in the tree
 - detect when the skill tree circles upon itself (ex: if then statements > for loops > if then statements)
 - plot the dataframe as a visual skill tree
 
Why:
 - As I record the skills I gain this might be a neat and informative representation of what I've learned.
 - This also gives a road map for helping others to learn what I've learned. You could use it for article ideas to write about.

Key Branches:
- Data Cleaning (Preparation)
- Data Visualization (Presentation)
- Data Mining (Collection)
- Database Managment (Access & Storage)
- Data Analysis 
- Artificial Intelligence
- Error Handling (Debugging)
- Data Security
'''


