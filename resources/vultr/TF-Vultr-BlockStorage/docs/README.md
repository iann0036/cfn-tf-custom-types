# TF::Vultr::BlockStorage

Provides a Vultr Block Storage resource. This can be used to create, read, modify, and delete Block Storage.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::BlockStorage",
    "Properties" : {
        "<a href="#attachedtoinstance" title="AttachedToInstance">AttachedToInstance</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#live" title="Live">Live</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sizegb" title="SizeGb">SizeGb</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::BlockStorage
Properties:
    <a href="#attachedtoinstance" title="AttachedToInstance">AttachedToInstance</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#live" title="Live">Live</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sizegb" title="SizeGb">SizeGb</a>: <i>Double</i>
</pre>

## Properties

#### AttachedToInstance

VPS ID that you want to have this block storage attached to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

Label that is given to your block storage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Live

Boolean value that will allow attachment of the volume to an instance without a restart. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Region in which this block storage will reside in. (Currently only NJ/NY supported region "ewr").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeGb

The size of the given block storage.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Cost

Returns the <code>Cost</code> value.

#### DateCreated

Returns the <code>DateCreated</code> value.

#### Id

Returns the <code>Id</code> value.

#### MountId

Returns the <code>MountId</code> value.

#### Status

Returns the <code>Status</code> value.

