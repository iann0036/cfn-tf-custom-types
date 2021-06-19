# TF::Panos::VmAuthKey

Creates a VM auth key you can use to bootstrap a VM NGFW.

**NOTE:** This is for Panorama only.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::VmAuthKey",
    "Properties" : {
        "<a href="#hours" title="Hours">Hours</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::VmAuthKey
Properties:
    <a href="#hours" title="Hours">Hours</a>: <i>Double</i>
</pre>

## Properties

#### Hours

The VM auth key lifetime in hours.

_Required_: No

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

#### AuthKey

Returns the <code>AuthKey</code> value.

#### Expiry

Returns the <code>Expiry</code> value.

#### Id

Returns the <code>Id</code> value.

#### Valid

Returns the <code>Valid</code> value.

