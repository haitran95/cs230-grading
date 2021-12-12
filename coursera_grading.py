# Imports
import pandas as pd


def course1_info():
    file_path = 'csv_files/course1_gradebook.csv'
    quiz_names = ['Introduction to deep learning', 'Neural Network Basics', 'Shallow Neural Networks',
                  'Key concepts on Deep Neural Networks']
    assn_names = ['Logistic Regression with a Neural Network Mindset',
                  'Planar Data Classification with One Hidden Layer',
                  'Building your Deep Neural Network: Step by Step', 'Deep Neural Network - Application']
    return file_path, quiz_names, assn_names


def course2_info():
    file_path = 'csv_files/course2_gradebook.csv'
    quiz_names = ['Practical aspects of deep learning', 'Optimization algorithms',
                  'Hyperparameter tuning, Batch Normalization, Programming Frameworks', ]
    assn_names = ['Initialization', 'Regularization', 'Gradient Checking', 'Optimization', 'Tensorflow']
    return file_path, quiz_names, assn_names


def course3_info():
    file_path = 'csv_files/course3_gradebook.csv'
    quiz_names = ['Bird Recognition in the City of Peacetopia (Case Study)', 'Autonomous Driving (Case Study)']
    assn_names = []
    return file_path, quiz_names, assn_names


def course4_info():
    file_path = 'csv_files/course4_gradebook.csv'
    quiz_names = ['The basics of ConvNets', 'Deep convolutional models', 'Detection algorithms',
                  'Special applications: Face recognition & Neural style transfer', ]
    assn_names = ['Convolutional Model: step by step', 'Convolutional model: application', 'Residual Networks',
                  'Car detection with YOLO', 'Art generation with Neural Style Transfer', 'Face Recognition']
    return file_path, quiz_names, assn_names


def course5_info():
    file_path = 'csv_files/course5_gradebook.csv'
    quiz_names = ['Recurrent Neural Networks', 'Natural Language Processing & Word Embeddings',
                  'Sequence models & Attention mechanism', ]
    assn_names = ['Building a recurrent neural network - step by step',
                  'Dinosaur Island - Character-Level Language Modeling', 'Jazz improvisation with LSTM',
                  'Operations on word vectors - Debiasing', 'Emojify', 'Neural Machine Translation with Attention',
                  'Trigger word detection']
    return file_path, quiz_names, assn_names


def import_roster(file_path):
    df = pd.read_csv(file_path, usecols=['Email Address'])
    roster = df['Email Address'].tolist()
    # Completing incomplete
    roster.remove('hassanf@stanford.edu')
    # Dropped course
    roster.remove('jasonwzm@stanford.edu')
    roster.remove('soyeon1@stanford.edu')
    roster.remove('jakaba@stanford.edu')
    roster.remove('jordanwr@stanford.edu')
    roster.remove('agondi@stanford.edu')
    roster.remove('chopra14@stanford.edu')
    roster.remove('kborden@stanford.edu')
    roster.remove('rajlaxmi@stanford.edu')
    # Coursera issues
    roster.remove('reetika@stanford.edu')
    roster.remove('selenas@stanford.edu')
    # Missing for some reason (Added now)
    roster += ['jangs7078@gmail.com']
    roster += ['gabrielspil@outlook.com']
    # Sort alphabetically
    roster.sort()
    return roster


def import_grades(file_path, quiz_names, assn_names):
    quiz_cols = ['Points Scored: ' + name for name in quiz_names]
    assn_cols = ['Points Scored: ' + name for name in assn_names]
    cols = ['Email'] + quiz_cols + assn_cols
    df = pd.read_csv(file_path, usecols=cols)
    df.set_index('Email', inplace=True)
    return df


class Coursera:
    def __init__(self):
        # Roster
        self.roster = import_roster('csv_files/F21-CS-230-01.csv')
        self.replacements = {'bjang1@stanford.edu': 'jangs7078@gmail.com',
                             'gspil@stanford.edu': 'gabrielspil@outlook.com'}
        # Course 1
        self.course1_file_path, self.course1_quiz_names, self.course1_assn_names = course1_info()
        self.course1_df = import_grades(self.course1_file_path, self.course1_quiz_names, self.course1_assn_names)
        self.course1_df.fillna(0)
        self.course1_quiz_names = ['Points Scored: ' + name for name in self.course1_quiz_names]
        self.course1_assn_names = ['Points Scored: ' + name for name in self.course1_assn_names]
        # Course 2
        self.course2_file_path, self.course2_quiz_names, self.course2_assn_names = course2_info()
        self.course2_df = import_grades(self.course2_file_path, self.course2_quiz_names, self.course2_assn_names)
        self.course2_df.fillna(0)
        self.course2_quiz_names = ['Points Scored: ' + name for name in self.course2_quiz_names]
        self.course2_assn_names = ['Points Scored: ' + name for name in self.course2_assn_names]
        # Course 3
        self.course3_file_path, self.course3_quiz_names, self.course3_assn_names = course3_info()
        self.course3_df = import_grades(self.course3_file_path, self.course3_quiz_names, self.course3_assn_names)
        self.course3_df.fillna(0)
        self.course3_quiz_names = ['Points Scored: ' + name for name in self.course3_quiz_names]
        self.course3_assn_names = ['Points Scored: ' + name for name in self.course3_assn_names]
        # Course 4
        self.course4_file_path, self.course4_quiz_names, self.course4_assn_names = course4_info()
        self.course4_df = import_grades(self.course4_file_path, self.course4_quiz_names, self.course4_assn_names)
        self.course4_df.fillna(0)
        self.course4_quiz_names = ['Points Scored: ' + name for name in self.course4_quiz_names]
        self.course4_assn_names = ['Points Scored: ' + name for name in self.course4_assn_names]
        # Course 5
        self.course5_file_path, self.course5_quiz_names, self.course5_assn_names = course5_info()
        self.course5_df = import_grades(self.course5_file_path, self.course5_quiz_names, self.course5_assn_names)
        self.course5_df.fillna(0)
        self.course5_quiz_names = ['Points Scored: ' + name for name in self.course5_quiz_names]
        self.course5_assn_names = ['Points Scored: ' + name for name in self.course5_assn_names]
        # Grades
        self.grades = dict()
        for name in self.roster:
            self.grades[name] = {'quiz': 0, 'assn': 0, 'late_days': 0}
        self.compute_grades(self.course1_df, self.course1_quiz_names, self.course1_assn_names)
        self.compute_grades(self.course2_df, self.course2_quiz_names, self.course2_assn_names)
        self.compute_grades(self.course3_df, self.course3_quiz_names, self.course3_assn_names)
        self.compute_grades(self.course4_df, self.course4_quiz_names, self.course4_assn_names)
        self.compute_grades(self.course5_df, self.course5_quiz_names, self.course5_assn_names)
        # Normalize grades
        max_quiz = 0
        max_assn = 0
        for name in self.roster:
            if max_quiz < self.grades[name]['quiz']:
                max_quiz = self.grades[name]['quiz']
            if max_assn < self.grades[name]['assn']:
                max_assn = self.grades[name]['assn']
        # Not sure why but the max is twice the actual maximum (someone's coursera grade is double)
        max_quiz /= 2
        max_assn /= 2
        for name in self.roster:
            self.grades[name]['quiz'] /= max_quiz
            self.grades[name]['assn'] /= max_assn

    def compute_grades(self, df, quiz_names, assn_names):
        for name in self.roster:
            quiz_total = 0
            assn_total = 0
            if name in list(self.replacements.keys()):
                name = self.replacements[name]
            for col in df.columns:
                score = df.loc[name][col]
                if isinstance(score, pd.Series):
                    score = score.iloc[-1]
                if col in quiz_names:
                    quiz_total += score
                elif col in assn_names:
                    assn_total += score
            self.grades[name]['quiz'] += quiz_total
            self.grades[name]['assn'] += assn_total

    def export_grades(self):
        for name in self.roster:
            if self.grades[name]['quiz'] > 1.0:
                print('QUIZ SCORE ERROR:', name, self.grades[name]['quiz'])
            if self.grades[name]['quiz'] > 1.0:
                print('ASSN SCORE ERROR:', name, self.grades[name]['assn'])
            print(name, '| quiz total:', self.grades[name]['quiz'], '| assn total:', self.grades[name]['assn'])


if __name__ == '__main__':
    coursera = Coursera()
    coursera.export_grades()
