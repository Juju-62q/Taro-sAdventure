<?php
namespace Score;

use Zend\Router\Http\Literal;
use Zend\Router\Http\Segment;

return[
    /*'controllers' =>[
        'factories' =>[
            Controller\ScoreController::class => InvokableFactory::class,
        ],
    ],*/
    'router' =>[
        'routes' =>[
            'home' => [
                'type' => Literal::class,
                'options' => [
                    'route'    => '/',
                    'defaults' => [
                        'controller' => Controller\ScoreController::class,
                        'action'     => 'index',
                    ],
                ],
            ],
            'score' =>[
                'type' => Segment::class,
                'options' =>[
                    'route' => '/score[/:action[/:id]]',
                    'constraints' =>[
                        'action' => '[a-zA-Z][a-zA-Z0-9_-]*',
                        'id' => '[1-9][1-9]*',
                    ],
                    'defaults' => [
                        'controller' => Controller\ScoreController::class,
                        'action' => 'index',
                    ]
                ],
            ],
        ],
    ],
    'view_manager' => [
        'display_not_found_reason' => true,
        'display_exceptions'       => true,
        'doctype'                  => 'HTML5',
        'not_found_template'       => 'error/404',
        'exception_template'       => 'error/index',
        'template_map' => [
            'layout/layout'           => __DIR__ . '/../view/layout/layout.phtml',
            //'application/index/index' => __DIR__ . '/../view/application/index/index.phtml',
            'error/404'               => __DIR__ . '/../view/error/404.phtml',
            'error/index'             => __DIR__ . '/../view/error/index.phtml',
        ],
        'template_path_stack' =>[
            'score' => __DIR__ . '/../view'
        ],
    ],
];
