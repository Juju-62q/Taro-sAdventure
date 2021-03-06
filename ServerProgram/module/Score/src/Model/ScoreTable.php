<?php
namespace Score\Model;
use RuntimeException;
use Zend\Db\TableGateway\TableGatewayInterface;
use Zend\Db\Sql\Select;


class ScoreTable{
    private $tableGateway;

    public function __construct(TableGatewayInterface $tableGateway){
        $this->tableGateway = $tableGateway;
    }

    public function fetchAll(){
        return $this->tableGateway->select();
    }

    public function getScore($id){
        $rows = $this->tableGateway->select(
            ['id' => $id]
        );
        $row = $rows->current();
        if (! $row) {
            throw new RuntimeException(sprintf(
                'Could not find row with identifier %d,%d',
                $id
            ));
        }
        return $row;
    }

    public function saveScore(Score $s){
        try{
            $row = $this->getScore($s->id);
            $data = [
                'score' => $s->score,
                'name' => $s->name,
                'created_at' => $s->created_at
            ];
            $this->tableGateway->update($data,
                ['id' => $s->id,]);

        }catch (\Exception $exception){
            $data = [
                'id' => $s->id,
                'score' => $s->score,
                'name' => $s->name,
                'created_at' => $s->created_at
            ];
            $this->tableGateway->insert($data);
            return;
        }
    }

    public function deleteScore($id){
        $this->tableGateway->delete(['id' =>$id]);
    }

    public function getHighScore(){
        return $this->tableGateway->select(
            function (Select $select) {
                $select->columns(array('name','score'))->order('score DESC')->limit(1);
            })->current();
    }

    public function getRanking(){
        $data = $this->tableGateway->select(
            function (Select $select) {
                $select->order('score DESC')->limit(10);
            });
        $ret = array();
        foreach ($data as $item) {
            array_push($ret, $item);
        }
        return $ret;
    }

    public function addScore($score, $name){
        // add Score
        $values = array(
            'score'  => $score,
            'name' => $name,
        );
        $this->tableGateway->insert($values);

        // get rank
        $select = $this->tableGateway->getSql()->select();
        $select->columns(array('id' => new \Zend\Db\Sql\Predicate\Expression('COUNT(*) + 1')))->where->greaterThan('score', $score);

        // return rank
        return $this->tableGateway->selectWith($select)->current();
    }

    public function getUserHighScore($name){
        $select = $this->tableGateway->getSql()->select();
        $select->columns(array('score'))->order('score DESC')->limit(1)->where->equalTo('name', "$name");

        return $this->tableGateway->selectWith($select)->current();
    }

}