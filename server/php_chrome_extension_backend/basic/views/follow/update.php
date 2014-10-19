<?php

use yii\helpers\Html;

/* @var $this yii\web\View */
/* @var $model app\models\UserWebsite */

$this->title = 'Update User Website: ' . ' ' . $model->user_id;
$this->params['breadcrumbs'][] = ['label' => 'User Websites', 'url' => ['index']];
$this->params['breadcrumbs'][] = ['label' => $model->user_id, 'url' => ['view', 'user_id' => $model->user_id, 'website_id' => $model->website_id]];
$this->params['breadcrumbs'][] = 'Update';
?>
<div class="user-website-update">

    <h1><?= Html::encode($this->title) ?></h1>

    <?= $this->render('_form', [
        'model' => $model,
    ]) ?>

</div>
