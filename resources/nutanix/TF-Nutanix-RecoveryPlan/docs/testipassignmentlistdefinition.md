# TF::Nutanix::RecoveryPlan TestIpAssignmentListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipconfiglist" title="IpConfigList">IpConfigList</a>" : <i>[ <a href="ipconfiglistdefinition.md">IpConfigListDefinition</a>, ... ]</i>,
    "<a href="#vmreference" title="VmReference">VmReference</a>" : <i>[ <a href="vmreferencedefinition.md">VmReferenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipconfiglist" title="IpConfigList">IpConfigList</a>: <i>
      - <a href="ipconfiglistdefinition.md">IpConfigListDefinition</a></i>
<a href="#vmreference" title="VmReference">VmReference</a>: <i>
      - <a href="vmreferencedefinition.md">VmReferenceDefinition</a></i>
</pre>

## Properties

#### IpConfigList

_Required_: No

_Type_: List of <a href="ipconfiglistdefinition.md">IpConfigListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmReference

_Required_: No

_Type_: List of <a href="vmreferencedefinition.md">VmReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

