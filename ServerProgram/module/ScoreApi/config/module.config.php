<?php
namespace ScoreApi;
use Zend\Router\Http\Segment;
use Zend\ServiceManager\Factory\InvokableFactory;
return [
    /**
     * Define route not found routes
     */
    'router' => [
        'routes' => [
            'score_api' =>[
                'type' => Segment::class,
                'options' =>[
                    'route' => '/api[/:action[/:name]]',
                    'constraints' =>[
                        'action' => '[a-zA-Z][a-zA-Z0-9_-]*',
                        'name' => '[a-zA-Z0-9_-]*',
                    ],
                    'defaults' => [
                        'controller' => Controller\ScoreApiController::class,
                        'action' => 'highScore'
                    ]
                ],
            ],
        ],
    ],
    /*'controllers' => [
        'factories' => [
            Controller\ScoreApiController::class => InvokableFactory::class,
        ],
    ],*/
    'view_manager' => [
        'strategies' => array(
            'ViewJsonStrategy',
        ),
    ],
];