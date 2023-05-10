from typing import Any, Union, Optional, Dict, Iterable

from marshmallow.exceptions import ValidationError

from builder import build_query
from functions import check_path
from model import RequestSchema
from flask import Flask, request, jsonify, Response, Request

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query() -> Union[Response, tuple[Response, int], str]:
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    data: Dict = request.json
    print(type(data))
    try:
        data = RequestSchema().load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    if not check_path(file_name=data["file_name"]):
        return "Файла  не существует"

    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    first_result: Optional[list[str]] = build_query(
        cmd=data['cmd1'],
        value=data['value1'],
        file_name=data['file_name'],
        data=None,
    )
    second_result: Optional[list[str]] = build_query(
        cmd=data['cmd2'],
        value=data['value2'],
        file_name=data['file_name'],
        data=first_result,
    )
    # вернуть пользователю сформированный результат
    return jsonify(second_result)


if __name__ == '__main__':
    app.run()

