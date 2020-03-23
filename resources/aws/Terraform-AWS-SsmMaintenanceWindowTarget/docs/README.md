# Terraform::AWS::SsmMaintenanceWindowTarget

Provides an SSM Maintenance Window Target resource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmMaintenanceWindowTarget",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerinformation" title="OwnerInformation">OwnerInformation</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#windowid" title="WindowId">WindowId</a>" : <i>String</i>,
        "<a href="#targets" title="Targets">Targets</a>" : <i>[ <a href="targets.md">Targets</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmMaintenanceWindowTarget
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerinformation" title="OwnerInformation">OwnerInformation</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#windowid" title="WindowId">WindowId</a>: <i>String</i>
    <a href="#targets" title="Targets">Targets</a>: <i>
      - <a href="targets.md">Targets</a></i>
</pre>

## Properties

#### Description

The description of the maintenance window target.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the maintenance window target.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerInformation

User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowId

The Id of the maintenance window to register the target with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targets

_Required_: No

_Type_: List of <a href="targets.md">Targets</a>

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

