# TF::VRA::Machine

CloudFormation equivalent of vra_machine

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::Machine",
    "Properties" : {
        "<a href="#customproperties" title="CustomProperties">CustomProperties</a>" : <i>[ <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>, ... ]</i>,
        "<a href="#deploymentid" title="DeploymentId">DeploymentId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#flavor" title="Flavor">Flavor</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#imageref" title="ImageRef">ImageRef</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#bootconfig" title="BootConfig">BootConfig</a>" : <i>[ <a href="bootconfigdefinition.md">BootConfigDefinition</a>, ... ]</i>,
        "<a href="#constraints" title="Constraints">Constraints</a>" : <i>[ <a href="constraintsdefinition.md">ConstraintsDefinition</a>, ... ]</i>,
        "<a href="#disks" title="Disks">Disks</a>" : <i>[ <a href="disksdefinition.md">DisksDefinition</a>, ... ]</i>,
        "<a href="#imagediskconstraints" title="ImageDiskConstraints">ImageDiskConstraints</a>" : <i>[ <a href="imagediskconstraintsdefinition.md">ImageDiskConstraintsDefinition</a>, ... ]</i>,
        "<a href="#nics" title="Nics">Nics</a>" : <i>[ <a href="nicsdefinition.md">NicsDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::Machine
Properties:
    <a href="#customproperties" title="CustomProperties">CustomProperties</a>: <i>
      - <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a></i>
    <a href="#deploymentid" title="DeploymentId">DeploymentId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#flavor" title="Flavor">Flavor</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#imageref" title="ImageRef">ImageRef</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#bootconfig" title="BootConfig">BootConfig</a>: <i>
      - <a href="bootconfigdefinition.md">BootConfigDefinition</a></i>
    <a href="#constraints" title="Constraints">Constraints</a>: <i>
      - <a href="constraintsdefinition.md">ConstraintsDefinition</a></i>
    <a href="#disks" title="Disks">Disks</a>: <i>
      - <a href="disksdefinition.md">DisksDefinition</a></i>
    <a href="#imagediskconstraints" title="ImageDiskConstraints">ImageDiskConstraints</a>: <i>
      - <a href="imagediskconstraintsdefinition.md">ImageDiskConstraintsDefinition</a></i>
    <a href="#nics" title="Nics">Nics</a>: <i>
      - <a href="nicsdefinition.md">NicsDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CustomProperties

Additional properties that may be used to extend the base resource.

_Required_: No

_Type_: List of <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentId

Deployment id that is associated with this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flavor

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human-friendly name used as an identifier in APIs that support this option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The id of the project this resource belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootConfig

_Required_: No

_Type_: List of <a href="bootconfigdefinition.md">BootConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Constraints

_Required_: No

_Type_: List of <a href="constraintsdefinition.md">ConstraintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disks

_Required_: No

_Type_: List of <a href="disksdefinition.md">DisksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageDiskConstraints

_Required_: No

_Type_: List of <a href="imagediskconstraintsdefinition.md">ImageDiskConstraintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nics

_Required_: No

_Type_: List of <a href="nicsdefinition.md">NicsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Address

Returns the <code>Address</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### DisksList

Returns the <code>DisksList</code> value.

#### ExternalId

Returns the <code>ExternalId</code> value.

#### ExternalRegionId

Returns the <code>ExternalRegionId</code> value.

#### ExternalZoneId

Returns the <code>ExternalZoneId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Links

Returns the <code>Links</code> value.

#### OrganizationId

Returns the <code>OrganizationId</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### PowerState

Returns the <code>PowerState</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

