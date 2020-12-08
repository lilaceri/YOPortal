import csv

# get data from given tablename
def get_data(tablename):
  filename = 'data/yop-' + tablename + '.csv'
  with open(filename) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      columns = {}
      user_list = []
      for row in csv_reader:
          if line_count == 0:
            for column in row:
              columns[column] = ""
              line_count += 1
          else:
            user_data = {}
            index = 0
            for column in columns:
              user_data[column] = row[index]
              index += 1
            user_list.append(user_data)
  return user_list