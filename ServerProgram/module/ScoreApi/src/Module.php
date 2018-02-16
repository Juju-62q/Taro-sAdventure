<?php
namespace ScoreApi;

use Score\Model\Score;
use Zend\ModuleManager\Feature\ConfigProviderInterface;
use Score\Model\ScoreTable;

use Zend\Db\Adapter\AdapterInterface;
use Zend\Db\ResultSet\ResultSet;
use Zend\Db\TableGateway\TableGateway;


class Module implements ConfigProviderInterface{
    public function getConfig(){
        return include __DIR__ . '/../config/module.config.php';
    }

    public function getServiceConfig(){
        return [
            'factories' =>[
                ScoreTable::class => function($container){
                    $tableGateway = $container->get(ScoreTableGateway::class);
                    return new ScoreTable($tableGateway);
                },
                ScoreTableGateway::class => function($container){
                    $dbAdapter = $container->get(AdapterInterface::class);
                    $resultSetPrototype = new ResultSet();
                    $resultSetPrototype->setArrayObjectPrototype(new Score());
                    return new Tablegateway('score',$dbAdapter,null,$resultSetPrototype);
                },
            ],
        ];
    }

    public function getControllerConfig(){
        return [
            'factories' => [
                Controller\ScoreApiController::class => function($container){
                    return new Controller\ScoreApiController(
                        $container->get(ScoreTable::class)
                    );
                },
            ],
        ];
    }
}