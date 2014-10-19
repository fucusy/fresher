<?php

namespace app\controllers;

use app\models\User;
use app\models\Website;
use Yii;
use app\models\UserWebsite;
use yii\data\ActiveDataProvider;
use yii\helpers\Html;
use yii\web\Controller;
use yii\web\NotFoundHttpException;
use yii\filters\VerbFilter;

/**
 * FollowController implements the CRUD actions for UserWebsite model.
 */
class FollowController extends Controller
{
    public function behaviors()
    {
        return [
            'verbs' => [
                'class' => VerbFilter::className(),
                'actions' => [
                    'delete' => ['post'],
                ],
            ],
        ];
    }

    /**
     * Lists all UserWebsite models.
     * @return mixed
     */
    public function actionIndex()
    {
        $dataProvider = new ActiveDataProvider([
            'query' => UserWebsite::find(),
        ]);

        return $this->render('index', [
            'dataProvider' => $dataProvider,
        ]);
    }

    /**
     * Displays a single UserWebsite model.
     * @param integer $user_id
     * @param integer $website_id
     * @return mixed
     */
    public function actionView($user_id, $website_id)
    {
        return $this->render('view', [
            'model' => $this->findModel($user_id, $website_id),
        ]);
    }

    /**
     * Creates a new UserWebsite model.
     * If creation is successful, the browser will be redirected to the 'view' page.
     * @return mixed
     */
    public function actionCreate($website_addr,$email)
    {

        $user = User::findOne(["email_addr" => $email]);
        if( $user == null )
        {
            $user = new User();
            $user->setAttribute("email_addr",$email);
            $user->date = date("y-m-d H:i:s");
            $user->save();
        }

        $website = Website::findOne(["website_address" => $website_addr]);
        if( $website == null )
        {
            $website = new Website();
            $website->website_address = $website_addr;
            $website->date = date("y-m-d H:i:s");
            $website->save();
        }

        $model = new UserWebsite();
        $model->user_id = $user->user_id;
        $model->website_id = $website->website_id;

        $model_exist = UserWebsite::findOne(["user_id"=>$model->user_id, "website_id"=>$model->website_id]);

        if( $model_exist)
            echo 0;
        else if( $model->save() )
            echo 1;
        else
            echo -1;
    }

    /**
     * Updates an existing UserWebsite model.
     * If update is successful, the browser will be redirected to the 'view' page.
     * @param integer $user_id
     * @param integer $website_id
     * @return mixed
     */
    public function actionUpdate($user_id, $website_id)
    {
        $model = $this->findModel($user_id, $website_id);

        if ($model->load(Yii::$app->request->post()) && $model->save()) {
            return $this->redirect(['view', 'user_id' => $model->user_id, 'website_id' => $model->website_id]);
        } else {
            return $this->render('update', [
                'model' => $model,
            ]);
        }
    }

    /**
     * Deletes an existing UserWebsite model.
     * If deletion is successful, the browser will be redirected to the 'index' page.
     * @param integer $user_id
     * @param integer $website_id
     * @return mixed
     */
    public function actionDelete($user_id, $website_id)
    {
        $this->findModel($user_id, $website_id)->delete();

        return $this->redirect(['index']);
    }

    /**
     * Finds the UserWebsite model based on its primary key value.
     * If the model is not found, a 404 HTTP exception will be thrown.
     * @param integer $user_id
     * @param integer $website_id
     * @return UserWebsite the loaded model
     * @throws NotFoundHttpException if the model cannot be found
     */
    protected function findModel($user_id, $website_id)
    {
        if (($model = UserWebsite::findOne(['user_id' => $user_id, 'website_id' => $website_id])) !== null) {
            return $model;
        } else {
            throw new NotFoundHttpException('The requested page does not exist.');
        }
    }
}
