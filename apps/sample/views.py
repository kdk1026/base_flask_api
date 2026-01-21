from dataclasses import asdict, dataclass
from flask import Blueprint, jsonify, request


sample_bp = Blueprint('sample', __name__)

@sample_bp.route('/sample')
def sample_index():
    return "This is Sample App"

# Person 객체 정의
@dataclass
class Person:
    seq: int
    name: str
    age: int

    def to_dict(self):
        return asdict(self)
    
# 메모리 DB 역할을 할 리스트
person_list = [
    Person(1, "홍길동", 20),
    Person(2, "임꺽정", 25)
]

NOT_FOUND = "Not Found"

@sample_bp.route('/sample/persons', methods=['GET'])
@sample_bp.route('/sample/persons/<int:seq>', methods=['GET'])
def get_persons(seq=None):
    if seq is None:
        return jsonify([p.to_dict() for p in person_list])
    
    person = next((p for p in person_list if p.seq == seq), None)
    if person:
        return jsonify(person.to_dict())
    
    return jsonify({"error": NOT_FOUND}), 404

@sample_bp.route('/sample/persons', methods=['POST'])
def add_person():
    data = request.json

    new_seq = person_list[-1].seq + 1 if person_list else 1
    new_person = Person(seq=new_seq, name=data['name'], age=data['age'])
    person_list.append(new_person)

    return jsonify({"result": "success"}), 201

@sample_bp.route('/sample/persons', methods=['PUT'])
def update_person():
    data = request.json

    person = next((p for p in person_list if p.seq == data['seq']), None)
    if person:
        person.name = data['name']
        person.age = data['age']
        return jsonify({"result": "success"})
    
    return jsonify({"error": "Not Found"}), 404

@sample_bp.route('/sample/persons/<int:seq>', methods=['DELETE'])
def delete_person(seq):
    global person_list

    person = next((p for p in person_list if p.seq == seq), None)
    if person:
        return jsonify({"result": "success"})

    return jsonify({"error": "Not Found"}), 404