# TF::VRA::Project

CloudFormation equivalent of vra_project

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::Project",
    "Properties" : {
        "<a href="#administrators" title="Administrators">Administrators</a>" : <i>[ String, ... ]</i>,
        "<a href="#customproperties" title="CustomProperties">CustomProperties</a>" : <i>[ <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#machinenamingtemplate" title="MachineNamingTemplate">MachineNamingTemplate</a>" : <i>String</i>,
        "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operationtimeout" title="OperationTimeout">OperationTimeout</a>" : <i>Double</i>,
        "<a href="#sharedresources" title="SharedResources">SharedResources</a>" : <i>Boolean</i>,
        "<a href="#viewers" title="Viewers">Viewers</a>" : <i>[ String, ... ]</i>,
        "<a href="#constraints" title="Constraints">Constraints</a>" : <i>[ <a href="constraintsdefinition.md">ConstraintsDefinition</a>, ... ]</i>,
        "<a href="#zoneassignments" title="ZoneAssignments">ZoneAssignments</a>" : <i>[ <a href="zoneassignmentsdefinition.md">ZoneAssignmentsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::Project
Properties:
    <a href="#administrators" title="Administrators">Administrators</a>: <i>
      - String</i>
    <a href="#customproperties" title="CustomProperties">CustomProperties</a>: <i>
      - <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#machinenamingtemplate" title="MachineNamingTemplate">MachineNamingTemplate</a>: <i>String</i>
    <a href="#members" title="Members">Members</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operationtimeout" title="OperationTimeout">OperationTimeout</a>: <i>Double</i>
    <a href="#sharedresources" title="SharedResources">SharedResources</a>: <i>Boolean</i>
    <a href="#viewers" title="Viewers">Viewers</a>: <i>
      - String</i>
    <a href="#constraints" title="Constraints">Constraints</a>: <i>
      - <a href="constraintsdefinition.md">ConstraintsDefinition</a></i>
    <a href="#zoneassignments" title="ZoneAssignments">ZoneAssignments</a>: <i>
      - <a href="zoneassignmentsdefinition.md">ZoneAssignmentsDefinition</a></i>
</pre>

## Properties

#### Administrators

List of administrator users associated with the project. Only administrators can manage project's configuration.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProperties

The project custom properties which are added to all requests in this project.

_Required_: No

_Type_: List of <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineNamingTemplate

The naming template to be used for resources provisioned in this project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

List of member users associated with the project.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human-friendly name used as an identifier in APIs that support this option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationTimeout

The timeout that should be used for Blueprint operations and Provisioning tasks. The timeout is in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedResources

Specifies whether the resources in this projects are shared or not. If not set default will be used.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Viewers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Constraints

_Required_: No

_Type_: List of <a href="constraintsdefinition.md">ConstraintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneAssignments

_Required_: No

_Type_: List of <a href="zoneassignmentsdefinition.md">ZoneAssignmentsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

