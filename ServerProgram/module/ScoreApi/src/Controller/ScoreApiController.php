<?php
/**
 * Created by PhpStorm.
 * User: kenya
 * Date: 18/02/15
 * Time: 22:50
 */
namespace ScoreApi\Controller;

use Zend\Mvc\Controller\AbstractRestfulController;

use Zend\View\Model\JsonModel;
use Zend\EventManager\EventManagerInterface;
use Firebase\JWT\JWT;

use Score\Model\ScoreTable;
use Score\Form\ScoreForm;

class ScoreApiController extends AbstractRestfulController{

    public $httpStatusCode = 200;
    public $apiResponse;
    public $token;
    public $tokenPayLoad;

}