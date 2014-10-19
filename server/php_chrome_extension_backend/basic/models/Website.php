<?php

namespace app\models;

use Yii;

/**
 * This is the model class for table "website".
 *
 * @property integer $website_id
 * @property string $website_address
 * @property string $date
 *
 * @property Push[] $pushes
 * @property UserWebsite[] $userWebsites
 * @property User[] $users
 * @property WebsiteHistory[] $websiteHistories
 */
class Website extends \yii\db\ActiveRecord
{
    /**
     * @inheritdoc
     */
    public static function tableName()
    {
        return 'website';
    }

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            [['website_address'], 'required'],
            [['date'], 'safe'],
            [['website_address'], 'string', 'max' => 245]
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeLabels()
    {
        return [
            'website_id' => 'Website ID',
            'website_address' => 'Website Address',
            'date' => 'Date',
        ];
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getPushes()
    {
        return $this->hasMany(Push::className(), ['website_id' => 'website_id']);
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getUserWebsites()
    {
        return $this->hasMany(UserWebsite::className(), ['website_id' => 'website_id']);
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getUsers()
    {
        return $this->hasMany(User::className(), ['user_id' => 'user_id'])->viaTable('user_website', ['website_id' => 'website_id']);
    }

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getWebsiteHistories()
    {
        return $this->hasMany(WebsiteHistory::className(), ['website_id' => 'website_id']);
    }
}
