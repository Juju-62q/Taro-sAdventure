<?php

namespace ScoreApi\Controller;

use RestApi\Controller\ApiController;
use Score\Model\ScoreTable;

class ScoreApiController extends ApiController{

    private $table;

    public function __construct(ScoreTable $table){
        $this->table = $table;
    }

    public function highScoreAction()
    {
        //check get action
        if($this->getRequest()->isPost()){
            $this->httpStatusCode = 500;
            return $this->createResponse();
        }

        // your action logic
        $data = $this->table->getHighScore();

        // Set the HTTP status code. By default, it is set to 200
        $this->httpStatusCode = 200;

        // Set the response
        $this->apiResponse['name'] = $data->name;
        $this->apiResponse['score'] = $data->score;

        return $this->createResponse();
    }

    public function rankingAction()
    {
        //check get action
        if($this->getRequest()->isPost()){
            $this->httpStatusCode = 500;
            return $this->createResponse();
        }

        // your action logic
        $ranking = $this->table->getRanking();

        // Set the HTTP status code. By default, it is set to 200
        $this->httpStatusCode = 200;

        // Set the response
        $this->apiResponse['ranking'] = $ranking;

        return $this->createResponse();
    }

    public function addScoreAction()
    {
        if($this->getRequest()->isGet()){
            $this->httpStatusCode = 500;
            return $this->createResponse();
        }

        // your action logic
        $data = \Zend\Json\Json::decode(
            $this->getRequest()->getContent(),
            \Zend\Json\Json::TYPE_ARRAY
        );

        $rank = $this->table->addScore($data['score'], $data['name']);

        $this->httpStatusCode = 200;

        // Set the response
        $this->apiResponse['rank'] = $rank->id;

        return $this->createResponse();
    }

    public function getUserHighScoreAction(){
        if($this->getRequest()->isGet()){
            $this->httpStatusCode = 500;
            return $this->createResponse();
        }

        // your action logic
        $data = \Zend\Json\Json::decode(
            $this->getRequest()->getContent(),
            \Zend\Json\Json::TYPE_ARRAY
        );

        $rank = $this->table->getUserHighScore($data['name']);

        $this->httpStatusCode = 200;

        // Set the response
        if(empty($rank->score)){
            $this->apiResponse['score'] = 0;
        }else{
            $this->apiResponse['score'] = $rank->score;
        }

        return $this->createResponse();
    }
}
