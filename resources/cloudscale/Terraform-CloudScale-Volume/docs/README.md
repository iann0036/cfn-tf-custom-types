# Terraform::CloudScale::Volume

Provides a cloudscale.ch Volume (block storage) resource. This can be used to create, modify, and delete Volumes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudScale::Volume",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#serveruuids" title="ServerUuids">ServerUuids</a>" : <i>[ String, ... ]</i>,
        "<a href="#sizegb" title="SizeGb">SizeGb</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudScale::Volume
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#serveruuids" title="ServerUuids">ServerUuids</a>: <i>
      - String</i>
    <a href="#sizegb" title="SizeGb">SizeGb</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>: <i>String</i>
</pre>

## Properties

#### Name

Name of the new volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerUuids

A list of server UUIDs. Default to an empty list. Currently a volume can only be attached to one server UUID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeGb

The volume size in GB. Valid values are multiples of 1 for type "ssd" and multiples of 100 for type "bulk".

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

For SSD/NVMe volumes specify "ssd" (default) or use "bulk" for our HDD cluster with NVMe caching. This is the only attribute that cannot be altered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneSlug

You can specify a zone slug. Options include `lpg1` and `rma1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Href

Returns the <code>Href</code> value.

#### Id

Returns the <code>Id</code> value.

