# TF::AWS::IotTopicRule Dynamodbv2Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#putitem" title="PutItem">PutItem</a>" : <i>[ <a href="putitemdefinition.md">PutItemDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#putitem" title="PutItem">PutItem</a>: <i>
      - <a href="putitemdefinition.md">PutItemDefinition</a></i>
</pre>

## Properties

#### RoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PutItem

_Required_: No

_Type_: List of <a href="putitemdefinition.md">PutItemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

