<?php

use yii\helpers\Html;


/* @var $this yii\web\View */
/* @var $model app\models\UserWebsite */

$this->title = 'Create User Website';
$this->params['breadcrumbs'][] = ['label' => 'User Websites', 'url' => ['index']];
$this->params['breadcrumbs'][] = $this->title;
?>
<div class="user-website-create">

    <h1><?= Html::encode($this->title) ?></h1>

    <?= $this->render('_form', [
        'model' => $model,
    ]) ?>

</div>
