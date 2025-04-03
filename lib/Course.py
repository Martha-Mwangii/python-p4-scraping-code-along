class Course:
    def __init__(self, title="Untitled Course", schedule="Full-Time", description="No description provided"):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
        output += '------------------'
        return output






