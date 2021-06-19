# TF::Dome9::CloudaccountAws IamSafeDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awsgrouparn" title="AwsGroupArn">AwsGroupArn</a>" : <i>String</i>,
    "<a href="#awspolicyarn" title="AwsPolicyArn">AwsPolicyArn</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#restrictediamentities" title="RestrictedIamEntities">RestrictedIamEntities</a>" : <i>[ <a href="iamsafedefinition.md">IamSafeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awsgrouparn" title="AwsGroupArn">AwsGroupArn</a>: <i>String</i>
<a href="#awspolicyarn" title="AwsPolicyArn">AwsPolicyArn</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#restrictediamentities" title="RestrictedIamEntities">RestrictedIamEntities</a>: <i>
      - <a href="iamsafedefinition.md">IamSafeDefinition</a></i>
</pre>

## Properties

#### AwsGroupArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsPolicyArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedIamEntities

_Required_: No

_Type_: List of <a href="iamsafedefinition.md">IamSafeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

