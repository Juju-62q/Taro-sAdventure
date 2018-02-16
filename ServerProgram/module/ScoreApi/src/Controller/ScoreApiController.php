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
        // your action logic
        $ranking = $this->table->getRanking();

        // Set the HTTP status code. By default, it is set to 200
        $this->httpStatusCode = 200;

        // Set the response
        $this->apiResponse['ranking'] = $ranking;

        return $this->createResponse();
    }
}
