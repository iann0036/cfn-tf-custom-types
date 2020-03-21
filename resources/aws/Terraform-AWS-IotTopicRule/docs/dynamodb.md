# Terraform::AWS::IotTopicRule Dynamodb

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hashkeyfield" title="HashKeyField">HashKeyField</a>" : <i>String</i>,
    "<a href="#hashkeytype" title="HashKeyType">HashKeyType</a>" : <i>String</i>,
    "<a href="#hashkeyvalue" title="HashKeyValue">HashKeyValue</a>" : <i>String</i>,
    "<a href="#payloadfield" title="PayloadField">PayloadField</a>" : <i>String</i>,
    "<a href="#rangekeyfield" title="RangeKeyField">RangeKeyField</a>" : <i>String</i>,
    "<a href="#rangekeytype" title="RangeKeyType">RangeKeyType</a>" : <i>String</i>,
    "<a href="#rangekeyvalue" title="RangeKeyValue">RangeKeyValue</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hashkeyfield" title="HashKeyField">HashKeyField</a>: <i>String</i>
<a href="#hashkeytype" title="HashKeyType">HashKeyType</a>: <i>String</i>
<a href="#hashkeyvalue" title="HashKeyValue">HashKeyValue</a>: <i>String</i>
<a href="#payloadfield" title="PayloadField">PayloadField</a>: <i>String</i>
<a href="#rangekeyfield" title="RangeKeyField">RangeKeyField</a>: <i>String</i>
<a href="#rangekeytype" title="RangeKeyType">RangeKeyType</a>: <i>String</i>
<a href="#rangekeyvalue" title="RangeKeyValue">RangeKeyValue</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#tablename" title="TableName">TableName</a>: <i>String</i>
</pre>

## Properties

#### HashKeyField

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashKeyType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashKeyValue

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayloadField

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeKeyField

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeKeyType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeKeyValue

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

