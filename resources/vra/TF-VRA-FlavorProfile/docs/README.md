# TF::VRA::FlavorProfile

CloudFormation equivalent of vra_flavor_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::FlavorProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#regionid" title="RegionId">RegionId</a>" : <i>String</i>,
        "<a href="#flavormapping" title="FlavorMapping">FlavorMapping</a>" : <i>[ <a href="flavormappingdefinition.md">FlavorMappingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::FlavorProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#regionid" title="RegionId">RegionId</a>: <i>String</i>
    <a href="#flavormapping" title="FlavorMapping">FlavorMapping</a>: <i>
      - <a href="flavormappingdefinition.md">FlavorMappingDefinition</a></i>
</pre>

## Properties

#### Description

A human-friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human-friendly name used as an identifier in APIs that support this option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionId

The id of the region for which this profile is defined as in vRealize Automation(vRA).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorMapping

_Required_: No

_Type_: List of <a href="flavormappingdefinition.md">FlavorMappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudAccountId

Returns the <code>CloudAccountId</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### ExternalRegionId

Returns the <code>ExternalRegionId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Links

Returns the <code>Links</code> value.

#### OrgId

Returns the <code>OrgId</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

