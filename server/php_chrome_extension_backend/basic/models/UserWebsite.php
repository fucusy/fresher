<?php

namespace app\models;

use Yii;

/**
 * This is the model class for table "user_website".
 *
 * @property integer $user_id
 * @property integer $website_id
 *
 * @property User $user
 * @property Website $website
 */
class UserWebsite extends \yii\db\ActiveRecord
{
    /**
     * @inheritdoc
     */
    public static function tableName()
    {
        return 'user_website';
    }

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            [['user_id', 'website_id'], 'required'],
            [['user_id', 'website_id'], 'integer']
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeLabels()
    {
        return [
            'user_id' => 'User ID',
            'website_id' => 'Website ID',
        ];
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getUser()
    {
        return $this->hasOne(User::className(), ['user_id' => 'user_id']);
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getWebsite()
    {
        return $this->hasOne(Website::className(), ['website_id' => 'website_id']);
    }
}
