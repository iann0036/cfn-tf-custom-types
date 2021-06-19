# TF::Nutanix::ProtectionRule

Provides a Nutanix Protection Rule resource to Create a Protection Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nutanix::ProtectionRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
        "<a href="#availabilityzoneconnectivitylist" title="AvailabilityZoneConnectivityList">AvailabilityZoneConnectivityList</a>" : <i>[ <a href="availabilityzoneconnectivitylistdefinition.md">AvailabilityZoneConnectivityListDefinition</a>, ... ]</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>,
        "<a href="#categoryfilter" title="CategoryFilter">CategoryFilter</a>" : <i>[ <a href="categoryfilterdefinition.md">CategoryFilterDefinition</a>, ... ]</i>,
        "<a href="#orderedavailabilityzonelist" title="OrderedAvailabilityZoneList">OrderedAvailabilityZoneList</a>" : <i>[ <a href="orderedavailabilityzonelistdefinition.md">OrderedAvailabilityZoneListDefinition</a>, ... ]</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>, ... ]</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nutanix::ProtectionRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
    <a href="#availabilityzoneconnectivitylist" title="AvailabilityZoneConnectivityList">AvailabilityZoneConnectivityList</a>: <i>
      - <a href="availabilityzoneconnectivitylistdefinition.md">AvailabilityZoneConnectivityListDefinition</a></i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
    <a href="#categoryfilter" title="CategoryFilter">CategoryFilter</a>: <i>
      - <a href="categoryfilterdefinition.md">CategoryFilterDefinition</a></i>
    <a href="#orderedavailabilityzonelist" title="OrderedAvailabilityZoneList">OrderedAvailabilityZoneList</a>: <i>
      - <a href="orderedavailabilityzonelistdefinition.md">OrderedAvailabilityZoneListDefinition</a></i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a></i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a></i>
</pre>

## Properties

#### Description

A description for protection rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for the protection rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZoneConnectivityList

_Required_: No

_Type_: List of <a href="availabilityzoneconnectivitylistdefinition.md">AvailabilityZoneConnectivityListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CategoryFilter

_Required_: No

_Type_: List of <a href="categoryfilterdefinition.md">CategoryFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedAvailabilityZoneList

_Required_: No

_Type_: List of <a href="orderedavailabilityzonelistdefinition.md">OrderedAvailabilityZoneListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### State

Returns the <code>State</code> value.

