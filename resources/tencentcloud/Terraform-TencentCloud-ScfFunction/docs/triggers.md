# Terraform::TencentCloud::ScfFunction Triggers

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cosregion" title="CosRegion">CosRegion</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#triggerdesc" title="TriggerDesc">TriggerDesc</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cosregion" title="CosRegion">CosRegion</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#triggerdesc" title="TriggerDesc">TriggerDesc</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CosRegion

Region of cos bucket. if `type` is `cos`, `cos_region` is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the SCF function trigger, if `type` is `ckafka`, the format of name must be `<ckafkaInstanceId>-<topicId>`; if `type` is `cos`, the name is cos bucket id, other In any case, it can be combined arbitrarily. It can only contain English letters, numbers, connectors and underscores. The maximum length is 100.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerDesc

TriggerDesc of the SCF function trigger, parameter format of `timer` is linux cron expression; parameter of `cos` type is json string `{"event":"cos:ObjectCreated:*","filter":{"Prefix":"","Suffix":""}}`, where `event` is the cos event trigger, `Prefix` is the corresponding file prefix filter condition, `Suffix` is the suffix filter condition, if not need filter condition can not pass; `cmq` type does not pass this parameter; `ckafka` type parameter format is json string `{"maxMsgNum":"1","offset":"latest"}`; `apigw` type parameter format is json string `{"api":{"authRequired":"FALSE","requestConfig":{"method":"ANY"},"isIntegratedResponse":"FALSE"},"service":{"serviceId":"service-dqzh68sg"},"release":{"environmentName":"test"}}`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the SCF function trigger, support `cos`, `cmq`, `timer`, `ckafka`, `apigw`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

