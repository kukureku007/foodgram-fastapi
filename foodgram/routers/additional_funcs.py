from io import BytesIO

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import xlsxwriter

additional_router = APIRouter(
    prefix='/api/additional',
)


@additional_router.get("/files/xlsx", response_description='xlsx')
async def payments():
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'ISBN')
    worksheet.write(0, 1, 'Name')
    worksheet.write(0, 2, 'Takedown date')
    worksheet.write(0, 3, 'Last updated')
    workbook.close()
    output.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="filename.xlsx"'
    }
    return StreamingResponse(output, headers=headers)
