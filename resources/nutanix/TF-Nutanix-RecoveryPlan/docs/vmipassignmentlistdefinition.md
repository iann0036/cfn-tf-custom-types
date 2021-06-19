# TF::Nutanix::RecoveryPlan VmIpAssignmentListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#recoveryfloatingipconfig" title="RecoveryFloatingIpConfig">RecoveryFloatingIpConfig</a>" : <i>[ <a href="recoveryfloatingipconfigdefinition.md">RecoveryFloatingIpConfigDefinition</a>, ... ]</i>,
    "<a href="#testfloatingipconfig" title="TestFloatingIpConfig">TestFloatingIpConfig</a>" : <i>[ <a href="testfloatingipconfigdefinition.md">TestFloatingIpConfigDefinition</a>, ... ]</i>,
    "<a href="#vmnicinformation" title="VmNicInformation">VmNicInformation</a>" : <i>[ <a href="vmnicinformationdefinition.md">VmNicInformationDefinition</a>, ... ]</i>,
    "<a href="#vmreference" title="VmReference">VmReference</a>" : <i>[ <a href="vmreferencedefinition.md">VmReferenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#recoveryfloatingipconfig" title="RecoveryFloatingIpConfig">RecoveryFloatingIpConfig</a>: <i>
      - <a href="recoveryfloatingipconfigdefinition.md">RecoveryFloatingIpConfigDefinition</a></i>
<a href="#testfloatingipconfig" title="TestFloatingIpConfig">TestFloatingIpConfig</a>: <i>
      - <a href="testfloatingipconfigdefinition.md">TestFloatingIpConfigDefinition</a></i>
<a href="#vmnicinformation" title="VmNicInformation">VmNicInformation</a>: <i>
      - <a href="vmnicinformationdefinition.md">VmNicInformationDefinition</a></i>
<a href="#vmreference" title="VmReference">VmReference</a>: <i>
      - <a href="vmreferencedefinition.md">VmReferenceDefinition</a></i>
</pre>

## Properties

#### RecoveryFloatingIpConfig

_Required_: No

_Type_: List of <a href="recoveryfloatingipconfigdefinition.md">RecoveryFloatingIpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestFloatingIpConfig

_Required_: No

_Type_: List of <a href="testfloatingipconfigdefinition.md">TestFloatingIpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmNicInformation

_Required_: No

_Type_: List of <a href="vmnicinformationdefinition.md">VmNicInformationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmReference

_Required_: No

_Type_: List of <a href="vmreferencedefinition.md">VmReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

