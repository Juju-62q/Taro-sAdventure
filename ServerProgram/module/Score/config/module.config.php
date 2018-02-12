<?php
namespace Score;
use Zend\Router\Http\Segment;
use Zend\ServiceManager\Factory\InvokableFactory;

return[
    /*'controllers' =>[
        'factories' =>[
            Controller\ScoreController::class => InvokableFactory::class,
        ],
    ],*/
    'router' =>[
        'routes' =>[
            'score' =>[
                'type' => Segment::class,
                'options' =>[
                    'route' => '/score[/:action][/:id]',
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
    'view_manager' =>[
        'template_path_stack' =>[
            'score' => __DIR__ . '/../view'
        ],
    ],
];

return [
    'Zend\Form',
    'Zend\Db',
    'Zend\Router',
    'Zend\Validator',
    'Application',
    'Score',
];