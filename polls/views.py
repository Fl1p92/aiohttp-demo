import aiohttp_jinja2
from aiohttp import web

from polls import models


@aiohttp_jinja2.template('detail.html')
async def poll(request):
    async with request.app['db'].acquire() as conn:
        question_id = request.match_info['question_id']
        try:
            question, choices = await models.get_question(conn, question_id)
        except models.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        return {
            'question': question,
            'choices': choices
        }
