import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def split_csv_data(input_csv, label_column, test_size=0.2, random_state=None):
    # Read the CSV file using pandas
    df = pd.read_csv(input_csv)

    # Extract the feature columns (all columns except the label column)
    feature_columns = df.columns.difference([label_column])

    # Separate features and labels
    X = df[feature_columns]
    y = df[label_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Create DataFrames for training and testing sets
    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)

    # Write the DataFrames to CSV files with modified names
    train_csv = input_csv.replace(".csv", "_train.csv")
    test_csv = input_csv.replace(".csv", "_test.csv")

    train_df.to_csv(train_csv, index=False)
    test_df.to_csv(test_csv, index=False)


def csv_to_svmlight(input_csv, output_svmlight, label_column):
    # Read the CSV file using pandas
    df = pd.read_csv(input_csv)

    # Extract the feature columns (all columns except the label column)
    feature_columns = df.columns.difference([label_column])

    # Create a LabelEncoder to convert class labels to numeric values
    le = LabelEncoder()
    df[label_column] = le.fit_transform(df[label_column])

    df[label_column] = df[label_column].apply(lambda x: 1 if x == 1 else -1)

    # Create the SVM-Light format text file
    with open(output_svmlight, 'w') as output_file:
        for index, row in df.iterrows():
            # Write the label
            label = int(row[label_column])
            output_file.write(f"{label} ")

            # Write the features in SVM-Light format
            for col in feature_columns:
                value = row[col]
                output_file.write(f"{feature_columns.get_loc(col) + 1}:{value} ")

            output_file.write('\n')

if __name__ == '__main__':
    # Define the input and output file paths
    input = 'C:/Users/carlo/svm_light/Datasets/WQ/waterQuality2.csv'
    input_test = 'C:/Users/carlo/svm_light/Datasets/WQ/waterQuality2_test.csv'
    input_train = 'C:/Users/carlo/svm_light/Datasets/WQ/waterQuality2_train.csv'
    output_test = 'C:/Users/carlo/svm_light/Datasets/WQ/waterQuality2_test_C.csv'
    output_train = 'C:/Users/carlo/svm_light/Datasets/WQ/waterQuality2_train_C.csv'

    split_csv_data(input, "is_safe", test_size=0.2, random_state=42)
    csv_to_svmlight(input_test, output_test, "is_safe")
    csv_to_svmlight(input_train, output_train, "is_safe")