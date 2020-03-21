# Terraform::Google::ComputeInstanceGroupManager

The Google Compute Engine Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/manager)
and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers)

~> **Note:** Use [google_compute_region_instance_group_manager](/docs/providers/google/r/compute_region_instance_group_manager.html) to create a regional (multi-zone) instance group manager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeInstanceGroupManager",
    "Properties" : {
        "<a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#targetpools" title="TargetPools">TargetPools</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetsize" title="TargetSize">TargetSize</a>" : <i>[ <a href="targetsize.md">TargetSize</a>, ... ]</i>,
        "<a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>" : <i>Boolean</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#autohealingpolicies" title="AutoHealingPolicies">AutoHealingPolicies</a>" : <i>[ <a href="autohealingpolicies.md">AutoHealingPolicies</a>, ... ]</i>,
        "<a href="#namedport" title="NamedPort">NamedPort</a>" : <i>[ <a href="namedport.md">NamedPort</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ <a href="updatepolicy.md">UpdatePolicy</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>[ <a href="version.md">Version</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeInstanceGroupManager
Properties:
    <a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#targetpools" title="TargetPools">TargetPools</a>: <i>
      - String</i>
    <a href="#targetsize" title="TargetSize">TargetSize</a>: <i>
      - <a href="targetsize.md">TargetSize</a></i>
    <a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>: <i>Boolean</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#autohealingpolicies" title="AutoHealingPolicies">AutoHealingPolicies</a>: <i>
      - <a href="autohealingpolicies.md">AutoHealingPolicies</a></i>
    <a href="#namedport" title="NamedPort">NamedPort</a>: <i>
      - <a href="namedport.md">NamedPort</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - <a href="updatepolicy.md">UpdatePolicy</a></i>
    <a href="#version" title="Version">Version</a>: <i>
      - <a href="version.md">Version</a></i>
</pre>

## Properties

#### BaseInstanceName

The base instance name to use for
instances in this group. The value must be a valid
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

An optional textual description of the instance
group manager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the instance group manager. Must be 1-63
characters long and comply with
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Supported characters
include lowercase letters, numbers, and hyphens.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPools

The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSize

_Required_: No

_Type_: List of <a href="targetsize.md">TargetSize</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForInstances

Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The zone that instances in this group should be created
in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoHealingPolicies

_Required_: No

_Type_: List of <a href="autohealingpolicies.md">AutoHealingPolicies</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedPort

_Required_: No

_Type_: List of <a href="namedport.md">NamedPort</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of <a href="updatepolicy.md">UpdatePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of <a href="version.md">Version</a>

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

#### InstanceGroup

Returns the <code>InstanceGroup</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### UpdateStrategy

Returns the <code>UpdateStrategy</code> value.

