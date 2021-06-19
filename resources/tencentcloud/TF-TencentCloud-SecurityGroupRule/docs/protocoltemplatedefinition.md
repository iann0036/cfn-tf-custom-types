# TF::TencentCloud::SecurityGroupRule ProtocolTemplateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
    "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
<a href="#templateid" title="TemplateId">TemplateId</a>: <i>String</i>
</pre>

## Properties

#### GroupId

Address template group ID, conflicts with `template_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

Address template ID, conflicts with `group_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

