<?php

namespace ScoreApi\Controller;

use RestApi\Controller\ApiController;

class ScoreApiController extends ApiController{

    public function highScoreAction()
    {
        // your action logic

        // Set the HTTP status code. By default, it is set to 200
        $this->httpStatusCode = 200;

        // Set the response
        $this->apiResponse['you_response'] = 'your response data';

        return $this->createResponse();
    }
}