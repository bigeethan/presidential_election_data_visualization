import pandas as pd
import matplotlib.pyplot as matplot
import csv

print("Enter the election year (1940 to 2020)")
year = input()
print("Enter the state")
state = input()
index = 0
d_can = ""
r_can = ""
i_can = ""
is_2_candidate_race = True

#Get the list index of each state
#unefficient but could not get index from element due to the structure of the csv data
if int(year) < 1960:
    if state.upper() == "ALABAMA":
        index = 0
    elif state.upper() == "ARIZONA":
        index = 1
    elif state.upper() == "ARKANSAS":
        index = 2
    elif state.upper() == "CALIFORNIA":
        index = 3
    elif state.upper() == "COLORADO":
        index = 4
    elif state.upper() == "CONNECTICUT":
        index = 5
    elif state.upper() == "DELAWARE":
        index = 6
    elif state.upper() == "FLORIDA":
        index = 7
    elif state.upper() == "GEORGIA":
        index = 8
    elif state.upper() == "IDAHO":
        index = 9
    elif state.upper() == "ILLINOIS":
        index = 10
    elif state.upper() == "INDIANA":
        index = 11
    elif state.upper() == "IOWA":
        index = 12
    elif state.upper() == "KANSAS":
        index = 13
    elif state.upper() == "KENTUCKY":
        index = 14
    elif state.upper() == "LOUISIANA":
        index = 15
    elif state.upper() == "MAINE":
        index = 16
    elif state.upper() == "MARYLAND":
        index = 17
    elif state.upper() == "MASSACHUSETTS":
        index = 18
    elif state.upper() == "MICHIGAN":
        index = 19
    elif state.upper() == "MINNESOTA":
        index = 20
    elif state.upper() == "MISSISSIPPI":
        index = 21
    elif state.upper() == "MISSOURI":
        index = 22
    elif state.upper() == "MONTANA":
        index = 23
    elif state.upper() == "NEBRASKA":
        index = 24
    elif state.upper() == "NEVADA":
        index = 25
    elif state.upper() == "NEW HAMPSHIRE":
        index = 26
    elif state.upper() == "NEW JERSEY":
        index = 27
    elif state.upper() == "NEW MEXICO":
        index = 28
    elif state.upper() == "NEW YORK":
        index = 29
    elif state.upper() == "NORTH CAROLINA":
        index = 30
    elif state.upper() == "NORTH DAKOTA":
        index = 31
    elif state.upper() == "OHIO":
        index = 32
    elif state.upper() == "OKLAHOMA":
        index = 33
    elif state.upper() == "OREGON":
        index = 34
    elif state.upper() == "PENNSYLVANIA":
        index = 35
    elif state.upper() == "RHODE ISLAND":
        index = 36
    elif state.upper() == "SOUTH CAROLINA":
        index = 37
    elif state.upper() == "SOUTH DAKOTA":
        index = 38
    elif state.upper() == "TENNESSEE":
        index = 39
    elif state.upper() == "TEXAS":
        index = 40
    elif state.upper() == "UTAH":
        index = 41
    elif state.upper() == "VERMONT":
        index = 42
    elif state.upper() == "VIRGINIA":
        index = 43
    elif state.upper() == "WASHINGTON":
        index = 44
    elif state.upper() == "WEST VIRGINIA":
        index = 45
    elif state.upper() == "WISCONSIN":
        index = 46
    elif state.upper() == "WYOMING":
        index = 47
elif int(year) >= 1960:
    if state.upper() == "ALABAMA":
        index = 0
    elif state.upper() == "ALASKA":
        index = 1
    elif state.upper() == "ARIZONA":
        index = 2
    elif state.upper() == "ARKANSAS":
        index = 3
    elif state.upper() == "CALIFORNIA":
        index = 4
    elif state.upper() == "COLORADO":
        index = 5
    elif state.upper() == "CONNECTICUT":
        index = 6
    elif state.upper() == "DELAWARE":
        index = 7
    elif state.upper() == "FLORIDA":
        index = 8
    elif state.upper() == "GEORGIA":
        index = 9
    elif state.upper() == "HAWAII":
        index = 10
    elif state.upper() == "IDAHO":
        index = 11
    elif state.upper() == "ILLINOIS":
        index = 12
    elif state.upper() == "INDIANA":
        index = 13
    elif state.upper() == "IOWA":
        index = 14
    elif state.upper() == "KANSAS":
        index = 15
    elif state.upper() == "KENTUCKY":
        index = 16
    elif state.upper() == "LOUISIANA":
        index = 17
    elif state.upper() == "MAINE":
        index = 18
    elif state.upper() == "MARYLAND":
        index = 19
    elif state.upper() == "MASSACHUSETTS":
        index = 20
    elif state.upper() == "MICHIGAN":
        index = 21
    elif state.upper() == "MINNESOTA":
        index = 22
    elif state.upper() == "MISSISSIPPI":
        index = 23
    elif state.upper() == "MISSOURI":
        index = 24
    elif state.upper() == "MONTANA":
        index = 25
    elif state.upper() == "NEBRASKA":
        index = 26
    elif state.upper() == "NEVADA":
        index = 27
    elif state.upper() == "NEW HAMPSHIRE":
        index = 28
    elif state.upper() == "NEW JERSEY":
        index = 29
    elif state.upper() == "NORTH MEXICO":
        index = 30
    elif state.upper() == "NORTH YORK":
        index = 31
    elif state.upper() == "NORTH CAROLINA":
        index = 32
    elif state.upper() == "NORTH DAKOTA":
        index = 33
    elif state.upper() == "OHIO":
        index = 34
    elif state.upper() == "OKLAHOMA":
        index = 35
    elif state.upper() == "OREGON":
        index = 36
    elif state.upper() == "PENNSYLVANIA":
        index = 37
    elif state.upper() == "RHODE ISLAND":
        index = 38
    elif state.upper() == "SOUTH CAROLINA":
        index = 39
    elif state.upper() == "SOUTH DAKOTA":
        index = 40
    elif state.upper() == "TENNESSEE":
        index = 41
    elif state.upper() == "TEXAS":
        index = 42
    elif state.upper() == "UTAH":
        index = 43
    elif state.upper() == "VERMONT":
        index = 44
    elif state.upper() == "VIRGINIA":
        index = 45
    elif state.upper() == "WASHINGTON":
        index = 46
    elif state.upper() == "WEST VIRGINIA":
        index = 47
    elif state.upper() == "WISCONSIN":
        index = 48
    elif state.upper() == "WYOMING":
        index = 49

#Get the names of each candidate in each election
if int(year) == 1940 or int(year) == 1944:
    d_can = 'FRANKLIN D. ROOSEVELT'
    if int(year) == 1940:
        r_can = 'WENDELL WILLKIE'
    else:
        r_can = 'THOMAS E. DEWEY'
elif int(year) == 1948:
    d_can = 'HARRY S TRUMAN'
    r_can = 'THOMAS E. DEWEY'
    i_can = 'STROM THURMOND'
    is_2_candidate_race = False
elif int(year) == 1952 or int(year) == 1956:
    d_can = 'ADLAI E. STEVENSON'
    r_can = 'DWIGHT D. EISENHOWER'
elif int(year) == 1960 or int(year) == 1968 or int(year) == 1972:
    if int(year) == 1960:
        d_can = 'JOHN F. KENNEDY'
        r_can = 'RICHARD M. NIXON'
    elif int(year) == 1968:
        r_can = 'RICHARD M. NIXON'
        d_can = 'HUBERT HUMPHREY'
        i_can = 'GEORGE WALLACE'
        is_2_candidate_race = False
    else:
        r_can = 'RICHARD M. NIXON'
        d_can = 'GEORGE McGOVERN'
elif int(year) == 1964:
    d_can = 'LYNDON B. JOHNSON'
    r_can = 'BARRY M. GOLDWATER'
elif int(year) == 1976 or int(year) == 1980 or int(year) == 1984:
    if int(year) == 1976:
        d_can = 'JIMMY CARTER'
        r_can = 'GERALD FORD'
    elif int(year) == 1980:
        r_can = 'RONALD REAGAN'
        d_can = 'JIMMY CARTER'
        i_can = 'JOHN ANDERSON'
        is_2_candidate_race = False
    else:
        r_can = 'RONALD REAGAN'
        d_can = 'WALTER MONDALE'
elif int(year) == 1988 or int(year) == 1992 or int(year) == 1996:
    if int(year) == 1988:
        d_can = 'MICHAEL S. DUKAKIS'
        r_can = 'GEORGE HW BUSH'
    elif int(year) == 1992:
        r_can = 'GEORGE HW BUSH'
        d_can = 'BILL CLINTON'
        i_can = 'ROSS PEROT'
        is_2_candidate_race = False
    else:
        r_can = 'BOB DOLE'
        d_can = 'BILL CLINTON'
        i_can = 'ROSS PEROT'
        is_2_candidate_race = False
elif int(year) == 2000 or int(year) == 2004:
    if int(year) == 2000:
        d_can = 'AL GORE'
        r_can = 'GEORGE W. BUSH'
        i_can = 'RALPH NADER'
        is_2_candidate_race = False
    else:
        r_can = 'GEORGE W. BUSH'
        d_can = 'JOHN KERRY'
elif int(year) == 2008 or int(year) == 2012:
    if int(year) == 2008:
        d_can = 'BARACK OBAMA'
        r_can = 'JOHN McCAIN'
    else:
        r_can = 'MITT ROMNEY'
        d_can = 'BARACK OBAMA'
elif int(year) == 2016 or int(year) == 2020:
    if int(year) == 2016:
        d_can = 'HILLARY CLINTON'
        r_can = 'DONALD TRUMP'
        i_can = 'GARY JOHNSON'
        is_2_candidate_race = False
    else:
        r_can = 'DONALD TRUMP'
        d_can = 'JOE BIDEN'

def add_labels(x, y):
    for i in range(len(x)):
        matplot.text(i, y[i] // 2, y[i], ha='center')

#Save data from csv file
with open(f'data/{year}.csv') as file:
    data = []
    csv = csv.DictReader(file)
    for row in csv:
        data.append(row)

#Get and save the candidate and vote data
election_data = (data[index])
if is_2_candidate_race:
    state_data = {
        "Candidates": [f'{r_can}', f'{d_can}'],
        "Votes": [int(election_data[f'{r_can} VOTES']), int(election_data[f'{d_can} VOTES'])]
    }
else:
    state_data = {
        "Candidates": [f'{r_can}', f'{d_can}', f'{i_can}'],
        "Votes": [int(election_data[f'{r_can} VOTES']), int(election_data[f'{d_can} VOTES']), int(election_data[f'{i_can} VOTES'])]
    }
votes = pd.DataFrame(state_data)

#Display the vote data in a bar graph
matplot.bar(votes["Candidates"], votes["Votes"])
matplot.title(f"{year} Presidential Election in {election_data['STATE']}")
add_labels(votes["Candidates"], votes["Votes"])
matplot.show()