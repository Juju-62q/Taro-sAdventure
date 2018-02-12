<?php
namespace Score;

use Zend\Db\Adapter\AdapterInterface;
use Zend\Db\ResultSet\ResultSet;
use Zend\Db\TableGateway\TableGateway;
 
use Zend\ModuleManager\Feature\ConfigProviderInterface;
 
class Module implements ConfigProviderInterface{
	public function getConfig(){
		return include __DIR__ . '/../config/module.config.php';
	}

	public function getServiceConfig(){
	    return[
	        'factories' =>[
	            Model\ScoreTable::class => function($container){
	                $tableGateway = $container->get(Model\ScoreTableGateway::class);
	                return new Model\ScoreTable($tableGateway);
                },
                Model\ScoreTableGateway::class => function($container){
                    $dbAdapter = $container->get(AdapterInterface::class);
                    $resultSetPrototype = new ResultSet();
                    $resultSetPrototype->setArrayObjectPrototype(new Model\Score());
                    return new Tablegateway('schedule',$dbAdapter,null,$resultSetPrototype);
                }
            ],
        ];
    }

    public function getControllerConfig(){
        return [
            'factories' => [
                Controller\ScoreController::class => function($container){
                    return new Controller\ScoreController(
                        $container->get(Model\ScoreTable::class)
                    );
                },
            ],
        ];
    }
}
