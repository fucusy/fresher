<?php
/**
 * Created by PhpStorm.
 * User: user
 * Date: 14-10-18
 * Time: 下午3:23
 */

namespace app\controllers;

use yii\rest\ActiveController;

class UserController extends ActiveController
{
    public $modelClass = 'app\models\Country';
}