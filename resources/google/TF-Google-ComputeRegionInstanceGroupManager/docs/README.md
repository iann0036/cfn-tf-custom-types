# TF::Google::ComputeRegionInstanceGroupManager

The Google Compute Engine Regional Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template.

To get more information about regionInstanceGroupManagers, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers)
* How-to Guides
    * [Regional Instance Groups Guide](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)

~> **Note:** Use [google_compute_instance_group_manager](/docs/providers/google/r/compute_instance_group_manager.html) to create a zonal instance group manager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ComputeRegionInstanceGroupManager",
    "Properties" : {
        "<a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#distributionpolicytargetshape" title="DistributionPolicyTargetShape">DistributionPolicyTargetShape</a>" : <i>String</i>,
        "<a href="#distributionpolicyzones" title="DistributionPolicyZones">DistributionPolicyZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#targetpools" title="TargetPools">TargetPools</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetsize" title="TargetSize">TargetSize</a>" : <i>Double</i>,
        "<a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>" : <i>Boolean</i>,
        "<a href="#waitforinstancesstatus" title="WaitForInstancesStatus">WaitForInstancesStatus</a>" : <i>String</i>,
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
Type: TF::Google::ComputeRegionInstanceGroupManager
Properties:
    <a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#distributionpolicytargetshape" title="DistributionPolicyTargetShape">DistributionPolicyTargetShape</a>: <i>String</i>
    <a href="#distributionpolicyzones" title="DistributionPolicyZones">DistributionPolicyZones</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#targetpools" title="TargetPools">TargetPools</a>: <i>
      - String</i>
    <a href="#targetsize" title="TargetSize">TargetSize</a>: <i>Double</i>
    <a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>: <i>Boolean</i>
    <a href="#waitforinstancesstatus" title="WaitForInstancesStatus">WaitForInstancesStatus</a>: <i>String</i>
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

#### DistributionPolicyTargetShape

The shape to which the group converges either proactively or on resize events (depending on the value set in update_policy.0.instance_redistribution_type). For more information see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributionPolicyZones

The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).

_Required_: No

_Type_: List of String

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

#### Region

The region where the managed instance group resides. If not provided, the provider region is used.

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

The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForInstances

Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForInstancesStatus

When used with `wait_for_instances` it specifies the status to wait for.
When `STABLE` is specified this resource will wait until the instances are stable before returning. When `UPDATED` is
set, it will wait for the version target to be reached and any per instance configs to be effective as well as all
instances to be stable before returning. The possible values are `STABLE` and `UPDATED`.

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

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Status

Returns the <code>Status</code> value.

