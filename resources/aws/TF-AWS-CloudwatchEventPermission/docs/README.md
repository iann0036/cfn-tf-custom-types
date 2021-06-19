# TF::AWS::CloudwatchEventPermission

Provides a resource to create an EventBridge permission to support cross-account events in the current account default event bus.

~> **Note:** EventBridge was formerly known as CloudWatch Events. The functionality is identical.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchEventPermission",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#eventbusname" title="EventBusName">EventBusName</a>" : <i>String</i>,
        "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>,
        "<a href="#statementid" title="StatementId">StatementId</a>" : <i>String</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="conditiondefinition.md">ConditionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchEventPermission
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#eventbusname" title="EventBusName">EventBusName</a>: <i>String</i>
    <a href="#principal" title="Principal">Principal</a>: <i>String</i>
    <a href="#statementid" title="StatementId">StatementId</a>: <i>String</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="conditiondefinition.md">ConditionDefinition</a></i>
</pre>

## Properties

#### Action

The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventBusName

The event bus to set the permissions on. If you omit this, the permissions are set on the `default` event bus.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Principal

The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus, optionally limited by `condition`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatementId

An identifier string for the external account that you are granting permissions to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="conditiondefinition.md">ConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

