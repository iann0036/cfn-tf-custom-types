# TF::GoogleBeta::GoogleComputeInstanceGroupManager

CloudFormation equivalent of google_compute_instance_group_manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleComputeInstanceGroupManager",
    "Properties" : {
        "<a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#targetpools" title="TargetPools">TargetPools</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetsize" title="TargetSize">TargetSize</a>" : <i>Double</i>,
        "<a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>" : <i>Boolean</i>,
        "<a href="#waitforinstancesstatus" title="WaitForInstancesStatus">WaitForInstancesStatus</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#autohealingpolicies" title="AutoHealingPolicies">AutoHealingPolicies</a>" : <i>[ <a href="autohealingpoliciesdefinition.md">AutoHealingPoliciesDefinition</a>, ... ]</i>,
        "<a href="#namedport" title="NamedPort">NamedPort</a>" : <i>[ <a href="namedportdefinition.md">NamedPortDefinition</a>, ... ]</i>,
        "<a href="#statefuldisk" title="StatefulDisk">StatefulDisk</a>" : <i>[ <a href="statefuldiskdefinition.md">StatefulDiskDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ <a href="updatepolicydefinition.md">UpdatePolicyDefinition</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>[ <a href="versiondefinition.md">VersionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleComputeInstanceGroupManager
Properties:
    <a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#targetpools" title="TargetPools">TargetPools</a>: <i>
      - String</i>
    <a href="#targetsize" title="TargetSize">TargetSize</a>: <i>Double</i>
    <a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>: <i>Boolean</i>
    <a href="#waitforinstancesstatus" title="WaitForInstancesStatus">WaitForInstancesStatus</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#autohealingpolicies" title="AutoHealingPolicies">AutoHealingPolicies</a>: <i>
      - <a href="autohealingpoliciesdefinition.md">AutoHealingPoliciesDefinition</a></i>
    <a href="#namedport" title="NamedPort">NamedPort</a>: <i>
      - <a href="namedportdefinition.md">NamedPortDefinition</a></i>
    <a href="#statefuldisk" title="StatefulDisk">StatefulDisk</a>: <i>
      - <a href="statefuldiskdefinition.md">StatefulDiskDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - <a href="updatepolicydefinition.md">UpdatePolicyDefinition</a></i>
    <a href="#version" title="Version">Version</a>: <i>
      - <a href="versiondefinition.md">VersionDefinition</a></i>
</pre>

## Properties

#### BaseInstanceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPools

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForInstancesStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoHealingPolicies

_Required_: No

_Type_: List of <a href="autohealingpoliciesdefinition.md">AutoHealingPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedPort

_Required_: No

_Type_: List of <a href="namedportdefinition.md">NamedPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulDisk

_Required_: No

_Type_: List of <a href="statefuldiskdefinition.md">StatefulDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of <a href="updatepolicydefinition.md">UpdatePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of <a href="versiondefinition.md">VersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceGroup

Returns the <code>InstanceGroup</code> value.

#### Operation

Returns the <code>Operation</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Status

Returns the <code>Status</code> value.

