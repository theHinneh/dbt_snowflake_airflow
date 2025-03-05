# Data Pipeline Project

This project demostrates the ELT process using Snowflake, dbt, and Airflow

## Project Structure

Here is an overview of the project structure:

- **analyses/**: Directory for storing analysis queries.
- **dbt_packages/**: Contains dbt packages, including `dbt_utils` which provides useful macros.
- **dbt_project.yml**: The main configuration file for the dbt project.
- **logs/**: Directory for storing log files.
- **macros/**: Directory for storing custom macros.
- **models/**: Directory for storing dbt models, organized into marts and staging.
- **seeds/**: Directory for storing seed files.
- **snapshots/**: Directory for storing snapshot files.
- **target/**: Directory for storing compiled SQL files and other artifacts.
- **tests/**: Directory for storing test files.

### Running the project

These commands are used to run and test the project respectively.

- `dbt run`
- `dbt test`

The test includes a generic test and two individual tests.