<?php
namespace Score\Model;

class Score{
    public $id;
    public $score;
    public $name;
    public $created_at;

    public function exchangeArray(array $data){
        $this->id = !empty(data['id']) ? $data['id'] : null;
        $this->score = !empty(data['score']) ? $data['score'] : null;
        $this->name = !empty(data['name']) ? $data['name'] : null;
        $this->created_at = !empty(data['created_at']) ? $data['created_at'] : null;
    }
}