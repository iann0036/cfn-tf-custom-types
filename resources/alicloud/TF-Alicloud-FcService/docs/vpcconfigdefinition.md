# TF::Alicloud::FcService VpcConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
    "<a href="#vswitchids" title="VswitchIds">VswitchIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
<a href="#vswitchids" title="VswitchIds">VswitchIds</a>: <i>
      - String</i>
</pre>

## Properties

#### SecurityGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
