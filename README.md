# Canvas Gradebook Zeros
This python script was made because Canvas does not take into account missing assignments when displaying grades. Therefore instructors must go column by column adding zeros so that students can see their actual current grade.

This repository contains ```canvas_gradebook_zeros.py``` which will take the most recent ```*.CSV``` file from your current directory, read the file, and create a new ```*_with_zeros.CSV``` file which adds zeros to all missing assignments. 

When exporting the CSV from Canvas, be sure to display only the assignments that wish to edit and not the entire Gradebook.
