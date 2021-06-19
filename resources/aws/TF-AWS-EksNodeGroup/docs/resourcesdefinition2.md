# TF::AWS::EksNodeGroup ResourcesDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalinggroups" title="AutoscalingGroups">AutoscalingGroups</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>,
    "<a href="#remoteaccesssecuritygroupid" title="RemoteAccessSecurityGroupId">RemoteAccessSecurityGroupId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalinggroups" title="AutoscalingGroups">AutoscalingGroups</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
<a href="#remoteaccesssecuritygroupid" title="RemoteAccessSecurityGroupId">RemoteAccessSecurityGroupId</a>: <i>String</i>
</pre>

## Properties

#### AutoscalingGroups

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAccessSecurityGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

