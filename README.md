# fintuser

[Notion documentation](https://adaptive-omelet-0bd.notion.site/fine-tuning-data-service-FTDS-16854548733a8020b2ecfb9fbb560a29?pvs=4)


## Introduction

I want to have an LLM-powered "CV reviewer" as a part of my CVAI project.

I have [the following chat in Telegram](https://t.me/resume_review), where engineers review the CVs of other engineers.

The idea is to use the reviews from this chat for fine-tuning an LLM.


## Description
A repository with the python scripts needed for creating a dataset from fine-tuning and submitting all the jobs.


- [create-message-chains.py](src/create_message_chains.py) takes care of transformation unstructured data into `ProcessedMessages` type.
- [transform_chat_data.py](src/transform_chat_data.py) takes the output of `create-message-chains.py`, and uses gpt-4o-mini to translate the text into english and add a yaml representation of PDF documents. So we can fine-tune both on raw documents and the transcriptions of the documents.
- [submit-finetune-job](src/submit_finetune_job.py) uploads a file with a fine-tuning dataset and submits a job
- [build-finetune-dataset](src/build_finetune_dataset.py) creates a dataset for fine-tuning given the data in the database
- [save-out-dir-to-db](src/save_out_dir_to_db.py) parser a directory with chatgpt dataset & pdf translations jobs output into prisma db. needs changes
