from process_document import process_document_sample

result = process_document_sample(
    file_path=r'D:\Tally Solutions Pvt. Ltd\Tally-AI - DocAI\Data\GST\1_GST.pdf'
)

page1_json = result.pages[0]

print(page1_json.form_fields)