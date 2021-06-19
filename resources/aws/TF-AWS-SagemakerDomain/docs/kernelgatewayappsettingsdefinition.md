# TF::AWS::SagemakerDomain KernelGatewayAppSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customimage" title="CustomImage">CustomImage</a>" : <i>[ <a href="customimagedefinition.md">CustomImageDefinition</a>, ... ]</i>,
    "<a href="#defaultresourcespec" title="DefaultResourceSpec">DefaultResourceSpec</a>" : <i>[ <a href="defaultresourcespecdefinition.md">DefaultResourceSpecDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customimage" title="CustomImage">CustomImage</a>: <i>
      - <a href="customimagedefinition.md">CustomImageDefinition</a></i>
<a href="#defaultresourcespec" title="DefaultResourceSpec">DefaultResourceSpec</a>: <i>
      - <a href="defaultresourcespecdefinition.md">DefaultResourceSpecDefinition</a></i>
</pre>

## Properties

#### CustomImage

_Required_: No

_Type_: List of <a href="customimagedefinition.md">CustomImageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultResourceSpec

_Required_: No

_Type_: List of <a href="defaultresourcespecdefinition.md">DefaultResourceSpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

