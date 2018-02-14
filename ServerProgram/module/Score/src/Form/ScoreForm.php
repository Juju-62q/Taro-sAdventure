<?php
namespace Score\Form;

use Zend\Form\Form;

class ScoreForm extends Form{
    public function __construct($name = null)
    {
        parent::__construct('score');

        $this->add([
            'name' => 'id',
            'type' => 'hidden',
        ]);
        $this->add([
            'name' => 'name',
            'type' => 'text',
            'options' => [
                'label' => 'Name',
            ],
        ]);
        $this->add([
            'name' => 'score',
            'type' => 'number',
            'options' => [
                'label' => 'Score',
            ],
        ]);
        $this->add([
            'name' => 'created_at',
            'type' => 'hidden',
        ]);
        $this->add([
            'name' => 'submit',
            'type' => 'submit',
            'attributes' => [
                'value' => 'Go',
                'id'    => 'submitbutton',
            ],
        ]);
    }
}