FROM astrocrpublic.azurecr.io/runtime:3.0-2


# Create and activate dbt venv
# This venv will be available to all containers built from this image
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && deactivate

