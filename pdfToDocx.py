import os
import time
from threading import Thread
import asyncio
from concurrent.futures import ThreadPoolExecutor
from pdf2docx import Converter

#Fungsi untuk mengonversi file PDF ke DOCX menggunakan pdf2docx.
def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print(f"Converted {pdf_file} to {docx_file}")

#Mengonversi menggunakan multithreading
def convert_with_multithreading(pdf_folder, docx_folder):
    os.makedirs(docx_folder, exist_ok=True)
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    threads = []
    start_time = time.time()
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        docx_path = os.path.join(docx_folder, pdf_file.replace(".pdf", ".docx"))
        
        thread = Thread(target=convert_pdf_to_docx, args=(pdf_path, docx_path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Multithreading conversion time: {end_time - start_time} seconds")

async def convert_with_asyncio(pdf_folder, docx_folder):
    os.makedirs(docx_folder, exist_ok=True)
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    start_time = time.time()
    
    tasks = [
        asyncio.to_thread(
            convert_pdf_to_docx,
            os.path.join(pdf_folder, pdf_file),
            os.path.join(docx_folder, pdf_file.replace(".pdf", ".docx"))
        )
        for pdf_file in pdf_files
    ]
    await asyncio.gather(*tasks) 

    end_time = time.time()
    print(f"Asyncio (await) conversion time: {end_time - start_time} seconds")

if __name__ == "__main__":
    input_folder = "/home/me/Documents/sharing_session/code-2/Docs"
    output_folder = "/home/me/Documents/sharing_session/code-2/Docs"

    print("\nStarting multithreading test...")
    convert_with_multithreading(input_folder, output_folder)

    print("\nStarting asyncio test...")
    asyncio.run(convert_with_asyncio(input_folder, output_folder))
