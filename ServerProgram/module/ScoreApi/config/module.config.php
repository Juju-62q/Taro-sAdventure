<?php
namespace ScoreApi;
use Zend\Router\Http\Segment;
use Zend\ServiceManager\Factory\InvokableFactory;

return[
    'controllers' =>[
        'factories' =>[
            Controller\ScoreApiController::class => InvokableFactory::class,
        ],
    ],

    'router' => [
        'routes' => [
            '404' => [
                'type' => Segment::class,
                'options' => [
                    'route' => '/:*',
                    'defaults' => [
                        'controller' => Controller\RouteNotFoundController::class,
                        'action' => 'routenotfound',
                    ],
                ],
                'priority' => -1000,
            ],
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
                        'action' => 'index',
                    ]
                ],
            ],
        ],
    ],

    'view_manager' => [
        'strategies' => array(
            'ViewJsonStrategy',
        ),
    ],
];