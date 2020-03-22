# Terraform::AWS::WafWebAcl

CloudFormation equivalent of aws_waf_web_acl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::WafWebAcl",
    "Properties" : {
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>[ <a href="defaultaction.md">DefaultAction</a>, ... ]</i>,
        "<a href="#loggingconfiguration" title="LoggingConfiguration">LoggingConfiguration</a>" : <i>[ <a href="loggingconfiguration.md">LoggingConfiguration</a>, ... ]</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rules.md">Rules</a>, ... ]</i>,
        "<a href="#redactedfields" title="RedactedFields">RedactedFields</a>" : <i>[ <a href="redactedfields.md">RedactedFields</a>, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ <a href="action.md">Action</a>, ... ]</i>,
        "<a href="#overrideaction" title="OverrideAction">OverrideAction</a>" : <i>[ <a href="overrideaction.md">OverrideAction</a>, ... ]</i>,
        "<a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>" : <i>[ <a href="fieldtomatch.md">FieldToMatch</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::WafWebAcl
Properties:
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>
      - <a href="defaultaction.md">DefaultAction</a></i>
    <a href="#loggingconfiguration" title="LoggingConfiguration">LoggingConfiguration</a>: <i>
      - <a href="loggingconfiguration.md">LoggingConfiguration</a></i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rules.md">Rules</a></i>
    <a href="#redactedfields" title="RedactedFields">RedactedFields</a>: <i>
      - <a href="redactedfields.md">RedactedFields</a></i>
    <a href="#action" title="Action">Action</a>: <i>
      - <a href="action.md">Action</a></i>
    <a href="#overrideaction" title="OverrideAction">OverrideAction</a>: <i>
      - <a href="overrideaction.md">OverrideAction</a></i>
    <a href="#fieldtomatch" title="FieldToMatch">FieldToMatch</a>: <i>
      - <a href="fieldtomatch.md">FieldToMatch</a></i>
</pre>

## Properties

#### MetricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

_Required_: No

_Type_: List of <a href="defaultaction.md">DefaultAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfiguration

_Required_: No

_Type_: List of <a href="loggingconfiguration.md">LoggingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rules.md">Rules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedactedFields

_Required_: No

_Type_: List of <a href="redactedfields.md">RedactedFields</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="action.md">Action</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAction

_Required_: No

_Type_: List of <a href="overrideaction.md">OverrideAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldToMatch

_Required_: No

_Type_: List of <a href="fieldtomatch.md">FieldToMatch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

