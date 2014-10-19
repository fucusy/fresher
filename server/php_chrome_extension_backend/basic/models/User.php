<?php

namespace app\models;

use Yii;

/**
 * This is the model class for table "user".
 *
 * @property integer $user_id
 * @property string $email_addr
 * @property string $date
 *
 * @property Push[] $pushes
 * @property UserWebsite[] $userWebsites
 * @property Website[] $websites
 */
class User extends \yii\db\ActiveRecord
{
    /**
     * @inheritdoc
     */
    public static function tableName()
    {
        return 'user';
    }

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            [['email_addr'], 'required'],
            [['date'], 'safe'],
            [['email_addr'], 'string', 'max' => 145]
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeLabels()
    {
        return [
            'user_id' => 'User ID',
            'email_addr' => 'Email Addr',
            'date' => 'Date',
        ];
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getPushes()
    {
        return $this->hasMany(Push::className(), ['user_id' => 'user_id']);
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getUserWebsites()
    {
        return $this->hasMany(UserWebsite::className(), ['user_id' => 'user_id']);
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getWebsites()
    {
        return $this->hasMany(Website::className(), ['website_id' => 'website_id'])->viaTable('user_website', ['user_id' => 'user_id']);
    }
}
